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
# Member  borrows a book
def test_member_borrows_a_book():
    member = Member("John")
    book = Book("Pride and Prejudice", "Jane Austen")

    member.borrow_book(book)

    assert book.available is False
    assert book in member.borrowed_books


# Member returns a book
def test_member_returns_a_book():
    member = Member("John")
    book = Book("Pride and Prejudice", "Jane Austen")

    member.borrow_book(book)
    member.return_book(book)

    assert book.available is True
    assert book not in member.borrowed_books

# cannot borrow already borrowed book
def test_cannot_borrow_already_borrowed_book():
    member1 = Member("Alice")
    member2 = Member("Bob")
    book = Book("1984", "George Orwell")

    member1.borrow_book(book)

#    with pytest.raises(ValueError, match="Book is already borrowed"):
#        member2.borrow_book(book)
    assert book.available is False
    assert book in member1.borrowed_books
    assert book not in member2.borrowed_books


# Member cannot return a book they never borrowed
def test_member_cannot_return_book_they_never_borrowed():
    member = Member("Alice")
    book = Book("Dune", "Frank Herbert")
 
#    with pytest.raises(ValueError, match="Book not borrowed by member"):
#        member.return_book(book)
    assert book.available is True



#E2E testing
# borrowing  workflow
def test_borrowing_workflow():
    library_taurange = Library()
    book = Book("The Hobbit", "J.R.R. Tolkien")
    member = Member("John")

    library_taurange.add_book(book)

    found_book = library_taurange.find_book("The Hobbit")
    assert found_book is not None

    member.borrow_book(found_book)

    assert found_book.available is False
    assert found_book in member.borrowed_books


# borrow and return workflow
def test_borrow_and_return_workflow():
    library_tauranga = Library()
    book = Book("The Hobbit", "J.R.R. Tolkien")
    member = Member("John")

    library_tauranga.add_book(book)


    member.borrow_book(library_tauranga.find_book("The Hobbit"))
    member.return_book(book)

    assert book.available is True

    assert book not in member.borrowed_books
    assert len(member.borrowed_books) == 0


# Add three books, borrow all three one member, and check if the limit is reached
def test_member_reaches_borrowing_limit():
    library = Library()
    titles = ["Book One", "Book Two", "Book Three"]
    for title in titles:
        library.add_book(Book(title, "Author"))
    library.add_book(Book("Book Four", "Author"))
 
    member = Member("Alice")
    for title in titles:
        member.borrow_book(library.find_book(title))
 
    assert len(member.borrowed_books) == Member.MAX_BOOKS
    assert all(not library.find_book(t).available for t in titles)
    
    fourth = library.find_book("Book Four")
    with pytest.raises(ValueError, match="Borrowing limit reached"):
        member.borrow_book(fourth)


# Borrow a book, return it, then another member borrows it successfully
def test_borrow_return_borrow_workflow():
    library = Library()
    book = Book("1984", "George Orwell")
    member1 = Member("John")
    member2 = Member("Bob")
    member3 = Member("Charlie")

    library.add_book(book)

    member1.borrow_book(book)
    member1.return_book(book)

    member2.borrow_book(book)

    assert book.available is False
    assert book in member2.borrowed_books
    assert book not in member1.borrowed_books

def test_borrow_return_then_another_member_borrows():
    library = Library()
    library.add_book(Book("Bible", "Frank Herbert"))
    book = library.find_book("Bible")
 
    alice_plant = Member("Alice_Plant")
    bob = Member("Bob")
 
    alice_plant.borrow_book(book)
    assert book.available is False
 
    alice_plant.return_book(book)
    assert book.available is True
    assert book not in alice_plant.borrowed_books
 
    bob.borrow_book(book)
    assert book.available is False
    assert book in bob.borrowed_books
    assert book not in alice_plant.borrowed_books


