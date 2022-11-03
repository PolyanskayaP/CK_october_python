class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    @property   #этот декоратор прописывается именно перет "геттером"
    def kg(self): #методы геттера и сеттера должны одинаково называться 
        return self.__kg
    
    @kg.setter 
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')
        
    #без использования декораторов:     
    #kg = property(get_kg, set_kg) 
    #или:
    #kg = property()
    #kg = kg.setter(set_kg)
    #kg = kg.getter(get_kg) 


c = KgToPounds(3)
print(c.to_pounds())

c.kg=10
print(c.to_pounds()) 

print(c.kg)

#Таким образом, свойство kg_prop скрывает приватный экземпляр __name
#property() и свойств-декораторов

#декораторы: https://proproprogs.ru/python_oop/svoystva-property-dekorator-property

'''Функция isinstance() вернет True, если проверяемый объект object является экземпляром указанного класса (классов) или его подкласса (прямого, косвенного или виртуального).'''