class Album:

    def __init__(self, id, title, release_year, artist_id):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    # Compare the object attributes, not the memory locations. Two object instances may have the same contents
    # but Python will say they are not the same


    def __repr__(self):
        return f"Album({self.id}, {self.title}, {self.release_year}, {self.artist_id})"
    
    # Print the object result in a nice readable format. Not memory location

