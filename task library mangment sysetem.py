#task on library mangement system
# Library Management System

library = {}
issued_books = {}

def add_book():
    book_id = input("Enter Book ID: ")
    book_name = input("Enter Book Name: ")
    
    if book_id in library:
        print("Book ID already exists!\n")
    else:
        library[book_id] = book_name
        print("Book added successfully!\n")

def search_book():
    book_id = input("Enter Book ID to search: ")
    
    if book_id in library:
        print("Book Found:", library[book_id], "\n")
    elif book_id in issued_books:
        print("Book is currently issued.\n")
    else:
        print("Book not found.\n")

def view_books():
    if not library:
        print("No books available.\n")
    else:
        print("Available Books:")
        for book_id, book_name in library.items():
            print(book_id, "-", book_name)
        print()

def issue_book():
    book_id = input("Enter Book ID to issue: ")
    
    if book_id in library:
        issued_books[book_id] = library[book_id]
        del library[book_id]
        print("Book issued successfully!\n")
    else:
        print("Book not available.\n")

def return_book():
    book_id = input("Enter Book ID to return: ")
    
    if book_id in issued_books:
        library[book_id] = issued_books[book_id]
        del issued_books[book_id]
        print("Book returned successfully!\n")
    else:
        print("This book was not issued.\n")

while True:
    print("------ Library Management System ------")
    print("1. Add Book")
    print("2. Search Book")
    print("3. View Books")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        view_books()
    elif choice == "4":
        issue_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        print("Thank you for using Library System!")
        break
    else:
        print("Invalid choice!\n")
