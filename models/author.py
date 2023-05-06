class Author():
    """Initializes Author Class
    """
    def __init__(self, id, email, first_name, last_name, image, favorite=False):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.image = image
        self.favorite = favorite
