class Soda():
    def __init__(self, dob:str = None):
        self.dob = dob 
    def  show_my_drink(self):
        if self.dob != None:
            print(f"Газировка и {self.dob}")
        else:
            print("Обычная газировка")

p = input("добавка: ")
g = Soda(p) 
g.show_my_drink()

g2 = Soda()
g2.show_my_drink()


#print(tom.company)  # ! Ошибка - AttributeError: Person object has no attribute company