

import mysql.connector as sql

db = sql.connect(
    host="localhost",
    user="root",
    password="rajpootchauhan"
    )

use = 'use app;'

conn = db.cursor()
conn.execute(use)
# Function to view all books in the database
def display_query(query):
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    for info in result:
        print (*info, sep = " | ")

def view_all_books():
    conn.execute('SELECT * FROM books')
    res = conn.fetchall()
    for row in res:
        print(*row, sep= '|')

# Function to view a single book by its ID
def view_book(book_id):
    q = 'SELECT * FROM books WHERE id=' + str(book_id)
    display_query(q)
    # if row is not None:
    #     print(*row, sep= '|')
    # else:
    #     print(f'Book with ID {book_id} not found.')

# Function to add a new book to the database
def add_book(title, author, genre, publisher, publish_date, price, description):
    
    query = "INSERT INTO books(title, author, genre, publisher, publish_date, price, description) values (%s, %s, %s, %s, %s, %s, %s)"
    # val = f'{title}', '{author}', '{genre}', '{publisher}', '{publish_date}', {price}, '{description}:'
    val = (title, author, genre, publisher, publish_date, price, description)
    # print(query)
    conn.execute(query, val)
    db.commit()
    # display_query(query)
    print('Book added successfully.')

# Function to update an existing book by its ID
def update_book(book_id, title=None, author=None, genre=None, publisher=None, publish_date=None, price=None, description=None):
    updates = []
    if title is not None:
        updates.append(('title', title))
    if author is not None:
        updates.append(('author', author))
    if genre is not None:
        updates.append(('genre', genre))
    if publisher is not None:
        updates.append(('publisher', publisher))
    if publish_date is not None:
        updates.append(('publish_date', publish_date))
    if price is not None:
        updates.append(('price', price))
    if description is not None:
        updates.append(('description', description))

    if len(updates) == 0:
        print('No updates provided.')
    else:
        update_query = 'UPDATE books SET ' + ', '.join(f'{key}=?' for key, value in updates) + ' WHERE id=?'
        values = [value for key, value in updates] + [book_id]
        conn.execute(update_query, values)
        conn.commit()
        print('Book updated successfully.')

# Function to delete a book by its ID
def delete_book(book_id):
    conn.execute(f'DELETE FROM books WHERE id = {book_id}')
    conn.commit()
    print('Book deleted successfully.')

