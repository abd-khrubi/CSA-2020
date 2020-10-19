import struct
import sys
from http.client import HTTPResponse
from io import BytesIO
from ipaddress import ip_address
from socket import socket
from zlib import crc32

from pwn import remote, context

context.log_level = 'ERROR'

FIRST_MESSAGE = b'\x01\xfe'
CHALLENGE_RESPONSE = b'\x5a%s%s'  # (third char from the challenge, xor result)
IP_REQUEST = b'\x01\x00\x01%s\x00\x50'
REQUIRED_IP = '192.168.173.20'

XOR_KEY = b'CSA'

SERVER = '52.28.255.56', 1080

GET_REQUEST = '''GET /%s HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36
Host: checkpoint.com
Accept-language: en-us
Connection: Keep-Alive

'''.replace('\n', '\r\n')


def format_message(msg: bytes):
	"""
		format a message to be sent to the server by adding the byte '0x5a' to the beginning
		and the crc32 checksum to the end
	"""
	msg = b'\x5a' + msg
	return msg + struct.pack('>I', crc32(msg))


def calculate_response(challenge: bytes):
	"""
	Calculates the response to the server's challenge by xor-ing the incoming message with 'CSA' and
	concatenating the crc32 checksum to the end of the response
	"""
	secret = challenge[3:6]
	response = struct.pack('BBBB', challenge[2], *[secret[i] ^ XOR_KEY[i] for i in range(len(secret))])
	return format_message(response)


def format_ip_request():
	ip = ip_address(REQUIRED_IP).packed
	return format_message(IP_REQUEST % ip)


def get_file(file: str):
	data = None
	try:
		with remote(*SERVER, timeout=5) as r:
			r.send(format_message(FIRST_MESSAGE))
			challenge = r.recv(10)
			r.send(calculate_response(challenge))
			r.send(format_ip_request())
			r.recv(14)  # server confirmation
			r.send(GET_REQUEST % file)
			data = r.recvall()
	except Exception as e:
		print('Failed: ', e)
	return data


# if not data:
# 	return b''
# idx = data.split(b'\r\n').index(b'')
# payload = data.split(b'\r\n')[idx + 1:]
# payload = b''.join(payload)
# return payload

class FakeSocket(socket):
	def __init__(self, response_bytes):
		super().__init__()
		self._file = BytesIO(response_bytes)

	def makefile(self, *args, **kwargs):
		return self._file


def parse_get_response(response_bytes):
	source = FakeSocket(response_bytes)
	response = HTTPResponse(source)
	response.begin()
	return response.status, response.reason, response.read()


if __name__ == '__main__':
	if len(sys.argv) > 1:
		flag_file = sys.argv[1]
	else:
		flag_file = 'Flag.jpg'
	if flag_file == '/':
		flag_file = 'index.html'
	print(f'Reading file: {flag_file}')
	code, reason, body = parse_get_response(get_file(flag_file))
	if code != 200:
		print('HTTP GET error:', code, reason)
	else:
		with open(flag_file, 'wb') as f:
			f.write(body)
			print('Success')
