class User: # Класс, представляющий пользователя, с возможностью проверки прав доступа
    def __init__(self, user_id, user_type) -> None:
        self.user_id = user_id
        self.user_type = user_type
    
    def has_permission(self, permission): # Метод для проверки прав доступа
        return self.user_type in permission

class BookFlyweight: # Легковес, который оптимизирует хранение информации о книгах
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author
        self.issued = False # Флаг, показывающий, выдана ли книга
    
    def is_issued(self): # Метод для проверки, выдана ли книга
        return self.issued
    
    def issue(self): # Метод, для выдачи книги
        self.issued = True
    
    def return_book(self):  # Метод, для возврата книги
        self.issued = False

class BookProxy:
    def __init__(self, books) -> None:
        self.books = books
    # Метод для добавление книги в систему
    def add_book(self, book_id, title, author):
        if book_id not in self.books: # Проверяем, если книги нет в систее
            self.books[book_id] = BookFlyweight(title, author)
    # Метод для проверки доступности книги
    def check_availability(self, book_id):
        return book_id in self.books and not self.books[book_id].is_issued()
    # Метод для выдачи книги пользователю
    def issue_book(self, book_id, user_id):
        if self.check_availability(book_id):
            print(f"Книга {book_id} выдана пользователю {user_id}")
        else:
            print(f"Книга {book_id} она недоступна")

    def return_book(self, book_id, user_id):
        print(f"Книга {book_id} была возвращена пользователю {user_id}")

class LibraryFacade:
    def __init__(self) -> None:
        self.users = {}
        self.books = {}
        self.book_proxy = BookProxy(self.books)
    
    def add_book(self, book_id, title, author):
        self.book_proxy.add_book(book_id, title, author)
    
    def issue_book(self, book_id, user_id):
        self.book_proxy.issue_book(book_id,  user_id)
    
    def return_book(self, book_id, user_id):
        self.book_proxy.return_book(book_id,  user_id)

    def check_book_availability(self, book_id):
        return self.book_proxy.check_availability(book_id)

library = LibraryFacade()

library.add_book(1, "Book Title 1", "Author A")
library.add_book(2, "Book Title 2", "Author B")

user1 = User(1, "Reader")
user2 = User(2, "Librarian")

print(library.check_book_availability(1))

library.issue_book(1, user1.user_id)

library.return_book(1, user1.user_id)