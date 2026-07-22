class LibraryBook:
    def __init__(self, book_name, author, available=True):
        self.book_name = book_name
        self.author = author
        self.available = available

    def show_status(self):
        print("\n===== Library Book =====")
        print("Book Name:", self.book_name)
        print("Author:", self.author)
        if self.available:
            print("Status: Available")
        else:
            print("Status: Borrowed")

    def borrow_book(self):
        if self.available:
            self.available = False
            print("\nBook Borrowed Successfully!")
        else:
            print("\nBook is Already Borrowed.")

    def return_book(self):
        if not self.available:
            self.available = True
            print("\nBook Returned Successfully!")
        else:
            print("\nBook is Already Available.")


book_name = input("Enter Book Name: ")
author = input("Enter Author Name: ")

book1 = LibraryBook(book_name, author)

book1.show_status()
book1.borrow_book()
book1.show_status()
book1.return_book()
book1.show_status()