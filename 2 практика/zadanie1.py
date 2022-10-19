from random import randint

def gen_cif_int(skok, xn, xk):
    spis = []
    for i in range(skok):
        spis.append(randint(xn, xk))
    return spis  

otrasli = {0: 'Сельское хозяйство', 1: 'Легкая промышленность', \
    2: 'Тяжелая промышленность группы А', 3: 'Тяжелая промышленность группы Б', \
4: 'Военно промышленный комплекс', 5: 'Наука', 6: 'Химическая промышленность' }
kolv_otr = len(otrasli)  
rep = {} 
#rep {'Qqq', }

n = int(input('введите количество союзных республик: '))
for i in range(n):
    a = input("название союзной республики: ")
    rep[a] = gen_cif_int(kolv_otr, -1, 1) 

z1 = list() 

'''
for key in rep:  #key belar
    #rep[key] получ списка индексов на кажд итер респ 
    ##ind = 0
    print(key, end=' ') 
   # for i in rep[key]:
    for i in range(7):
        ##ind = ind + 1
        print(rep[key][i], end=' ') 
    print(' ')
'''
'''
for key in rep:      #3*7
    for i in range(kolv_otr):
        print(rep[key][i], end=' ')
    print(' ')  
'''

for i in range(kolv_otr):   #7*3 
    for key in rep:
        print(rep[key][i], end=' ')  
    print(' ')  




 
#print(rep)