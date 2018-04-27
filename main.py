# hello world
print("init")
from PIL import Image
import random

HEIGHT = 1080
WIDTH = 1920

def main():


    im = Image.new("HSV",(WIDTH,HEIGHT),color=0)
    pix = im.load()


    matrix = [[[0 for rgb in range(3)] for y in range(HEIGHT)] for x in range(WIDTH)]

    for x in range(WIDTH):
        for y in range(HEIGHT):
            for rgb in range(3):
                matrix[x][y][rgb] = round5(random.random()*255)
            # pix[x,y] = (matrix[x][y][0],matrix[x][y][1],matrix[x][y][2])
            pix[x,y] = (matrix[x][y][0],matrix[x][y][1],matrix[x][y][2])

    # print(matrix)
    print("about to save image")
    im.convert('RGB').save("new.png")
    print("image saved")



def round5(x, base=5):
    return int(base * round(float(x)/base))

main()
