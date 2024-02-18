#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Library:
    def __init__(self):
        self.file_name = "books.txt"
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        if not books:
            print("No books in the library.")
        else:
            print("\n*** LIST OF BOOKS ***")
            for book in books:
                title, author, release_date, num_pages = book.split(',')
                print(f"Title: {title}, Author: {author}")

    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the author: ")
        release_date = input("Enter the release date: ")
        num_pages = input("Enter the number of pages: ")

        book_info = f"{title},{author},{release_date},{num_pages}\n"
        self.file.write(book_info)
        print(f"\n'{title}' by {author} has been added to the library.")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")
        
        self.file.seek(0)
        books = self.file.read().splitlines()
        
        updated_books = [book for book in books if title_to_remove not in book.split(',')[0]]

        if len(updated_books) == len(books):
            print(f"\nNo book with the title '{title_to_remove}' found in the library.")
        else:
            self.file.truncate(0)
            self.file.seek(0)
            for book in updated_books:
                self.file.write(f"{book}\n")

            print(f"\n'{title_to_remove}' has been removed from the library.")


# Create Library object
lib = Library()

# Menu
while True:
    print("\n*** LIBRARY MANAGEMENT SYSTEM ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == '4':
        print("Exiting the Library Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")








# In[ ]:




