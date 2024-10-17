from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository


class Application():
  def __init__(self):
    self._connection = DatabaseConnection()
    self._connection.connect()
    self._connection.seed("seeds/music_library.sql")

  def run(self):

    print("Welcome to the music library manager!\nWhat would you like to do? \n1 - List all albums \n2 - List all artists")

    selection = input()

    if selection == str(2):
        artist_repository = ArtistRepository(self._connection)
        artists = artist_repository.all()

        for artist in artists:
            print(f"{artist.id}: {artist.name} ({artist.genre})")

    elif selection == str(1):
        album_repository = AlbumRepository(self._connection)
        albums = album_repository.all()

        for album in albums:
            print(f"{album.id}: {album.title} ({album.release_year})")

       
if __name__ == '__main__':
    app = Application()
    app.run()

    # "Runs" the terminal application.
    # It might:
    #   * Ask the user to enter some input
    #   * Make some decisions based on that input
    #   * Query the database
    #   * Display some output
    # We're going to print out the artists!

#     artist_repository = ArtistRepository(self._connection)
#     artists = artist_repository.all()

#     for artist in artists:
#         print(f"{artist.id}: {artist.name} ({artist.genre})")


# # Connect to the database
# connection = DatabaseConnection()
# connection.connect()

# # Seed with some seed data
# connection.seed("seeds/music_library.sql")

# # Retrieve all artists
# artist_repository = ArtistRepository(connection)
# artists = artist_repository.all()

# # List them out
# for artist in artists:
#     print(artist)

# # Retrieve all albums
# album_repository = AlbumRepository(connection)
# albums = album_repository.all()

# for album in albums:
#     print(album)


