from random import choice

from pwn import remote

SERVER = 'tricky-guess.csa-challenge.com', 2222


def main():
	with open('words.txt') as f:
		words = f.readlines()
	words = list(map(lambda w: w.strip(), words))
	r = remote(*SERVER)
	r.recvline_contains('GO')
	while len(words) > 0:
		word = choice(words)
		r.sendline(word)
		hint = r.recvline(timeout=1).strip().decode('ascii')
		if hint.isdigit():
			hint = int(hint)
			words = list(filter(lambda w: len(set(w).intersection(word)) == hint, words))
		elif hint.startswith('csa'):
			print('The flag is:', hint)
			r.close()
			return
	r.close()
	print('Could not get the flag')


if __name__ == '__main__':
	main()
