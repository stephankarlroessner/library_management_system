class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if not self.available:
            raise ValueError("Book already borrowed")
        self.available = False

    def return_book(self):
        self.available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

class Member:
    MAX_BOOKS = 3

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.MAX_BOOKS:
            raise ValueError("Borrowing limit reached")

        book.borrow()
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book not in self.borrowed_books:
            raise ValueError("Book not borrowed by member")

        book.return_book()
        self.borrowed_books.remove(book)


