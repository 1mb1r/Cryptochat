import json
import os
import hashlib
from time import time

# path to chain dir
chain_dir = os.curdir + '/chain/'
files = os.listdir(chain_dir)
files = sorted(int(i) for i in files)

def get_hash(file_name):          # hash def \__0__/
	file = open(chain_dir + file_name, 'rb').read()# указываем имя файла, который мы открываем для чтения с указанием папки
	return hashlib.sha256(file).hexdigest()

def check_integrity():
    for file in files[1:]:
        h = json.load(open(chain_dir + str(file)))['hash']
        actual_hash = get_hash(str(file - 1))

        prev_block = str(file -1)

        if h == actual_hash:
            res = 'kk'
        else:
            res = 'corrupted'
        print('block {} is {}'.format(prev_block, res))


def get_files():
	files = os.listdir(chain_dir)# получили список всех файлов, хранящихся в папке chain
	return sorted([int(i) for i in files])# сортируем названия файлов в порядке возрастания, как целочисленные значения


def write_block(sender, amount, message, recipient, prev_hash=''):
	files = get_files()
	prev_file = files[-1]# последний блок, который находится в папке chain
	file_name = str(prev_file + 1)# называем след.файл символьным значением
	prev_hash = get_hash(str(prev_file))# олучаем хэш предыдущего файла

	block = {'index': int(file_name),
			'timestamp': time() ,
			 'sender' : sender,
			 'amount' : amount,
			 'message' : message,
			 'recipient' : recipient,
			 'hash': prev_hash}

	with open(chain_dir + file_name, 'w') as file:
		json.dump(block, file, indent=4, ensure_ascii=False)

def main():
	sender = input()
	amount = int(input())
	message = input()
	recipient = input()
	write_block(sender, amount, message, recipient)
	check_integrity()


if __name__ == '__main__':
	main()