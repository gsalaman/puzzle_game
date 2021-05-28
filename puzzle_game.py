
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
if __name__ == '__main__':
  print("initalized")
  
  # images is a 2d array of our tiles, indexed by "proper" board location. 
  # For example, images[0][0] is the tile that belongs in the top left.
  images = build_images(8,8,16,16) 

  # next test...see if I've broken up the images correctly
  for y in range(8):
    for x in range(8):
      show_tile(images, (x,y), (x,y), 16, 16, matrix)
      time.sleep(1)
     
  while True:
    time.sleep(.1)


