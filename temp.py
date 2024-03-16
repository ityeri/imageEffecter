from PIL import Image

image = Image.open("icon.png")

matrix = [[0 for i in range(64)] for j in range(64)]

for y in range(64):
    for x in range(64):
        if image.getpixel((x, y))[3] >= 127:
            matrix[y][x] = 1

print('[')
for y in range(64):
    print(f'{matrix[y]},')
print(']')