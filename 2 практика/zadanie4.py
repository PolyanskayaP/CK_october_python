import random 

mag1 = set() 
mag2 = set()

tov = ['рыба', 'мясо', 'сталь', 'игрушки', 'молоко', \
    'шоколад', 'ёжик', 'пирожок', 'йогурт', 'сметана', \
        'котлета', 'хлеб', 'кофе', 'автобус', 'телефон']

n1 = int(input("сколько товаров на первом заводе? "))
n2 = int(input("сколько товаров на первом заводе? "))


l = list(range(0, len(tov)))
random.shuffle(l)
for i in range(n1):
    mag1.add(tov[i])  

l = list(range(0, len(tov)))
random.shuffle(l)
for i in range(n2):
    mag2.add(tov[i])  

print("первый завод ", mag1)
print("второй завод ", mag2) 

for w in mag1:
    mag2.discard(w)
print("----------------")
print("первый завод ", mag1)
print("второй завод ", mag2) 
