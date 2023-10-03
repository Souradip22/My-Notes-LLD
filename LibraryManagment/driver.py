

# Usage
from time import ctime
from checkout import Checkout
from models.book import Book
from models.library import Library
from models.patron import Patron


library = Library()
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")
patron1 = Patron("John Smith", "123")
patron2 = Patron("Jane Doe", "456")
checkout = Checkout()

# Add books to the library
library.add_book(book1)
library.add_book(book2)

# Display all books in the library
library.display_books()

# Check out a book
checkout.check_out(book1, patron1)

# Check out a book
checkout.check_out(book2, patron2)

# Get the due date of the checked out book
due_date = checkout.get_due_date(book1)
if due_date != -1:
    print("Due Date:", ctime(due_date))

# Calculate and display the fine for the overdue book
fine = checkout.calculate_fine(book1)
if fine > 0:
    print("Fine for overdue book: Rs", fine)

# Display all current checkouts
checkout.display_checkouts()

# Return a book
checkout.return_book(book1)

# Display all current checkouts
checkout.display_checkouts()