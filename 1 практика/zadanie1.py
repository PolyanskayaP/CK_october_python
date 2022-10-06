a = int(input("введите число "))
z = input("введите один из знаков[+ - * / % ^ sqrt] ")
b = int(input("введите число "))

if (z == "+"):
    print("результат = ", a+b)
elif (z == "-"):
    print("результат = ", a-b)
elif (z == "*"):
    print("результат = ", a*b)
elif (z == "/"):
    print("результат = ", a/b)
elif (z == "%"):
    print("результат = ", a%b)
elif (z == "^"):
    print("результат = ", a**b)
elif (z == "sqrt"):
    print("результат =", a**(1/b))
else:
    print("error")


