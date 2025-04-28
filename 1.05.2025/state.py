from abc import ABC, abstractmethod
from colorama import Fore, init # Для разноцветного принта
init(autoreset=True) # Автосброс стиля

class Observer(ABC):
    @abstractmethod 
    def update(self, state):...

class Subject(ABC):
    def __init__(self):
        self.__observers = []

    def add_observer(self, observer: Observer):
        self.__observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.__observers.remove(observer)

    def notify_observers(self):
        for observer in self.__observers:
            observer.update(self)

class State(ABC):
    @abstractmethod
    def handle(self, subject): ...

class OnlineState(State):
    def handle(self, subject):
        print(Fore.GREEN + "User Online!")
        subject.notify_observers()

class AwayState(State):
    def handle(self, subject):
        print(Fore.YELLOW + "User Offline")
        subject.notify_observers()

class DoNotDistrubate(State):
    def handle(self, subject):
        print(Fore.RED + "Do not distrub")

class User(Subject):
    def __init__(self):
        super().__init__()
        self.__state = None

    def set_state(self, state: State):
        self.__state = state
        self.__state.handle(self)

class UserObserver(Observer):
    def __init__(self, name: str):
        self.name = name
    
    def update(self, state):
        print(f"{self.name} recived state changes")

user = User()

user.add_observer(UserObserver('John Smith'))
user.add_observer(UserObserver('Bill Gates'))

user.set_state(OnlineState())
user.set_state(AwayState())
user.set_state(DoNotDistrubate())