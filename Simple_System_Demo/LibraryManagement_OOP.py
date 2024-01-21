import os

#name of the class. Dito sa class na to nakalagay ung mga process sa Library Management System
class LibraryManagementSystem:
    def __init__(self):
        # Dictionary to store information about books
        self.books = {} #Eto ung kunwaring lagayan ng books sa Library, dito nakalagay lahat ng books

    # Eto ung method sa pag aadd ng book. Method taawag dito instead of functions. 
    def add_book(self, book_id, book_name, book_count):
        # Add a book to the library
        self.books[book_id] = {'Book name': book_name, 'Book stock': book_count} #Dito namna, nag aadd na na book sa library, eto ung formay { book_id : { book_name: 'Sample Book', book_count : 12 (number of stocks to)} }
        
        print(f"Successfully Added the book {book_name}")
        input("Press Enter to continue...")

    #Eto naman ung method na view_books. Once na tawagin to, ididisplay lahat ung laman ng library
    def view_books(self):
        # View all available books in the library
        if self.books:
            for key, value in self.books.items(): #interation tawag dito, kinukuha lahat ng laman ng Library. 
                print(f"Book ID: {key}\nName: {value['Book name']}\nStocks: {value['Book stock']}") #Print lahat ng laman
        else:
            print("No current available Books")

        input("Press Enter to continue...")

    #Eto namna ung method na delete_block. Once na tawagin to at ilagay ung ID ng book, mededelete completely sa library.
    def delete_book(self, book_id):
        # Delete a book from the library
        if book_id in self.books: #Checks if the books is in the library, if meron, idedelete ung book.
            del self.books[book_id]
            print("Successfully Deleted.")
        else: # Pero kung wala, ididisplay lang na wala ung book.
            print(f"No book with the id {book_id}")

        input("Press Enter to continue...")

    #Eto namna ung method na edit_book. Eto ung tinatawag kapag may ieedit ka sa book. 
    def edit_book(self, book_id, new_book_name, new_book_count): # Ung tawag sa book_id, new_book_name and new_book_count is parameters. Same lang sa other methods, parameters din ung tawag sa laman nung parenthesis. 
        
        # Edit information about a book in the library
        self.books[book_id] = {'Book name': new_book_name, 'Book stock': new_book_count}
        print(f"Book {new_book_name} Successfully Edited.")
        input("Press Enter to continue...")

    #Eto naman ung method na nag baborrow ng book. Once na mag borrow ng book, mababawasan kung ilan ung hiniram na book.
    def borrow_book(self, book_id, borrow_count):
        # Borrow a book from the library
        if book_id in self.books: #Checks if the book is available in the library
            if self.books[book_id]['Book stock'] > borrow_count: #checks if the number of book is enough once na humiram si user
                self.books[book_id]['Book stock'] -= borrow_count # Ibabawas sa stocks kung ilan ung hiniram
                print(f"Book {self.books[book_id]['Book name']} successfully borrowed.")
            else:
                print("Sorry, there's no enough copies of the book.")
        else:
            print(f"Sorry, no book with the ID {book_id}")

        input("Press Enter to continue...")

    def library_interface(self):
        # Main interface for the library management system
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

            if user_input == 1:
                if self.books:
                    print("\nBorrow a Book\n")
                    for key, value in self.books.items():
                        print(f"Book ID: {key}\nName: {value['Book name']}\nStocks: {value['Book stock']}")
                    borrow_id = int(input("\nEnter the Book ID you want to borrow: "))
                    count_borrow = int(input("Enter the number of copies to borrow: "))
                    self.borrow_book(borrow_id, count_borrow)
                else:
                    print("No Available Books. ")
                    input("Press Enter to continue...")
                    self.library_interface()
            elif user_input == 2:
                self.view_books()
            elif user_input == 3:
                print("Add Books")
                add_id = int(input("\nEnter the ID number of the Book: "))
                book_Name = input("Enter the book name: ")
                book_Count = int(input("Enter the number of the stock of the book: "))
                self.add_book(add_id, book_Name, book_Count)
            elif user_input == 4:
                if self.books:
                    for key, value in self.books.items():
                        print(f"Book ID: {key}\nName: {value['Book name']}\nStocks: {value['Book stock']}")
                    del_id = int(input("\nEnter the ID of the book: "))
                    self.delete_book(del_id)
                else:
                    print("No Current Books to Delete.")
                    input("Press any key to continue...")
                    self.library_interface()
            elif user_input == 5:
                if self.books:
                    print("Edit Book")
                    for key, value in self.books.items():
                        print(f"Book ID: {key}\nName: {value['Book name']}\nStocks: {value['Book stock']}")
                    edit_id = int(input("\nEnter the ID of the book: "))
                    new_name = input("Enter the new name of the book: ")
                    new_count = int(input("Enter the number of stocks: "))
                    self.edit_book(edit_id, new_name, new_count)
                else:
                    print("No Current Books.")
                    input("Press any key to continue...")
                    self.library_interface()
            elif user_input == 6:
                exit()

# Main program
if __name__ == "__main__":
    library_system = LibraryManagementSystem()
    library_system.library_interface()
