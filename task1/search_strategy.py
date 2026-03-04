class SearchStrategy:
    def search(self, books, keyword):
        pass

class SearchByTitle(SearchStrategy):
    def search(self, books, keyword):
        return [book for book in books if keyword in book.get_title()]

class SearchByAuthor(SearchStrategy):
    def search(self, books, keyword):
        return [book for book in books if keyword in book.author]
