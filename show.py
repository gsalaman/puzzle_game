
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

if __name__ == '__main__':
  print("initalized")
  
  # 1st test...just show our pic.  
  solved_puzzle = Image.open("puzzle_game_1.png")
  solved_puzzle = solved_puzzle.convert("RGB")
  solved_puzzle = solved_puzzle.resize((total_rows, total_columns))

  matrix.SetImage(solved_puzzle, 0, 0)

  while True:
    time.sleep(.1)


