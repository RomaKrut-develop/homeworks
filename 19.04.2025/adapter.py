# Адаптер

# from abc import ABC, abstractmethod # Абстрактность
from bridge import NotificationSender, AlertNotification
from colorama import Fore, Style # Для разноцветного принта

class PushNotification: # Несовместмый класс с NotificationSender
    def push(self, content: str):
        return Fore.LIGHTCYAN_EX + f"[push] sending: {content}" + Style.RESET_ALL

class PushNotificationAdapter(NotificationSender):
    def __init__(self, adaptee: PushNotification):
        self.adaptee = adaptee

    def send(self, message):
        return self.adaptee.push(message)
    
# Пользовательский код
 
push = PushNotification()
adapter = PushNotificationAdapter(push)

alert = AlertNotification(adapter)
print(alert.notify(Fore.LIGHTGREEN_EX + "Новинка!" + Style.RESET_ALL))