import os
name_file = 'z2.txt'
f_old = open(name_file,'r')
f_new = open('new.txt', 'a+')

for line in f_old:
    f_new.write(line)

f_old.close()
os.remove(name_file)
f_new.close()