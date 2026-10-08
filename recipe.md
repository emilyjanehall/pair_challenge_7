As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

# 1 - Class design
``` python
class Track():
    def __init__(self, name, artist):
        # Parameters:
        #   name: string
        #   artist: string
        # Side effects:
        #   Initialises self.name as name
        #   Initialises self.artist as artist

    def format(self):
        # Parameters:
        #   none
        # Returns:
        #   f"{name} by {artist}"

class MusicLibrary():
    def __init__(self):
        # Parameters:
        #   none
        # Side effects:
        #   Initialises self.track as track
        #   Initialises self.track_list as empty list []
    
    def add_track(self, track):
        # Parameters:
        #   track: object
        # Side effects:
        #   adds track to track_list

    def view_tracklist(self):
        # Parameters:
        #   none
        # Returns:
        #   track_list
```
