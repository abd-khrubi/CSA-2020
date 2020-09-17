from pwn import remote, context
from Crypto.Cipher import ARC4
from itertools import product

context.log_level = 'ERROR'

SERVER = '3.126.154.76', 80
RC4_KEY = b'csa-mitm-key'

LENGTHS = [13, 15, 2, 3, 2, 14, 6, 7, 8, 10]  # lengths of the secret combination words in order (including the '\n')


def load_dict():
    with open('dictionary.txt') as f:
        return list(map(lambda w: w.strip(), f.readlines()))


def get_possible_words(words, lengths):
    answers = []
    for length in lengths:
        answers.append(list(filter(lambda x: len(x) == length - 1, words)))

    return answers


def get_combinations(words, lengths):
    answers = get_possible_words(words, lengths)
    return list(product(*answers))


def try_combination(combination):
    cipher = ARC4.new(RC4_KEY)

    combination = '\n'.join(combination) + '\n'

    with remote(*SERVER) as r:
        r.recvline()  # the RC4 key message

        welcome_msg = r.recv(32)  # encrypted welcome message
        cipher.decrypt(welcome_msg)  # should decrypt to "Hi! what's the secret sequence?\n"

        r.send(cipher.encrypt(combination.encode()))

        response = r.recvall()
        return cipher.decrypt(response)


def main():
    words = load_dict()
    combinations = get_combinations(words, LENGTHS)
    print(f'Trying all {len(combinations)} different combinations...')
    for i in range(len(combinations)):
        p = (i + 1) / len(combinations)
        print(f'\r[{"=" * int(25 * p)}{" " * int(25 * (1 - p))}] - {p * 100: 0.2f}%', end='', flush=True)
        comb = combinations[i]
        # print(f'Trying combination: "{" ".join(comb)}" => ', end='', flush=True)
        response = try_combination(comb)
        if not response.isascii():
            print('Error decoding response')
        elif b'CSA' in response:
            print('\nFound the flag!')
            print(response.decode('ascii'))
            print(f'The secret combination is: {" ".join(comb)}')


if __name__ == '__main__':
    main()
