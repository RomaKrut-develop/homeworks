class Animal:
    def __init__(self, animal_name, animal_type):
        self.animal_name = animal_name
        self.animal_type = animal_type

    def make_sound(self):
        print(f"*{self.animal_name} noise*")

    def get_info(self):
        return f'Name: {self.animal_name}, Type: {self.animal_type}'


class Bird(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "Flying")


class Mammal(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "Mammal")


class ZooEmployee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def feed(self):
        print(f'{self.name} is feeding the animal')


class Visitor:
    def __init__(self, visitor_name, ticket_number):
        self.visitor_name = visitor_name
        self.ticket_number = ticket_number

    def watch_animal(self):
        print(f'Visitor with name: {self.visitor_name} enjoying animals!')


# Создание экземпляров
hamster = Mammal('Hamster')
red_cardinal = Bird('Red Cardinal')

bob = ZooEmployee('Bob', 'Keeper')
mike_the_visitor = Visitor('Mike', 2024)

# Вывод информации
print(hamster.get_info())
print(red_cardinal.get_info())
mike_the_visitor.watch_animal()