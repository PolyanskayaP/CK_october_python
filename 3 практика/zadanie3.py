#выводящую содержимое файла в консоль
#Если файла нет то выводится сообщение “Файла нет” 
#name_file = 'z2.txt' 

name_file = input('введите имя файла: ')

try:
    with open(name_file,'r') as f: 
        for line in f:
            print(line) 
except FileNotFoundError:
    print('Файла нет')    