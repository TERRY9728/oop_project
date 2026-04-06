import sqlite3

# connect to the database with file name
class Database:
    def __init__(self, file_name):
        # sql queries
        self.statements = {
            "reader_exist": "SELECT EXISTS (SELECT 1 FROM users WHERE id_num = %d);",
            "fetch_reader": "SELECT * FROM users WHERE id_num = %d;",
            "update_reader": "UPDATE users SET name = \"%s\", borrowed_book = \"%s\" WHERE id_num = %d;",
            "book_exist": "SELECT EXISTS (SELECT 1 FROM books WHERE id_num = %d);",
            "fetch_book_by_id": "SELECT * FROM books WHERE id_num = %d;",
            "update_book": "UPDATE books SET title = \"%s\", author = \"%s\", stock = %d WHERE id_num = %d;",
            "book_id_title": "SELECT id_num, title FROM books;",
            "insert_book": "INSERT INTO books(title, author, stock) VALUES(\"%s\", \"%s\", %d);",
            "del_book": "DELETE FROM books WHERE id_num = %d;",
            "librarian_exist": "SELECT EXISTS (SELECT 1 FROM librarians WHERE id_num = % d);",
            "fetch_librarian": "SELECT * FROM librarians WHERE id_num = %d;"
        }
        self.file_name = file_name
        self.cursor = self.connect()

    def connect(self):
        file_path = self.file_name
        with sqlite3.connect(file_path) as self.sqlite_conn:
            cursor = self.sqlite_conn.cursor()
        return cursor

    def is_reader_exist(self, reader_id):
        result = self.cursor.execute(self.statements["reader_exist"] % reader_id)
        result = result.fetchone()
        return result[0]

    # return reader's info
    def get_reader(self, reader_id):
        result = self.cursor.execute(self.statements["fetch_reader"] % reader_id)
        result = result.fetchone()
        return result

    def update_reader(self, reader_id, reader_name, book_list):
        self.cursor.execute(self.statements["update_reader"] % (reader_name, book_list, reader_id))
        self.sqlite_conn.commit()
        return 1

    def is_book_exist(self, book_id):
        result = self.cursor.execute(self.statements["book_exist"] % book_id)
        result = result.fetchone()
        return result[0]

    def get_book_by_id(self, book_id):
        result = self.cursor.execute(self.statements["fetch_book_by_id"] % book_id)
        result = result.fetchone()
        return result

    def update_book(self, book_id, title, author, stock):
        self.cursor.execute(self.statements["update_book"] % (title, author, stock, book_id))
        self.sqlite_conn.commit()
        return 1

    # return book's id and title
    def book_id_title(self):
        result = self.cursor.execute(self.statements["book_id_title"])
        result = result.fetchall()
        return result

    def add_book(self, title, author, stock):
        self.cursor.execute(self.statements["insert_book"] % (title, author, stock))
        self.sqlite_conn.commit()
        return 1

    def del_book(self, book_id):
        self.cursor.execute(self.statements["del_book"] % book_id)
        self.sqlite_conn.commit()
        return 1

    def is_librarian_exist(self, librarian_id):
        result = self.cursor.execute(self.statements["librarian_exist"] % librarian_id)
        result = result.fetchone()
        return result[0]

    def get_librarian(self, librarian_id):
        result = self.cursor.execute(self.statements["fetch_librarian"] % librarian_id)
        result = result.fetchone()
        return result

if __name__ == "__main__":
    database_conn = Database("library.db")
