#словарь из словарей
d = {}
#d = {'dict': 1, 'dictionary': 2}

i = input('введите фио работника или стоп! ')
while i != 'стоп!':
    voz = int(input('возраст '))
    dol = input('введите должность ')
    nom = int(input('номер рабочего места '))
    gt = int(input('доступ к г.тайне 1-да 0-нет '))
    d[i] = {'возраст:': voz, 'должность': dol, '№ рабочего места': nom, 'доступ к гос.тайне': gt}
    i = input('введите фио работника или стоп! ')

print(d) 
for key in d:
    print(key, ":")
    q = d[key]
    for key in q:
        print("    ", key, ": " ,q[key])
    