import time

h = int(input("введите часы: "))
m = int(input("введите минуты: "))
s = int(input("введите секунды: "))

all_s = h*60*60 + m*60 + s
tochbud = all_s + int(time.time())
ostalos = tochbud - int(time.time())
while (ostalos >= 0):
    hh = ostalos // 3600
    ostalos = ostalos % 3600
    mm = ostalos // 60
    ss = ostalos % 60
    print("осталось ",hh,":",mm,":",ss)
    time.sleep(1)
    ostalos = tochbud - int(time.time()) 
