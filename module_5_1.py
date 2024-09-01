class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.number_of_floors = new_floor
        if h1.number_of_floors > 18 or h1.number_of_floors < 1:
            h1.number_of_floors = 'которого нет'
        elif h2.number_of_floors > 2 or h2.number_of_floors < 1:
            h2.number_of_floors = 'которого нет'
        return h1, h2


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
print(f'Вы в {h1.name}, на этаже {h1.number_of_floors}')
print(f'Вы в {h2.name}, на этаже {h2.number_of_floors}')
