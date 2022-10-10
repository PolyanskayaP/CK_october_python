'''Задание 3 Отлично, фразы получаются, но иногда руководитель пишет и свои 
речи и допускает ошибки. Нужно чтобы программа проверяла правильно ли написаны 
слова. Вводятся “правильные” слова которыми будет проверятся, после чего 
вводится предложение слова из которого проверяются. после выводятся слова 
с ошибками(ошибка отделяется пробелом справа и слева от буквы). ПОДСКАЗКА 
нужно проверять на минимальное отличие от “эталонного” слова. 
'''
from socket import ALG_SET_AEAD_ASSOCLEN
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

print("стоп-слово: стоп!")
prav = list()

s = input("введите правильное слово: ")

while s != "стоп!":
    prav.append(s)
    s = input("введите правильное слово: ")

fraza = input("введите предложение: ")
sp_fraza = fraza.split(' ') 
qq = ''

for sl in sp_fraza:
    a = process.extractOne(sl, prav) 
    if a[1]!=100:
        pr_sl = a[0]
        ch_pr_sl = [c for c in pr_sl]
        ch_sl = [c for c in sl]
        len_ch_pr_sl = len(ch_pr_sl)
        len_ch_sl = len(ch_sl) 
        if len_ch_pr_sl == len_ch_sl:
            for i in range(0, len_ch_sl):
                if ch_pr_sl[i] == ch_sl[i]:
                    qq += ch_pr_sl[i]
                else:
                    qq = ' ' + ch_sl[i] + ' ' 
            if qq != '':
                print(qq)
                qq = ''
        else:
            print('')

#for i in range
 #   a = process.extractOne(, prav)

#city = ["Москва", "Санкт-Петербург", "Саратов", "Краснодар", "Воронеж", "Омск", "Екатеринбург", "Орск", "Красногорск", "Красноярск", "Самара"]
#a = process.extractOne("Краногрск", city)
#print(a[0])

#pip install fuzzywuzzy
#pip install python-Levenshtein