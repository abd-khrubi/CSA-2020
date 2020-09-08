from base64 import standard_b64decode

import matplotlib.pyplot as plt


def lsb_decode(img):
	txt = ''
	data = (img.flatten() * 255).astype(int)
	for i in range(0, len(data), 8):
		k = 0
		for j in range(8):
			k = (k << 1) + (data[i + j] & 1)
		c = chr(k)
		txt += c
	return txt


def main():
	img = plt.imread('image2.png')
	code = lsb_decode(img)[3:51]
	flag = standard_b64decode(standard_b64decode(code)).decode('ascii')
	print(flag)


if __name__ == '__main__':
	main()
