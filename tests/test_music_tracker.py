from lib.music_tracker import *

def test_check_tracklist_initially_empty():
    music_library = MusicLibrary()
    assert music_library.view_tracklist() == []

def test_format_track():
    track = Track("thriller","michael jackson")
    assert track.format() == "Thriller by Michael Jackson"