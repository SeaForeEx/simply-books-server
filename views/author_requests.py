import sqlite3
import json
from models import Author

def get_single_author(id):
    """Get a single author
    """
    # open a connection to the database
    with sqlite3.connect("./simply.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        # write the SQL query to get the info you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.email,
            a.first_name,
            a.last_name,
            a.image,
            a.favorite
        FROM author a
        WHERE a.id = ?                  
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        author = Author(data['id'], data['email'], data['first_name'], data['last_name'], data ['image'], data['favorite'])
        
        return author.__dict__
      
def get_all_authors():
    """Get all authors
    """
    
    #Open a connection to the database
    with sqlite3.connect("./simply.sqlite3") as conn:
      
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
    
        # Write SQL query to get the info you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.email,
            a.first_name,
            a.last_name,
            a.image,
            a.favorite
        FROM Author a                
        """)
        
        # Initialize an empty list to hold all author representations
        authors = []
        
        # convert rows of data into a Python list
        dataset = db_cursor.fetchall()
        
        # iterate list of data returned from database
        for row in dataset:

            # create author instance from current row
            author = Author(row['id'], row['email'], row['first_name'], row['last_name'], row['image'], row['favorite'])
            
            # add dictionary representation of author to the list
            authors.append(author.__dict__)
            
    return authors
  
  
    
    
