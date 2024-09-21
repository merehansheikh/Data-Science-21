from console_app import *

if __name__ == "__main__":
    
    # Main program loop
    while True:
        print('Select an operation:')
        print('1. View all books')
        print('2. View a single book')
        print('3. Add a new book')
        print('4. Update an existing book')
        print('5. Delete a book')
        print('6. Quit')
        choice = input('Enter your choice: ')
        # choice = input(3)

        if choice == '1':
            view_all_books()
        elif choice == '2':
            book_id = input('Enter the book ID: ')
            view_book(book_id)
        elif choice == '3':
            title = input('Enter the book title: ')
            author = input('Enter the book author: ')
            genre = input('Enter the book genre: ')
            publisher = input('Enter the book publisher: ')
            publish_date = input('Enter the publish date: ')
            price = int(input('Enter the price of the book: '))
            description = input('Enter the description: ')
            
            add_book(title, author, genre, publisher, publish_date, price, description )

        elif choice == '4':
            idd = input('Enter the id you want to change: ')
            
            update_book(idd)
            
        elif choice == '5':
            idd = input('Enter the id of the book you want to delete: ')
            delete_book(idd)
            
        else:
            
            break