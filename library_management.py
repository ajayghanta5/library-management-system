import json
import os
from datetime import datetime

class Book:
    def __init__(self, book_id, title, author, isbn, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity = quantity
        self.available = quantity

    def to_dict(self):
        return {
            'book_id': self.book_id,
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'quantity': self.quantity,
            'available': self.available
        }

class Member:
    def __init__(self, member_id, name, email, phone):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone
        self.borrowed_books = []

    def to_dict(self):
        return {
            'member_id': self.member_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'borrowed_books': self.borrowed_books
        }

class Transaction:
    def __init__(self, transaction_id, member_id, book_id, transaction_type, date):
        self.transaction_id = transaction_id
        self.member_id = member_id
        self.book_id = book_id
        self.transaction_type = transaction_type
        self.date = date

    def to_dict(self):
        return {
            'transaction_id': self.transaction_id,
            'member_id': self.member_id,
            'book_id': self.book_id,
            'transaction_type': self.transaction_type,
            'date': self.date
        }

class LibraryManagementSystem:
    def __init__(self):
        self.books = []
        self.members = []
        self.transactions = []
        self.load_data()

    def load_data(self):
        try:
            if os.path.exists('library_data.json'):
                with open('library_data.json', 'r') as f:
                    data = json.load(f)
                    self.books = [Book(**book) for book in data.get('books', [])]
                    self.members = [Member(**member) for member in data.get('members', [])]
                    self.transactions = [Transaction(**trans) for trans in data.get('transactions', [])]
        except Exception as e:
            print(f"Error loading data: {e}")

    def save_data(self):
        try:
            data = {
                'books': [book.to_dict() for book in self.books],
                'members': [member.to_dict() for member in self.members],
                'transactions': [trans.to_dict() for trans in self.transactions]
            }
            with open('library_data.json', 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")

    def add_book(self, title, author, isbn, quantity):
        book_id = len(self.books) + 1
        book = Book(book_id, title, author, isbn, quantity)
        self.books.append(book)
        self.save_data()
        print(f"Book '{title}' added successfully!")

    def add_member(self, name, email, phone):
        member_id = len(self.members) + 1
        member = Member(member_id, name, email, phone)
        self.members.append(member)
        self.save_data()
        print(f"Member '{name}' added successfully!")

    def borrow_book(self, member_id, book_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.book_id == book_id), None)

        if not member:
            print("Member not found!")
            return
        if not book:
            print("Book not found!")
            return
        if book.available <= 0:
            print("Book not available!")
            return

        book.available -= 1
        member.borrowed_books.append(book_id)
        transaction_id = len(self.transactions) + 1
        transaction = Transaction(transaction_id, member_id, book_id, 'borrow', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        self.transactions.append(transaction)
        self.save_data()
        print(f"Book '{book.title}' borrowed by {member.name}")

    def return_book(self, member_id, book_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.book_id == book_id), None)

        if not member:
            print("Member not found!")
            return
        if not book:
            print("Book not found!")
            return
        if book_id not in member.borrowed_books:
            print("This book was not borrowed by this member!")
            return

        book.available += 1
        member.borrowed_books.remove(book_id)
        transaction_id = len(self.transactions) + 1
        transaction = Transaction(transaction_id, member_id, book_id, 'return', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        self.transactions.append(transaction)
        self.save_data()
        print(f"Book '{book.title}' returned by {member.name}")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("\n--- Library Books ---")
        for book in self.books:
            print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Available: {book.available}/{book.quantity}")

    def display_members(self):
        if not self.members:
            print("No members registered.")
            return
        print("\n--- Library Members ---")
        for member in self.members:
            print(f"ID: {member.member_id}, Name: {member.name}, Email: {member.email}, Phone: {member.phone}, Borrowed: {len(member.borrowed_books)}")

def main():
    lms = LibraryManagementSystem()
    
    while True:
        print("\n=== Library Management System ===")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Display Books")
        print("6. Display Members")
        print("7. Exit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            quantity = int(input("Enter quantity: "))
            lms.add_book(title, author, isbn, quantity)
        
        elif choice == '2':
            name = input("Enter member name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            lms.add_member(name, email, phone)
        
        elif choice == '3':
            lms.display_members()
            lms.display_books()
            member_id = int(input("Enter member ID: "))
            book_id = int(input("Enter book ID: "))
            lms.borrow_book(member_id, book_id)
        
        elif choice == '4':
            lms.display_members()
            member_id = int(input("Enter member ID: "))
            book_id = int(input("Enter book ID: "))
            lms.return_book(member_id, book_id)
        
        elif choice == '5':
            lms.display_books()
        
        elif choice == '6':
            lms.display_members()
        
        elif choice == '7':
            print("Thank you for using Library Management System!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
