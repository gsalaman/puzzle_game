
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image
import time

##RGB Matrix Standards
# Size of one panel
matrix_rows = 32 
matrix_columns = 32 

# How many mattixes stacked horizontally and vertically
matrix_horizontal = 8
matrix_vertical = 2

total_rows = 128 
total_columns = 128 

options = RGBMatrixOptions()
options.rows = matrix_rows
options.cols = matrix_columns
options.chain_length = matrix_horizontal
options.parallel = matrix_vertical
options.hardware_mapping = 'regular'
options.gpio_slowdown = 2
options.pixel_mapper_config = 'U-mapper'

matrix = RGBMatrix(options = options) #making the matrix for all programs

################################
# build_images
#
# this function returns a 2d array of images tiles, indexed by "proper" 
# board location. For example, images[0][0] is the tile that belongs in 
# the top left.
################################
def build_images(num_x_tiles, num_y_tiles, tile_width, tile_height):

  # first step: open our solved puzzle
  solved_puzzle = Image.open("puzzle_game_1.png")
  solved_puzzle = solved_puzzle.convert("RGB")
  solved_puzzle = solved_puzzle.resize((total_rows, total_columns))

  # next, make an empty array for us to populate with images
  images = [[None for i in range(num_x_tiles)] for j in range(num_y_tiles)]

  # x and y corner mark the current "top left" corner of the tile
  x_corner = 0
  y_corner = 0
  
  # iterate through our image, creating sub-tiles
  for y in range (num_y_tiles):
    for x in range (num_x_tiles):
      images[x][y] = solved_puzzle.crop((x_corner, y_corner, 
                             x_corner + tile_width, y_corner + tile_height))
      x_corner = x_corner + tile_width
    x_corner = 0
    y_corner = y_corner + tile_width

  return images
  
#######################################################
# show_tile
#
# This function displays a given tile at the specified x,y coordinates
#
# example:  show_tile((7,0), (0,7)) 
#   shows the tile that belongs at the top-right corner in the bottom-left 
#######################################################
def show_tile(image_array, src_pos, dest_pos, tile_width, tile_height, matrix):
  tile_image = image_array[src_pos[0]][src_pos[1]]
  
  # dest_pos is indexed 0-7, but we need it to be absolute (0-127)
  dest_x = dest_pos[0] * tile_width 
  dest_y = dest_pos[1] * tile_height 
  
  matrix.SetImage(tile_image, dest_x, dest_y)
   

#######################################################
# populate_scramble
# 
# This function returns a 2d list of scrambled tile locations.
# Each array cell gives the x,y coordinates (0-7) of the tile being displayed in
# that locaiton. 
#######################################################
def populate_scramble():

  standard_spots = [[(i,j) for i in range(8)] for j in range(8)]

  source_list = []

  for row in standard_spots:
    for item in row:
      source_list.append(item)

  random.shuffle(source_list)
  return source_list

#######################################################
#  highlight_tile
#
#  This function highlights a tile with a red boarder in the given x,y location
#  x,y in this case is TILE x,y (0-7) NOT matrix x,y (0-127)
#######################################################
def highlight_tile(matrix, tile):
  
  rect_image = Image.new("RGB", (16,16))
  rect_draw = ImageDraw.Draw(rect_image)
  rect_draw.rectangle((0,0,15,15), outline = (255,0,0) 
  
  x = tile[0] * 16
  y = tile[1] * 16

  matrix.SetImage(rect_image, x, y)

#######################################################
# check_for_win
# 
# This function checks the passed tile location array to see whether
# all tiles are in the correct location.  If so, it returns True.
#######################################################
def check_for_win(tiles):

  for y in range(8):
    for x in range(8):
      tile = tiles[x][y]
      if (tile[0] != x):
        return False
      if (tile[1] != y):
        return False

  return True
        
#######################################################
if __name__ == '__main__':
  print("initalized")
  
  # images is a 2d array of our tiles, indexed by "proper" board location. 
  # For example, images[0][0] is the tile that belongs in the top left.
  images = build_images(8,8,16,16) 

  # next test...see if I've broken up the images correctly
  for y in range(8):
    for x in range(8):
      show_tile(images, (x,y), (x,y), 16, 16, matrix)

  # scramble the tile locations
  tile_locations = populate_scramble() 

  # and show the scrambled puzzle
  for y in range(8):
    for x in range(8):
      src_location = tile_locations[x][y]
      dest_location = (x,y)
      show_tile(images, src_location, dest_location, 16, 16, matrix)
  
     
  game_over = False 
  while !game_over:
    
    # Get a button press.  That corresponds to our source tile.
    src_tile = get_buttons.wait_for_press()

    # highlight it.
    highlight_tile(matrix, src_tile)

    # potential debounce goes here...if we need it, wait for a short 
    # time (50ms?), clear the button queue, then move on to reading dest
    # tile.

    # now, get a second button press for our destination tile.
    dest_tile = get_buttons.wait_for_press()

    # swap source and destination
    # note that src_tile and dest_tile are the x,y of the two chosen tiles.
    # I'm gonna make src_image and dest_image to show which images
    # were originally in those 2 locations, then swap them.
    src_img = tile_locations[src_tile[0]][src_tile[1]]
    dest_img = tile_locations[dest_tile[0]][dest_tile[1]]
    tile_locations[src_tile[0]][src_tile[1]] = dest_img
    tile_locations[dest_tile[0]][dest_tile[1]] = src_img

    # show just those two swapped tiles.  
    # note that since we've swapped, src_image is in dest_tile and 
    # dest_image is in src_tile
    # This will also "undo" the highlight.
    show_tile(images, src_img, dest_tile, 16, 16, matrix)
    show_tile(images, dest_img, src_tile, 16, 16, matrix)

    # check for win
    game_over = check_for_win():

  # This is the end of the while loop.  If we get here, the game is over
  print("Game Over!")

