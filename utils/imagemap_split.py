"""
Use this script to split imagemaps into several sprites
"""

from PIL import Image
from os import mkdir, path

WIDTH = 128
HEIGHT = 192
ROWS = 4
COLS = 4
IMAGEMAP = "rome.png"
OUTPUT_DIR = "output"

sprite_width = WIDTH//COLS
sprite_height = HEIGHT//ROWS


sheet = Image.open(IMAGEMAP)
count = 1

for y in range(COLS):
    for x in range(ROWS):
        a = (x + 1) * sprite_width
        b = (y + 1) * sprite_height
        icon = sheet.crop((a - sprite_width, b - sprite_height, a, b))
        icon.save(path.join(OUTPUT_DIR, "{}.png".format(count)))
        count += 1
