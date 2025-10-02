# Kat's Dice Bot
A discord dice bot that is made by me and meant for dice rolling...and music and some fun social things too.

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
