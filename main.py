# hello world
print("init")

matrix = [[[0 for rgb in range(3)] for y in range(10)] for x in range(10)]

for x in range(10):
    for y in range(10):
        for rgb in range(3):
            matrix[x][y][rgb] = x * y * rgb
print(matrix)
