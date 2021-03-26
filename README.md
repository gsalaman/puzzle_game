# Puzzle Game for the Jumbotron
Concept:  
* take a square image and break it into an grid of pieces
* randomize those pieces and display
* User clicks a piece to select, then clicks a piece where they want it to go
* Once puzzle is complete, user wins!!!

Start with a 6x6 grid and have a back button and timer?  Maybe even a restart button?
Timer later.  High scores later.

Multi-select later (hold one piece and select others to group and then move as a chunk)

## Overall Architecture/HLD
2d array to hold images

2d array of current image locations...each s a tuple of the indexes of the image array

function to determine win:  loop through location array and see if all pieces are in the right spots

Power-up inits:
* break up image and create images array

Game inits:
* randomize piece locations and create locations array
* Display all pieces
* "solved" = False

Function to display image in an x,y location

"highlight" function for when piece is pressed?  (white rectangle?)

Main Flow --- while true:
* do game init
* while "not solved":
  * wait for button press
  * if that press was a "restart", break out of our "while not solved" loop
  * Highlight that piece
  * wait for another button press
  * Move highlighted piece to new location
  * Move new location piece to highlighted piece location
  * Check for solve
* If we're here, it's either solved or a restart
  * if solved, show "you win" screen and wait 3s (tbr)
  * If restart, show "restarting..." wait 1s (tbr)
