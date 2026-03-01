class Reader():
    def __init__(self, id_num, name, borrow_limit=5):
        self.__id_num = id_num
        self.__name = name
        self.__borrow_limit = borrow_limit
        self.__borrowed_books = []

    def borrow_book(self):
        pass

    def return_book(self):
        pass

class Book:
    def __init__(self, title, author, stock=1):
        self.__title = title
        self.__author = author
        self.__stock = max(0, stock)

    def get_title(self):
        pass

    def get_stock(self):
        pass

    def reduce_stock(self):
        pass

    def add_stock(self):
        pass

class SearchStrategy:
    def search(self, books, keyword):
        pass

class SearchByTitle(SearchStrategy):
    def search(self, books, keyword):
        return [book for book in books if keyword in book.get_title()]

class SearchByAuthor(SearchStrategy):
    def search(self, books, keyword):
        return [book for book in books if keyword in book.__author]

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
