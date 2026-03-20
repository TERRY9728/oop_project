from search_strategy import *

class Reader():
    def __init__(self, id_num, name, borrow_limit=5):
        self.id_num = id_num
        self.name = name
        self.borrow_limit = borrow_limit
        self.borrowed_book = []

    def borrow_book(self, book):
        num_of_borrowed = len(self.borrowed_books)
        if num_of_borrowed < self.borrow_limit:
            self.borrowed_book.append(book)
            print("loan succeed")
        else:
            print("loan failed")

    def return_book(self, book):
       pass 

class Book:
    def __init__(self, title, author, stock=1):
        self.title = title
        self.author = author
        self.stock = max(0, stock)

    def get_title(self):
        pass

    def get_stock(self):
        pass

    def reduce_stock(self):
        pass

    def add_stock(self):
        pass

class LibraryManager:
    def __init__(self):
        self.__books = []
        self.__readers = []

    def add_book(self, book):
        self.__books.append(book)

    def add_reader(self, reader):
        self.__readers.append(reader)

    def search_books(self, keyword, strategy):
        return strategy.search(self.__books, keyword)

if __name__ == "__main__":
    pass
