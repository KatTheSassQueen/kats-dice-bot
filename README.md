# Kat's Dice Bot
A discord dice bot that is made by me and meant for dice rolling...and music and some fun social things too.

## Prior to Running:
You will need to obtain some crucial information.
(If you know me, then you can get mine from me.  OTHERWISE!)
- Discord Bot Token
- Spotify Developer Client ID
- Spotify Developer Client Secret
These must be placed at the top (for spotify, in the global variable section) or bottom (for discord, literally the last line except comments).

## Replacing the CENSORING
I'm not giving you my filepath/username/etc.  So I've removed a few things and this will **NOT** run straight downloaded!  You will need to replace the following (lines 28, 29, 30, and 31 as of the commit on 2026-08-24):
- Spotify Developer Client ID and Client Secret
- The filepath to where you have the FFMPEG executable saved
- The bot token/secret

## How to Use:
I usually use this with a Windows command prompt, but any way you can open it that runs it perpetually in the background should work.

You'll need to make sure that your PYTHONPATH includes any packages you installed (with pip, for example) to make this run, as well as FFMPEG.  For me, with a little censoring, this looks like:
`set PYTHONPATH=%PYTHONPATH%;C:\Users\[USERNAME]\AppData\Local\Programs\Python\Python313\Lib\site-packages`
`set PYTHONPATH=%PYTHONPATH%;C:\Users\[USERNAME]\AppData\Local\Programs\Python\Python313\Lib\site-packages\discord\ffmpeg\bin`

You'll then want to change directory to the directory holding the code.  Again, with a little censoring, for me this looks like:
`cd C:\Users\[USERNAME]\Desktop\Dice-Bot`
Yes, I'm aware code on the desktop is a bad idea, but here we are anyway!

Finally, run the code with Python, which will be:
`python dice-bot.py`
in your command prompt.

## Dependencies
You will need to ensure the following libraries are installed on your Python path:
- asyncio
- discord
- math
- numpy
- re
- yt_dlp
- spotipy
