

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author   
        self._reviews = []     

    def add_review(self, reader, rating, comment):
        """Create a new Review and associate it with this Book"""
        from src.review import Review
        review = Review(reader, self, rating, comment)
        self._reviews.append(review)
        return review

    @property
    def reviews(self):
        return self._reviews

    def average_rating(self):
        """Return average rating or None if no reviews"""
        if not self._reviews:
            return None
        return sum(r.rating for r in self._reviews) / len(self._reviews)

    def __repr__(self):
        return f"<Book '{self.title}' by {self.author.name}>"
