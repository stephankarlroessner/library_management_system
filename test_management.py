from management import Book, Library, Member
import pytest

#unit testing
# testing basic functionality

# New book is available
def test_new_book_is_avaialble():
    book = Book("The Great Gatsby", "F. Scott Fitzgerald")
    assert book.available is True

# Borrow changes availabaility
def test_borrow_book():
    book = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book.borrow()
    assert book.available is False

# Return changes availability
def test_return_book():
    book = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book.borrow()
    book.return_book()
    assert book.available is True

# Add book to the Library
def test_add_book_to_library():
    library = Library()
    book = Book("The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book(book)

    assert library.find_book("The Great Gatsby") == book
    assert len(library.books) == 1


#  Searching for missing book returns None
def test_find_missing_book_returns_none():
    library = Library()
    assert library.find_book("Missing Book") is None
 
#  Member starts with zero borrowed books
def test_member_starts_with_zero_borrowed_books():
    member = Member("Alice")
    assert member.borrowed_books == []

#  Searching for missing book returns None
def test_find_missing_book_returns_none():
    library = Library()
    assert library.find_book("Missing Book") is None
 
#  Member starts with zero borrowed books
def test_member_starts_with_zero_borrowed_books():
    member = Member("Alice")
    assert member.borrowed_books == []
 
# Library can store multiple books
def test_library_can_store_multiple_books():
    library = Library()
    library.add_book(Book("Book One", "Author One"))
    library.add_book(Book("Book Two", "Author Two"))
    library.add_book(Book("Book Three", "Author Three"))
    assert len(library.books) == 3
 
#  Borrowing limit is enforced
def test_borrowing_limit_is_enforced():
    member = Member("Alice")
    for i in range(Member.MAX_BOOKS):
        member.borrow_book(Book(f"Book {i}", "Author"))
 
    extra = Book("One Too Many", "Author")
    with pytest.raises(ValueError, match="Borrowing limit reached"):
        member.borrow_book(extra)
    assert extra.available is True
    assert len(member.borrowed_books) == Member.MAX_BOOKS
 

# 1 Cannot borrow already borrowed book.
# 2 Searching for missing book returns None.
# 3 Member starts with zero borrowed books.
# 4 Library can store multiple books.
# 5 Borrowing limit is enforced.

#integration testing






#E2E testing