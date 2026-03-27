class User:
    def __init__(self, id_num, name):
        self.id_num = id_num
        self.name = name

class Reader(User):
    def __init__(self, database_conn, id_num=None, name=None, borrowed_book=[]):
        super().__init__(id_num, name)
        self.borrowed_book = borrowed_book
        self.database_conn = database_conn

    def initialise(self):
        self.id_num, self.name, self.borrowed_book = (None, None, [])
        return 1

    def borrow_book(self, book_id):
        self.borrowed_book.append(book_id)
        self.update()
        return 1

    def return_book(self, book_id):
        for i in range(len(self.borrowed_book)):
            if book_id == self.borrowed_book[i]:
                returned_book = self.borrowed_book.pop(i)
                self.update()
                return 1
        return 0

    def is_exist(self, id_num):
        return self.database_conn.is_reader_exist(id_num)

    def login(self, id_num):
        if self.is_exist(id_num):
            data = self.database_conn.get_reader(id_num)
            self.id_num, self.name, self.borrowed_book = data
            self.borrowed_book = self.borrowed_book.split(",")
            self.borrowed_book = [int(item) for item in self.borrowed_book if item != ""]
            return 1
        else:
            self.initialise()
            return 0

    def update(self):
        borrowed_book = [str(item) for item in self.borrowed_book]
        borrowed_book = ",".join(borrowed_book)
        self.database_conn.update_reader(self.id_num, self.name, borrowed_book)
        return 1

class Book:
    def __init__(self, database_conn, id_num=None, title=None, author=None, stock=1):
        self.id_num = id_num
        self.title = title
        self.author = author
        self.stock = max(0, stock)
        self.database_conn = database_conn

    def initialise(self):
        self.id_num = self.title = self.author = None
        self.stock = 0
        return 1

    def load_by_id(self, id_num):
        data = self.database_conn.get_book_by_id(id_num)
        self.id_num, self.title, self.author, self.stock = data
        return 1

    def load_by_title(self, substr):
        book_list = self.database_conn.book_id_title()
        substr = substr.lower()
        print(substr)
        for book in book_list:
            title = book[1].lower()
            print(title)
            if substr in title:
                self.load_by_id(book[0])
                return 1
            else:
                continue
        self.initialise()
        return 0

    def update(self):
        self.database_conn.update_book(self.id_num, self.title, self.author, self.stock)
        return 1

    def add_book(self):
        self.database_conn.add_book(self.title, self.author, self.stock)
        return 1

    def del_book(self, id_num):
        self.database_conn.del_book(id_num)
        return 1

    def is_exist(self, id_num):
        is_exist = self.database_conn.is_book_exist(id_num)
        if is_exist:
            self.load_by_id(id_num)
        else:
            self.initialise()
        return is_exist

    def reduce_stock(self):
        self.stock = max(0, self.stock - 1)
        self.update()
        return 1

    def add_stock(self):
        self.stock += 1
        self.update()
        return 1

class Librarian(User):
    def __init__(self, database_conn, id_num=None, name=None):
        super().__init__(id_num, name)
        self.database_conn = database_conn

    def initialise(self):
        self.id_num = None
        self.name = None
        return 1

    def add_book(self, book_obj):
        self.database_conn.add_book(book_obj.title, book_obj.author, book_obj.stock)
        return 1

    def del_book(self, book_id):
        self.database_conn.del_book(book_id)
        return 1

    def is_exist(self, librarian_id):
        return self.database_conn.is_librarian_exist(librarian_id)

    def login(self, librarian_id):
        if self.is_exist(librarian_id):
            data = self.database_conn.get_librarian(librarian_id)
            self.id_num, self.name = data
            return 1
        else:
            self.initialise()
            return 0

if __name__ == "__main__":
    pass
