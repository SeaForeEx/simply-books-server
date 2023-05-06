class Author_Book():
    """Initializes Author_Book Class
    """
    def __init__(self, id, author_id = "", book_id = ""):
        self.id = id
        self.author_id = author_id
        self.book_id = book_id
        self.author = None
        self.book = None
        
