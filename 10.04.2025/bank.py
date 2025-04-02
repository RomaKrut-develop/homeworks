from colorama import Fore, Style

class ClientNode:
    def __init__(self, name, account_number, balance):
        self.name = name 
        self.account_number = account_number
        self.balance = balance
        self.prev = None
        self.next = None

class BankClientList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_client(self, name, account_number, balance):
        new_client = ClientNode(name, account_number, balance)
        if not self.head:
            self.head = self.tail = new_client # Становится первым и последним элементом в списке, как змея в змейке в начале игры
        else: 
            self.tail.next = new_client
            new_client.prev = self.tail
            self.tail = new_client

    def remove_client(self, account_number):
        current = self.head

        while current and current.account_number != account_number:
            current = current.next

        if not current:
            return False
        
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next

        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev

        return True
    
    def find_client(self, account_number):
        current = self.head
        while current:
            if current.account_number == account_number:
                return True
            current = current.next
        return False

    def list_clients(self):
        current = self.head
        while current:
            print(f'Name: {current.name}, credit number: {current.account_number}, balance: {current.balance}')
            current = current.next

bank_list = BankClientList()
bank_list.add_client('Elon Musk', "246", 34735)
bank_list.add_client('Bill Gates', "674", 15467)
bank_list.add_client('Christofer', "546", 3467)
bank_list.list_clients()
bank_list.remove_client('246')
bank_list.list_clients()