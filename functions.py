import pygame
import random
import time
from colorama import init
from colorama import Fore, Back, Style
from random import shuffle, randrange

class Func:
    def __init__(self, file):
        self.file = file
        self.img_to_crop = pygame.image.load(file).convert()

    #Function Sprite to crop bush
    def sprite(self, x, y, w, h):
        sprite = pygame.Surface((w,h))
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.img_to_crop, (0, 0), (x, y, w, h))
        return sprite

def listen_event(width, height, x, y):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y += -1*65
            if event.key == pygame.K_DOWN:
                y += 1*65
            if event.key == pygame.K_LEFT:
                x += -1*65
            if event.key == pygame.K_RIGHT:
                x += 1*65
            if event.key == pygame.K_SPACE:
                maze = create_maze(int(width/65), int((height/65)*0.70))
                for h in range(len(maze)):
                    for w in range(len(maze[0])):
                        if maze[h][w] == 'w':
                            maze[h][w] = random.randint(0, 3)
                x=20
                y=35
    return x, y
