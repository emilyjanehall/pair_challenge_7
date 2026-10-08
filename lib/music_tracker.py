class Track():
    def __init__(self, name, artist):
        # Parameters:
        #   name: string
        #   artist: string
        # Side effects:
        #   Initialises self.name as name
        #   Initialises self.artist as artist
        if not isinstance(name, str) or not isinstance(artist, str):
            raise TypeError("Name and Artist must be a string")
        self.name = name
        self.artist = artist

    def format(self):
        # Parameters:
        #   none
        # Returns:
        #   f"{name} by {artist}"
        return f"{self.name.title()} by {self.artist.title()}"

class MusicLibrary():
    def __init__(self):
        # Parameters:
        #   none
        # Side effects:
        #   Initialises self.track as track
        #   Initialises self.track_list as empty list []
        self.track_list = []
    
    def add_track(self, track):
        # Parameters:
        #   track: object
        # Side effects:
        #   adds track to track_list
        return self.track_list.append(track.format())
        

    def view_tracklist(self):
        # Parameters:
        #   none
        # Returns:
        #   track_list
        return self.track_list