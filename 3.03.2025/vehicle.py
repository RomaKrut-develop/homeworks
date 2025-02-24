class Vehicle:
    def __init__(self, model, brand, year, distance):
        self.__model = model 
        self.__brand = brand
        self.__year = year
        self.__distance = distance

    def get_info(self):
        return f"{self.__year} {self.__brand} {self.model}"
    
    def get_brand(self): return self.__brand

    def get_model(self): return self.__model

class Car(Vehicle):
    def __init__(self, model, brand, year, distance, type):
        super().__init__(model, brand, year, distance, type)
        self.__type = type # вот как создать доп. атрибут

    def get_info(self):
        return super().get_info() + f", type: {self.type}"

class Truck(Vehicle):
    def __init__(self, model, brand, year, distance, weight_ability):
        super().__init__(model, brand, year, distance, weight_ability)
        self.__weight_ability = weight_ability

    def get_info(self):
        return super().get_info() + f", weight capacity: {self.type}"

class Motorcycle(Vehicle):
    def __init__(self, model, brand, year, distance, engine_capacity):
        super().__init__(model, brand, year, distance, engine_capacity)
        self.engine_capacity = engine_capacity

    def get_info(self):
        return super().get_info() + f", engine capacity: {self.type}"


class Fleet:
    def __init__(self):
        self.__cars = []

    def add_car(self, car):
        self.__cars.append(car)
        print(f'New car!: {self.car}!')

    def list(self):
        for car in self.__cars:
            print(car.get_info())

    def search(self, brand=None, model=None):
        searched_cars = [
            c for c in self.__cars
            if(brand is None or c.get_brand() == brand)
            and (model is None or c.get_brand() == model)
        ]

        return searched_cars
fleet = Fleet() 

truck = Truck("Stambecco", "Autobello", "1971", "1000km", '2T')

Fleet.add_car(truck)

Fleet.show_info()