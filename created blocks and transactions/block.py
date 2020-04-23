import json
import os
import hashlib

blockchain_dir = os.curdir + '/blockchain/'#получаем список всех файлов

def get_hash(file_name):#вычисляем хэш предыдущего файла
	file = open(blockchain_dir + file_name,'rb').read()#указываем имя файла, который мы открываем для чтения с указанием папки
	return hashlib.sha256(file).hexdigest()

def get_files():
	files = os.listdir(blockchain_dir)#получили список всех файлов, хранящихся в папке blockchain
	return sorted([int(i) for i in files])# сортируем названия файлов в порядке возрастания, как целочисленные значения
def write_block(name,amount,to_whom,prev_hash=''):
	files = get_files()
	prev_file = files[-1]#последний блок, который находится в папке blockchain
	file_name = str(prev_file + 1)#называем след.файл символьным значением
	prev_hash = get_hash(str(prev_file))#получаем хэш предыдущего файла

	#print(file_name)

	data = { 'name' : name,
			 'amount' : amount,
			 'to whom' : to_whom,
			 'hash': prev_hash}

	with open(blockchain_dir + file_name,'w') as file:
		json.dump(data, file, indent=4, ensure_ascii=False)

def main():
	name = input()
	amount = int(input())
	to_whom = input()
	write_block(name, amount, to_whom)


if __name__ == '__main__':
	main()