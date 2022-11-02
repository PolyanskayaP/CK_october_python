class Nikola:
    __slots__ = ('name', 'age')
    def __init__(self, name, age):
        if name != "Николай":
            self.name = f"Я не {name}, а Николай"
        else:
            self.name = name
        self.age = age
     
n = Nikola('Николай', 20)
print(n.name, n.age)

m = Nikola('Макс', 28)
print(m.name, m.age)

#m.otch = 'Иванович'