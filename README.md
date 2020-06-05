# get_lyric
Foobar Lyric Show 3 component external_command script to retrieve lyrics from genius.com

# Prerequisites:
  - foobar2000
  - foo_uie_lyrics3 plugin (ie: Lyric Show 3), available here: https://github.com/tripod31/foo_lyricsource
  - python3 environment
  - genius.com account and corresponding API access/token
  - lyricsgenius python module, provided by John W. Miller here: https://github.com/johnwmillr/LyricsGenius

# Setup
`git clone` or copy the contents of `get_lyric.py`, and place it into your foobar2000 installation directory, ie: `C:\Program Files (x86)\foobar2000`

Replace the API_KEY placeholder string in the script with your API token from genius.com

# Script test
Test the script using the following syntax: `.\get_lyric.py --artist "Trace Mountains" --song "Absurdity"`

If successful, the lyrics should display on the terminal.

# Foobar setup
Now, in Foobar, go to Preferences -> Tools -> Lyric Show 3, and remove all entries you can from the `Search order` table, and ensure that `external command` method is present in the `Search order` table and is first. Ensure you apply accordingly. A restart of foobar should not be required.

Assuming you followed all of the steps, lyrics should display dynamically!
