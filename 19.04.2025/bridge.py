# Мост

from abc import ABC, abstractmethod # Абстрактность
from colorama import Fore, Style # Для разноцветного принта

class NotificationSender(ABC): # Интерфейс для всех каналов отправки
    @abstractmethod
    def send(self, message): ...

class EmailNotification(NotificationSender):
    def send(self, message):
        return Fore.LIGHTCYAN_EX + f"[email] sending: {message}" + Style.RESET_ALL
    
class SMSNotification(NotificationSender):
    def send(self, message):
        return Fore.LIGHTCYAN_EX + f"[sms] sending: {message}" + Style.RESET_ALL
    
class ViboNotification(NotificationSender):
    def send(self, message):
        return Fore.LIGHTCYAN_EX + f"[vibo] sending: {message}" + Style.RESET_ALL

# Абстракция

class Notification(ABC):
    def __init__(self, sender):
        self.sender = sender
    
    def notify(self, message: str): ...

class AlertNotification(Notification):
    def notify(self, message: str):
        return self.sender.send(message)

# Пользовательский код 

email = EmailNotification()
sms = SMSNotification()
vibo = ViboNotification()

alert = AlertNotification(vibo)
print(alert.notify(Fore.LIGHTRED_EX + "Check device!" + Style.RESET_ALL))

alert = AlertNotification(email)
print(alert.notify(Fore.LIGHTRED_EX + "Система перегружена" + Style.RESET_ALL))

alert = AlertNotification(sms)
print(alert.notify(Fore.LIGHTRED_EX + "Критически низкий заряд батери" + Style.RESET_ALL))