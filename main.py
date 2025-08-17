# main.py

from src.author import Author

def run_demo():
    # create an author
    author = Author("George Orwell")

    # author writes books
    book1 = author.write_book("1984")
    book2 = author.write_book("Animal Farm")

    # show author's books
    print("Author:", author)
    print("Books:", author.books)

if __name__ == "__main__":
    run_demo()
