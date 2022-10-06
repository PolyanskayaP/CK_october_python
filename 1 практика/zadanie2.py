from random import randint

print("стоп-слово: стоп!")
sush = list()

s = input("введите существительное: ")

while s != "стоп!":
    sush.append(s)
    s = input("введите существительное: ")

glag = list()

s = input("введите глагол: ")

while s != "стоп!":
    glag.append(s)
    s = input("введите глагол: ")

k = int(input("сколько фраз сгенерировать? "))

len_s = len(sush)
len_g = len(glag)

for i in range(k):
    rand_s1 = randint(0, len_s-1)
    rand_s2 = randint(0, len_s-1)
    rand_g = randint(0, len_g-1) 

    if i % 3 == 0:
        result = glag[rand_g] + " " + sush[rand_s1] + " " + sush[rand_s2]
    elif i % 3 == 1:
        result = sush[rand_s1] + " " + glag[rand_g] + " " + sush[rand_s2]
    elif i % 3 == 2:
        result = sush[rand_s1] + " " + sush[rand_s2] + " " + glag[rand_g] 
    
    print(result) 



