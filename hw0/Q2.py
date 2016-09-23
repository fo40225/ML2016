import sys
from PIL import Image

Image.open(sys.argv[1]).rotate(180).save("ans2.png")
