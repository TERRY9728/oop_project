from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from library_objects import *
from database_control import *

DATABASE_CONN = Database("library.db")
READER = Reader(DATABASE_CONN)
LIBRARIAN = Librarian(DATABASE_CONN)
BOOK = Book(DATABASE_CONN)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content_type", "text/html")
            self.end_headers()
            with open("templates/index.html", "r") as file:
                self.wfile.write(bytes(file.read(), "utf-8"))
            READER.initialise()

        elif self.path == "/reader/base":
            self.send_response(200)
            self.send_header("Content_type", "text/html")
            self.end_headers()
            with open("templates/reader_base.html", "r") as file:
                self.wfile.write(bytes(file.read() % (READER.name, READER.borrowed_book), "utf-8"))

        elif self.path == "/librarian/base":
            self.send_response(200)
            self.send_header("Content_type", "text/html")
            self.end_headers()
            with open("templates/librarian_base.html", "r") as file:
                self.wfile.write(bytes(file.read() % (LIBRARIAN.name), "utf-8"))

        else:
            self.send_error(404)

        return

    def do_POST(self):
        if self.path == "/reader/base":
            parsed_data = self.parse_from_header()
            reader_id = int(parsed_data["reader_id"][0])
            login_state = READER.login(reader_id)
            if login_state:
                self.send_response(200)
                self.send_header("Content_type", "text/html")
                self.end_headers()
                with open("templates/reader_base.html", "r") as file:
                    self.wfile.write(bytes(file.read() % (READER.name, READER.borrowed_book), "utf-8"))
            else:
                self.send_response(200)
                self.send_header("Content_type", "text/javascript")
                self.end_headers()
                self.wfile.write(bytes("<script>alert(\"invalid id\");window.location.href='/';</script>", "utf-8"))

        elif self.path == "/librarian/base":
            parsed_data = self.parse_from_header()
            librarian_id = int(parsed_data["librarian_id"][0])
            login_state = LIBRARIAN.login(librarian_id)
            if login_state:
                self.send_response(200)
                self.send_header("Content_type", "text/html")
                self.end_headers()
                with open("templates/librarian_base.html", "r") as file:
                    self.wfile.write(bytes(file.read() % LIBRARIAN.name, "utf-8"))
            else:
                self.send_response(200)
                self.send_header("Content_type", "text/javascript")
                self.end_headers()
                self.wfile.write(bytes("<script>alert(\"invalid id\");window.location.href='/';</script>", "utf-8"))

        elif self.path == "/search_by_title":
            parsed_data = self.parse_from_header()
            keyword = parsed_data["keyword"][0]
            BOOK.load_by_title(keyword)
            self.send_response(200)
            self.send_header("Content_type", "text")
            self.end_headers()
            self.wfile.write(bytes(f"ID: {BOOK.id_num}\nTitle: {BOOK.title}\nAuthor: {BOOK.author}\nStock: {BOOK.stock}", "utf-8"))

        elif self.path == "/book/borrow":
            parsed_data = self.parse_from_header()
            book_id = int(parsed_data["book_id"][0])
            self.send_response(200)
            self.send_header("Content_type", "text/javascript")
            self.end_headers()
            if BOOK.is_exist(book_id) and BOOK.stock > 0:
                READER.borrow_book(book_id)
                BOOK.reduce_stock()
                self.wfile.write(bytes("<script>alert(\"borrow successfully\");window.location.href='/reader/base';</script>", "utf-8"))
            else:
                self.wfile.write(bytes("<script>alert(\"borrow failed\");window.location.href='/reader/base';</script>", "utf-8"))

        elif self.path == "/book/return":
            parsed_data = self.parse_from_header()
            book_id = int(parsed_data["book_id"][0])
            self.send_response(200)
            self.send_header("Content_type", "text/javascript")
            self.end_headers()
            if BOOK.is_exist(book_id) and READER.return_book(book_id):
                BOOK.add_stock()
                self.wfile.write(bytes("<script>alert(\"return successfully\");window.location.href='/reader/base';</script>", "utf-8"))
            else:
                self.wfile.write(bytes("<script>alert(\"return failed\");window.location.href='/reader/base';</script>", "utf-8"))

        elif self.path == "/add_book":
            parsed_data = self.parse_from_header()
            BOOK.initialise()
            BOOK.title = parsed_data["title"][0]
            BOOK.author = parsed_data["author"][0]
            BOOK.stock = int(parsed_data["stock"][0])
            BOOK.add_book()
            self.send_response(200)
            self.send_header("Content_type", "text/javascript")
            self.end_headers()
            self.wfile.write(bytes("<script>alert(\"add successfully\");window.location.href='/librarian/base';</script>", "utf-8"))

        elif self.path == "/del_book":
            parsed_data = self.parse_from_header()
            book_id = int(parsed_data["book_id"][0])
            BOOK.del_book(book_id)
            self.send_response(200)
            self.send_header("Content_type", "text/javascript")
            self.end_headers()
            self.wfile.write(bytes("<script>alert(\"delete successfully\");window.location.href='/librarian/base';</script>", "utf-8"))

        else:
            self.send_error(404)

        return

    def parse_from_header(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length).decode()
        parsed_data = parse_qs(post_data)
        return parsed_data

if __name__ == "__main__":
    IP = "127.0.0.1"
    PORT = 8000
    server_address = (IP, PORT)
    server = HTTPServer(server_address, Handler)
    print(f"http://{IP}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print("\nserver closed")
