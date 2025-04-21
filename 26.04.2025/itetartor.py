from colorama import Fore, Style # Для разноцветного принта 
from abc import ABC, abstractmethod # Абстрактные методы

class Employee: # Класс работника 
    def __init__(self, name, position, departament):
        self.name = name
        self.position = position
        self.departament = departament

    def __repr__(self):
        return f"{self.name} - {self.position} ({self.departament})"

class Departament: # Класс департамента
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_iterator(self):
        return EmployeeIterator(self)
    
class EmployeeIterator: # Класс перебора работников
    def __init__(self, departament):
        self.departament = departament
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.departament.employees):
            employee = self.departament.employees[self.index]
            self.index += 1
            return employee
        else:
            raise StopIteration
        
class Mediator(ABC):
    @abstractmethod
    def send_message(self, from_employee, to_employee, message): ...

class DepartamentMediator(Mediator):
    def send_message(self, from_employee, to_employee, message):
        print(Fore.BLUE + f'Сообщение от {from_employee} для {to_employee}: {message}' + Style.RESET_ALL)

employee1 = Employee("Билл Гейтс", "Системный Администратор", "IT")
employee2 = Employee("Илон Маск", "Пиар-менеджер", "HR")
employee3 = Employee("Гвидо-Ван Россум", "Разработчик", "IT")
employee4 = Employee("Стив Джобс", "Разработчик android приложений", "IT")

it_departament = Departament("IT")
hr_departament = Departament("HR")

it_departament.add_employee(employee1)
it_departament.add_employee(employee3)
it_departament.add_employee(employee4)
hr_departament.add_employee(employee2)

hr_iterator = hr_departament.get_iterator()
it_iterator = it_departament.get_iterator()

for employee in it_iterator:
    print(employee)

for employee in hr_iterator:
    print(employee)

mediator = DepartamentMediator()

mediator.send_message(employee3, employee1, "Привет, у меня полегла система, нужно исправить")
mediator.send_message(employee1, employee3, "Привет, хорошо")
mediator.send_message(employee2, employee4, "Ребята, как будем продвигать проект?")
mediator.send_message(employee3, employee4, "Нужно сделать что-то резонансное!")