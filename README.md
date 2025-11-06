# library-management-system
A comprehensive Python-based Library Management System with features for managing books, members, and transactions

## Features

- **Book Management**: Add, view, and manage library books
- **Member Management**: Register and manage library members
- **Borrow/Return System**: Track book borrowing and returns
- **Transaction History**: Maintain complete record of all transactions
- **Data Persistence**: All data is saved to JSON file for persistence
- **User-Friendly Interface**: Simple command-line menu system

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ajayghanta5/library-management-system.git
```

2. Navigate to the project directory:
```bash
cd library-management-system
```

3. Run the application:
```bash
python library_management.py
```

## Usage

The system provides an interactive menu with the following options:

1. **Add Book** - Add new books to the library
2. **Add Member** - Register new library members
3. **Borrow Book** - Allow members to borrow books
4. **Return Book** - Process book returns
5. **Display Books** - View all books in the library
6. **Display Members** - View all registered members
7. **Exit** - Exit the application

## Project Structure

- `library_management.py` - Main application file containing all classes and functions
- `library_data.json` - Data storage file (created automatically)
- `.gitignore` - Git ignore file for Python projects
- `README.md` - Project documentation

## Classes

### Book
Represents a book in the library with attributes:
- book_id
- title
- author
- isbn
- quantity
- available

### Member
Represents a library member with attributes:
- member_id
- name
- email
- phone
- borrowed_books

### Transaction
Records borrowing/returning activities with:
- transaction_id
- member_id
- book_id
- transaction_type
- date

### LibraryManagementSystem
Main system class that handles all operations

## Requirements

- Python 3.x
- No external dependencies required

## Author

**Ajay Ghanta**

## License

This project is open source and available for educational purposes.
