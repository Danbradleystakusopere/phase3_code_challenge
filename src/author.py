

class Author:
    def __init__(self, name):
        self.name = name
        self._books = []  

    def write_book(self, title):
        """Create a new Book and associate it with this Author"""
        from src.book import Book  
        book = Book(title, self)
        self._books.append(book)
        return book

    @property
    def books(self):
        return self._books

    def __repr__(self):
        return f"<Author {self.name}>"
