# Wizards-Curse
This project utilizes a raspberry pi to play music, sound cues, search for input, and unlock a magnetic lock.
This project has been entirely re-written by myself, for increased readability, reliability, and functionality.

First, the players tilt a number of paintings upright, triggering tilt sensors which the program picks up, and plays an audio cue.
Then, a hidden button is pressed, which gives another clue, and successive presses repeat this clue.
Finally, four banners must be placed in the correct order, which opens the door into the next room.

In the future, I would avoid using tilt switches as they are unreliable in their current format and trigger multiple calls at a time.

In order for the program to parse all files correctly, place this repository on the pi desktop as-is, and you'd probably need to change the root folder name in the newmagic.py file as well
