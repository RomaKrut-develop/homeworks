# Паттерн-фасад c легковесом и заместителем 
from colorama import Fore, Style # Разноцветный принт

class User:
    def __init__(self, user_id, user_type):
        self.user_id = user_id
        self.user_type = user_type

    def has_permission(self, permission): # Полномочия
        return self.user_type in permission
    
class BookFlyWeight: # Легковес, опитизирует хранение информации о книгах
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.issued = False # флажок который показывает, выдана ли книга

    def is_issued(self): # для проверки наличия книги
        return self.issued
    
    def issue(self): # для самой выдачи книги
        self.issued = True

    def return_book(self): # для возврата книги
        self.issued = False

class BookProxy:
    def __init__(self, books):
        self.books = books
    
    def add_book(self, book_id, title, author):
        if book_id not in self.books:
            self.books[book_id] = BookFlyWeight(title, author)

    def check_availability(self, book_id):
        return book_id in self.books and not self.books[book_id].is_issued()

    def issue_book(self, book_id, user_id):
        if self.check_availability(book_id):
            print(Fore.GREEN + f"Book {book_id} has been gived to user_{user_id}" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Book {book_id} not allowed")
    
    def return_book(self, book_id, user_id):
        print(Fore.YELLOW + f"Book {book_id} has been returned to user_{user_id}" + Style.RESET_ALL)

class LibraryFacade:
    def __init__(self):
        self.users = {}
        self.books = {}
        self.book_proxy = BookProxy(self.books)

    def add_book(self, book_id, title, author):
        self.book_proxy.add_book(book_id, title, author)
     
    def issue_book(self, book_id, user_id):
        self.book_proxy.issue_book(book_id, user_id)

    def return_book(self, book_id, user_id):
        self.book_proxy.return_book(book_id, user_id)

    def check_books_availability(self, book_id):
        return self.book_proxy.check_availability(book_id)
        
# Пользовательский код

lbr = LibraryFacade()

lbr.add_book(1, "bestBookInTheWorld", "Johan Smith")
lbr.add_book(2, "Tisseract", "Max Payne")

user1 = User(1, "Reader")
user2 = User(2, "Librarian")

print(lbr.check_books_availability(1))

lbr.issue_book(1, user1.user_id)

lbr.return_book(1, user1.user_id)