import sqlite3
import json
from models import Book

def get_single_book(id):
    """Get a single book
    """
    # open a connection to the database
    with sqlite3.connect("./simply.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        # write the SQL query to get the info you want
        db_cursor.execute("""
        SELECT
            b.id,
            b.title,
            b.image,
            b.price,
            b.sale,
            b.description
        FROM book b
        WHERE b.id = ?                  
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        book = Book(data['id'], data['title'], data['image'], data['price'], data ['sale'], data['description'])
        
        return book.__dict__
      
def get_all_books():
    """Get all books
    """
    
    # Open a connection to the database
    with sqlite3.connect("./simply.sqlite3") as conn:
      
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
    
        # Write SQL query to get the info you want
        db_cursor.execute("""
        SELECT
            b.id,
            b.title,
            b.image,
            b.price,
            b.sale,
            b.description
        FROM Book b                
        """)
        
        # Initialize an empty list to hold all book representations
        books = []
        
        # convert rows of data into a Python list
        dataset = db_cursor.fetchall()
        
        # iterate list of data returned from database
        for row in dataset:

            # create author instance from current row
            book = Book(row['id'], row['title'], row['image'], row['price'], row['sale'], row['description'])
            
            # add dictionary representation of book to the list
            books.append(book.__dict__)
            
    return books
  
  
    
    
