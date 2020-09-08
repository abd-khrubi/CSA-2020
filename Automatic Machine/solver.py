import json

import numpy as np

# Globals
max_idx = 0
CHAR_SET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.!@#$%^&*()-_=+`~ {}'


class Data:
	def __init__(self, idx):
		self.idx = idx
		self.values = {ord(x): np.asarray([x], dtype=str) for x in CHAR_SET}

	def apply(self, cond):
		new_values = dict()
		for val in self.values:
			if not (val % cond):
				new_val = np.floor(val / cond)
			else:
				new_val = val
			if new_val not in new_values:
				new_values[new_val] = self.values[val]
			else:
				new_values[new_val].append(self.values[val])
		self.values = new_values

	def filter(self, cond, positive):
		"""
		3 = positive (True)
		4 = negative (False)
		"""
		f = filter(lambda char: not ((char % cond == 0) == positive), self.values)
		self.values = {key: self.values[key] for key in f}

	def __getitem__(self, item):
		if item in self.values:
			return self.values[item]
		return []

	def get(self):
		lst = set()
		for k in self.values:
			lst = lst.union(set(self.values[k]))
		return lst


class MyList:

	def __init__(self):
		self.available = {}

	def __getitem__(self, idx) -> Data:
		if idx not in self.available:
			self.available[idx] = Data(idx)
		return self.available[idx]


def func_1(arr, idx_from, idx_to, val):
	arr[idx_from: idx_to] += val


def func_2(arr, idx_from, idx_to, val):
	arr[idx_from: idx_to] -= val


def func_3(arr, idx_from, idx_to, val):
	arr[idx_from: idx_to] ^= val


def decode_text(arr, idx_from):
	num = arr[idx_from + 1]
	txt = ''
	for idx in range(num):
		txt += chr(arr[idx_from + 2 + idx] ^ 0x37)
	return txt


funcs = [func_1, func_2, func_3]


def decode(arr, input_arr: MyList):
	"""
		arr: copy of array `a`
		input_arr: user input as ascii codes
	"""
	global max_idx

	idx = 0
	while idx < len(arr):
		if max_idx < idx < 17251:
			max_idx = idx
		num = arr[idx]

		if num == 5:
			return decode_text(arr, idx)

		input_idx = arr[idx + 1]
		condition = arr[idx + 2]

		input_arr[input_idx].filter(condition, bool(4 - num))
		input_arr[input_idx].apply(condition)

		func_idx = arr[idx + 4]
		j = arr[idx + 5]
		i = arr[idx + 6] ^ (num - 3)
		val = arr[i]
		func = funcs[func_idx]
		func(arr, idx + 7, (j + 1) * 7, val)
		idx += 7


if __name__ == '__main__':
	my_lst = MyList()
	with open('array.json') as f:
		a = json.loads(f.read())

	print(decode(np.asarray(a[:]), my_lst))
	flag = ''
	for k in sorted(my_lst.available.keys()):
		flag += list(my_lst[k].get())[0]
	print(flag)
