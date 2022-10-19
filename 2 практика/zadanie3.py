def func(a):
    m = a % 10
    a = a // 10 
    s = m 
    while a >= 10:
        m = a % 10
        a = a // 10
        s = s + m
    s = s + a 
    return s 
    

a = int(input("введите число: "))
print(func(a))
