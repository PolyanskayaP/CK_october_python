from random import randint 

def del_ch():
    try:
        k = randint(0,1)  
        k = 10 / k 
        return(k)
    except:
        return 'деление на 0'

print(del_ch())