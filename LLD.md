# Low Level Design

## Data Architecture - Picture Info
We're starting with a 6x6 grid of 16x16 images.  I'm going to call each 16x16 a "tile".  Helpful defines:
```
grid_x =      6  # number of tiles in the x direction
grid_y =      6  # number of tiles in the y direction
tile_width = 16  # x dimension of each tile
tile_height = 16 # y dimension of each tile
```

`images` is a 2d array of our 6x6 tiles, indexed by "proper" location on the display.  Meaning `images[0][0]` refers to the tile that *belongs* in the top left.

`tile_location` is a 2d array that maps each tile to it's location on the board.  There are two ways to do this:
*  use index as grid index (where that tile is on the board) and have a tuple for the actual index (via `images[][]`)
*  use index as actual index (via `images[][]`) and have the tuple indicate where on the board that image is.

I'm gonna start with the former...this may change.

## Main Flow
Main Flow --- while true:
* do game init  (game_init())
* solved = False
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
