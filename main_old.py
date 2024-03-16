import pygame
from random import *
import os
import glob

pygame.init()

screenSize = 650

screen = pygame.display.set_mode((screenSize, screenSize), pygame.RESIZABLE)
pygame.display.set_caption("dd")

on = True

min = 4

path = "C:/Users/hahoah/Desktop/codingworkspace/파이똔/"
print("탐색 시작..")
pngFiles = glob.glob(path + "**/*.png", recursive=True)
print("탐색 끝")

index = 0

maxLoop = 20000
while True:
    try:
        img = pygame.image.load(pngFiles[index])
        break
    except: 
        print(f'"{pngFiles[index]}": Formet error')
        index += 1
if img.get_width() > img.get_height():
    ratio = screenSize / img.get_width()
    img = pygame.transform.scale(img, (img.get_width() * ratio, img.get_height() * ratio))

    offset = (0, (screenSize - img.get_height()) / 2)
if img.get_width() < img.get_height():
    ratio = screenSize / img.get_height()
    img = pygame.transform.scale(img, (img.get_width() * ratio, img.get_height() * ratio))

    offset = ((screenSize - img.get_width()) / 2, 0)

print(pngFiles[index])

count = 0

size = 50

while True:
    # screenSize = screen.get_size()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if index >= len(pngFiles):
                    index += 1
                    while True:
                        try:
                            img = pygame.image.load(pngFiles[index])
                            break
                        except: 
                            print(f'"{pngFiles[index]}": Formet error')
                            index += 1
                    if img.get_width() > img.get_height():
                        ratio = screenSize / img.get_width()
                        img = pygame.transform.scale(img, (img.get_width() * ratio, img.get_height() * ratio))

                        offset = (0, (screenSize - img.get_height()) / 2)
                    else:
                        ratio = screenSize / img.get_height()
                        img = pygame.transform.scale(img, (img.get_width() * ratio, img.get_height() * ratio))

                        offset = ((screenSize - img.get_width()) / 2, 0)
                    
                    print(pngFiles[index])

                    count = 0

                    size = 50
                else: print('마지막 이미지 입니다.')
            
            elif event.key == pygame.K_LEFT:
                if index > 0:
                    index -= 1
                    while True:
                        try:
                            img = pygame.image.load(pngFiles[index])
                            break
                        except: 
                            print(f'"{pngFiles[index]}": Formet error')
                            index -= 1
                    if img.get_width() > img.get_height():
                        ratio = screenSize / img.get_width()
                        img = pygame.transform.scale(img, (img.get_width() * ratio, img.get_height() * ratio))

                        offset = (0, (screenSize - img.get_height()) / 2)
                    else:
                        ratio = screenSize / img.get_height()
                        img = pygame.transform.scale(img, (img.get_width() * ratio, img.get_height() * ratio))

                        offset = ((screenSize - img.get_width()) / 2, 0)
                    
                    print(pngFiles[index])

                    count = 0

                    size = 50
                else: print('첫번째 이미지 임다')


    for i in range(5):
        x = randint(0, img.get_width() - 1)
        y = randint(0, img.get_height() - 1)
        try:
            pygame.draw.circle(screen, img.get_at((x, y)), (x+offset[0], y+offset[1]), size)

            if size > min: size *= 0.9995
            else: count += 1
        except: 
            print(f'"{pngFiles[index]}": Unknown error')

            index += 1
            img = pygame.image.load(pngFiles[index])
            if img.get_width() > img.get_height():
                ratio = screenSize / img.get_width()
                img = pygame.transform.scale(img, (img.get_width() * ratio, img.get_height() * ratio))

                offset = (0, (screenSize - img.get_height()) / 2)
            else:
                ratio = screenSize / img.get_height()
                img = pygame.transform.scale(img, (img.get_width() * ratio, img.get_height() * ratio))

                offset = ((screenSize - img.get_width()) / 2, 0)
            
            print(pngFiles[index])

            count = 0

            size = 50

            break

    if count >= maxLoop:
        index += 1
        try:
            img = pygame.image.load(pngFiles[index])
            break
        except: 
            print(f'"{pngFiles[index]}": Formet error')
            index += 1
        if img.get_width() > img.get_height():
            ratio = screenSize / img.get_width()
            img = pygame.transform.scale(img, (img.get_width() * ratio, img.get_height() * ratio))

            offset = (0, (screenSize - img.get_height()) / 2)
        else:
            ratio = screenSize / img.get_height()
            img = pygame.transform.scale(img, (img.get_width() * ratio, img.get_height() * ratio))

            offset = ((screenSize - img.get_width()) / 2, 0)
        
        print(pngFiles[index])

        count = 0

        size = 50

    pygame.display.update()