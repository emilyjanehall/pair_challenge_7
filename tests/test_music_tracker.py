import pytest
from lib.music_tracker import *

def test_check_tracklist_initially_empty():
    music_library = MusicLibrary()
    assert music_library.view_tracklist() == []

def test_format_track():
    track = Track("thriller", "michael jackson")
    assert track.format() == "Thriller by Michael Jackson"

def test_add_then_view_track_list():
    music_library = MusicLibrary()
    track = Track("Perfect", "One Direction")
    music_library.add_track(track)
    assert music_library.view_tracklist() == [track.format()]

def test_name_is_string():
    with pytest.raises(TypeError, match= "Name and Artist must be a string"):
        track = Track(1, 2)