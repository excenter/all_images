# hello world
print("init")
from PIL import Image

HEIGHT = 100
WIDTH = 100

im = Image.new("RGB",(HEIGHT,WIDTH),color=0)
pix = im.load()


matrix = [[[0 for rgb in range(3)] for y in range(WIDTH)] for x in range(HEIGHT)]

for x in range(HEIGHT):
    for y in range(WIDTH):
        for rgb in range(3):
            matrix[x][y][rgb] = x * y
        pix[x,y] = (matrix[x][y][0],matrix[x][y][1],matrix[x][y][2])

print(matrix)

im.save("new.png")
