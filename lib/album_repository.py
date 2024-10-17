from lib.album import *

class AlbumRepository():

    def __init__(self, connection):
        self._connection = connection
    

    #loop over the list of dictionaries and convert them to album objects
    def all(self):
        rows = self._connection.execute("SELECT * FROM albums")
        albums = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums
    
    def find_by_id(self, album_id):
        rows = self._connection.execute("SELECT * FROM albums WHERE id = %s", [album_id])
        row = rows[0]
        item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
        return item
    
    def create(self, album):
        self._connection.execute(
            "INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)",
            [album.title, album.release_year, album.artist_id]
        )

    def delete(self,album_id):
        self._connection.execute("DELETE FROM albums WHERE id = %s", [album_id])

