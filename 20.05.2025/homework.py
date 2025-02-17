class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
    
    def get_info(self):
        return f"{self.title} ({self.author}) - {self.year}, ISBN: {self.isbn}"

class Reader:
    def __init__(self, name, reader_id):
        self.name = name
        self.reader_id = reader_id
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
        else:
            print('Данной книги не существует')
    
    def get_borrowed_books(self):
        return [book.title for book in self.borrowed_books]
    
class Library:
    def __init__(self):
        self.books = {}
        self.readers = {}
    
    def add_book(self, book):
        self.books[book.isbn] = book

    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]

    def register_reader(self, reader):
        self.readers[reader.reader_id] = reader
    
    def lend_book(self, isbn, reader_id):
        if isbn in self.books and reader_id in self.readers:
            book = self.books.pop(isbn)
            self.readers[reader_id].borrow_book(book)
            print(f'Книга "{book.title} выдана {self.readers[reader_id].name + "у"}"')
        else:
            print('Не найдена книга или читатель, попробуйте еще раз')
    
    def accept_returned_book(self, isbn, reader_id):
        if reader_id in self.readers:
            reader = self.readers[reader_id]
            for book in reader.borrowed_books:
                if book.isbn == isbn:
                    reader.return_book(book)
                    self.books[isbn] = book
                    print(f'Книга {book.title} возвращена в библиотеку')
                    return
        else:
            print('Книга не найдена у получателя')

library = Library()

book1 = Book('История Microsoft', "Пол Аллен", 2012, "123456")
book2 = Book('', "Ден Мафен", 2003, "654321")

library.add_book(book1)
library.add_book(book2)

reader1 = Reader('Cтив', "u001")
reader2 = Reader('Джон', "u002")

library.register_reader(reader1)
library.register_reader(reader2)

library.lend_book("123456", "u001")

print('Книги у Стива: ', reader1.get_borrowed_books())

library.accept_returned_book("123456", "u001")

books_in_library = [book.get_info() for book in library.books.values()]

print('Доступные книги в библиотеке: ', books_in_library)