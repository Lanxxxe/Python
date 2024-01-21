import os
# Dictionary of Books. The variable "Books" contains a key value pair.
Books = {}

def add_Books(id, book_name, book_count):
    # Function to add a book to the library
    Books[id] = {'Book name': book_name, 'Book stock': book_count}
    print(f"Successfully Added the book {book_name}")

    # Pause for user input and return to the main interface function
    input("Please press Enter to continue...")
    return interface

def view_Books():
    # Function to view all available books in the library
    if Books:
        for key, value in Books.items():
            print(
                f"Book ID: {key}\nName: {value['Book name']}\nStocks: {value['Book stock']}")
    else:
        print("No current available Books")

    # Pause for user input and return to the main interface function
    input("Please press Enter to continue...")
    return interface

def del_Books(book_id):
    # Function to delete a book from the library
    if book_id in Books:
        del Books[book_id]
        print("Successfully Deleted.")
    else:
        print(f"No book with the id {book_id}")

    # Pause for user input and return to the main interface function
    input("Please press Enter to continue...")
    return interface

def edit_Books(book_id, new_book_name, new_book_count):
    # Function to edit information about a book in the library
    Books[book_id] = {'Book name': new_book_name, 'Book stock': new_book_count}
    print(f"Book {new_book_name} Succesfully Edited.")
    return interface

def borrow_book(book_id):
    # Function to borrow a book from the library
    if book_id in Books:
        if Books[book_id]['Book stock'] > 0:
            Books[book_id]['Book stock'] -= 1
            print(f"Book {Books[book_id]['Book name']} successfully borrowed.")
        else:
            print("Sorry, no current copies of the book.")
    else:
        print(f"Sorry no book with the ID {Books[book_id]}")

    # Pause for user input and return to the main interface function
    input("Please press any key to continue...")
    return interface

def interface():
    # Main interface function for the library management system
    while True:
        os.system('cls')  # Clear the console screen
        print('''
        \n\nACTIONS:
        1 -> Borrow a Book
        2 -> View Available Books
        3 -> Add Books
        4 -> Remove a Book
        5 -> Edit Book Information
        6 -> Exit\n
            ''')
        user_input = int(input("Enter an action: "))

        # Use the 'match' statement to handle different user actions
        match user_input:
            case 1:
                # Borrow a Book
                if Books:
                    print("\nBorrow a Bool\n")
                    for key, value in Books.items():
                        print(
                            f"Book ID: {key}\nName: {value['Book name']}\nStocks: {value['Book stock']}")
                    borrow_id = int(
                        input("\nEnter the Book ID you want to borrow: "))
                    borrow_book(borrow_id)
                else:
                    print("No Available Books. ")
                    input("Press Enter to continue...")
                    interface()
            case 2:
                # View Available Books
                view_Books()
            case 3:
                # Add Books
                print("Add Books")
                add_id = int(input("\nEnter the ID number of the Book: "))
                book_Name = input("Enter the book name: ")
                book_Count = int(
                    input("Enter the number of the stock of the book: "))
                add_Books(add_id, book_Name, book_Count)
            case 4:
                # Remove a Book
                if Books:
                    del_id = int(input("Enter the ID of the book: "))
                    del_Books(del_id)
                else:
                    print("No Current Books to Delete.")
                    input("Press any key to continue...")
                    interface()
            case 5:
                # Edit Book Information
                if Books:
                    print("Edit Book")
                    edit_id = int(input("\nEnter the ID of the book: "))
                    new_name = input("Enter the new name of the book: ")
                    new_count = int(input("Enter the number of stocks: "))
                    edit_Books(edit_id, new_name, new_count)
                else:
                    print("No Current Books.")
                    input("Press any key to continue...")
                    interface()
            case 6:
                # Exit
                exit()

if __name__ == "__main__":
    # Start the library management system interface
    interface()
