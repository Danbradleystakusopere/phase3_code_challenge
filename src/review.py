

class Review:
    def __init__(self, reader, book, rating, comment=""):
        self.reader = reader
        self.book = book
        self.rating = rating
        self.comment = comment

        
        reader._reviews.append(self)
        book._reviews.append(self)

    def __repr__(self):
        return f"<Review {self.rating}/5 by {self.reader.name} on '{self.book.title}'>"
