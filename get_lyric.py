# Written by Lukasz Sulek
#
# Credit goes to John W. Miller for publishing the lyricsgenius module available below:
# https://github.com/johnwmillr/LyricsGenius

import lyricsgenius
import sys

# Create a free genius.com account to set up API access and replace/paste the key below
genius = lyricsgenius.Genius("API_KEY")

# Turn off status messages
genius.verbose = False

# Script is invoked like so when called by the external_command method:
#     [0]                [1]      [2]       [3]    [4]
#     \path\get_lyric.py --artist "$ARTIST" --song "$SONG"
song = genius.search_song(sys.argv[4], sys.argv[2])

# Note: if running on Windows, you may get a UnicodeEncodeError exception due to, well, Windows/Python default encoding
# Follow the steps here http://www.tiernok.com/posts/python-3-6-unicode-output-for-windows-console.html
# This will tell your python3 environment to use UTF-8
#   PYTHONIOENCODING UTF-8

try:
    print(song.lyrics)
except AttributeError:
    print(f"{sys.argv[2]} - {sys.argv[4]}\n\nLyrics not found")
