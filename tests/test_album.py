from lib.album import *

# When I construct an album with the fields title, release year
# and artist_id, they are reflected in the instance properties

def test_constructs_with_fields():
    album = Album(1, "Greatest Hits", 2012, 1)
    assert album.id == 1
    assert album.title == "Greatest Hits"
    assert album.release_year == 2012
    assert album.artist_id == 1




