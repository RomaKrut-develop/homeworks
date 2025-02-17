class Car:
    def __init__(self, brand, year, model, color):
        self.brand = brand
        self.year = year
        self.model = model
        self.color = color
    
    def display_info(self):
        return f"Brand: {self.brand}, Model: ({self.model}), Year: {self.year}, Color: {self.color}"
    
car1 = Car("Toytoa", "Camry", 2020, "Black")
car2 = Car("BMW", "X5", 2019, "Yellow")
car3 = Car("Ibishu", "Pigeon", 1980, "Green")

print(car1.display_info())
print(car2.display_info())
print(car3.display_info())