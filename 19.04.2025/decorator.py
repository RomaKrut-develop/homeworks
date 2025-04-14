# Декоратор 

from colorama import Fore, Style # Для разноцветного принта
from abc import ABC, abstractmethod # Абстрактность
from bridge import *

class BaseNotification(ABC):
    @abstractmethod
    def notify(self, message) -> str: ...

# Простое уведомление
class SimpleNotification(BaseNotification):
    def __init__(self, sender: NotificationSender) -> None:
        self.sender = sender

    def notify(self, message):
        return self.sender.send(message)


class UrgentNotification(BaseNotification):
    def __init__(self, wrapped: BaseNotification) -> None:
        self.wrapped = wrapped

    def notify(self, message):
        return "[URGENT]" + " " + self.wrapped.notify(message)

# Пользовательский код 

email = EmailNotification()
simple = SimpleNotification(email)

urgent = UrgentNotification(simple)
urgent.notify(Fore.LIGHTRED_EX + "Server has been crashed" + Style.RESET_ALL)