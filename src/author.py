# src/author.py

class Author:
    def __init__(self, name):
        self.name = name
        self._books = []  # keeps track of books written by this author

    def write_book(self, title):
        """Create a new Book and associate it with this Author"""
        from src.book import Book  # local import to avoid circular import
        book = Book(title, self)
        self._books.append(book)
        return book

    @property
    def books(self):
        return self._books

    def __repr__(self):
        return f"<Author {self.name}>"
