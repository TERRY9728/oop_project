from library_objects import *
from database_control import *

if __name__ == "__main__":
    DATABASE_CONN = Database("library.db")
    READER = Reader(DATABASE_CONN)
    BOOK = Book(DATABASE_CONN)
    LIBRARIAN = Librarian(DATABASE_CONN)

    READER.login(10000000)
    print("reader logged in")
    print(f"Reader ID: {READER.id_num}, Name: {READER.name}, Borrowed Books: {READER.borrowed_book}")

    print("-" * 50)

    print("borrow book: ")
    book_id = 20000000
    if BOOK.is_exist(book_id):
        BOOK.load_by_id(book_id)
        if BOOK.stock > 0:
            READER.borrow_book(book_id)
            BOOK.reduce_stock()
            print("borrow successfully")
    print(f"Title: {BOOK.title}, Author: {BOOK.author}, Stock: {BOOK.stock}")
    print(f"Reader ID: {READER.id_num}, Name: {READER.name}, Borrowed Books: {READER.borrowed_book}")

    print("-" * 50)

    print("return book: ")
    book_id = 20000000
    if BOOK.is_exist(book_id):
        BOOK.load_by_id(book_id)
        READER.return_book(book_id)
        BOOK.add_stock()
        print("return successfully")
    print(f"Title: {BOOK.title}, Author: {BOOK.author}, Stock: {BOOK.stock}")
    print(f"Reader ID: {READER.id_num}, Name: {READER.name}, Borrowed Books: {READER.borrowed_book}")
