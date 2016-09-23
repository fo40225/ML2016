import sys
from PIL import Image

img =  Image.open(sys.argv[1])

out = img.rotate(180)

out.save("ans2.png")