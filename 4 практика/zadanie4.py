class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    def set_kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')

    def get_kg(self):
        return self.__kg
    kg_prop = property(get_kg, set_kg) 

c = KgToPounds(3)
print(c.to_pounds())

c.kg_prop=10
print(c.to_pounds()) 

print(c.kg_prop)

#Таким образом, свойство kg_prop скрывает приватный экземпляр __name
#property() и свойств-декораторов

'''Функция isinstance() вернет True, если проверяемый объект object является экземпляром указанного класса (классов) или его подкласса (прямого, косвенного или виртуального).'''