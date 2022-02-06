import pygame
import random
import PIL
from PIL import Image
from functions import *

#initialize pygame
pygame.display.init()
pygame.display.set_caption("DynoLand")
WIDTH = 1920
HEIGHT = 1020
screen = pygame.display.set_mode((WIDTH,HEIGHT))

#----------------Variables----------------------#
isRunning = True
clock = pygame.time.Clock()

#initialize background
background = pygame.image.load('assets/background.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
#load Bush image
bush_img = Func('assets/bush.png')
dyno = pygame.image.load("assets/dino-left.jpg")
bush1 = bush_img.sprite(0, 0, 65, 65)
bush2 = bush_img.sprite(65, 0, 65, 65)
bush3 = bush_img.sprite(140, 0, 65, 65)
bush4 = bush_img.sprite(205, 0, 65, 65)
bushs = (bush1, bush2, bush3, bush4, dyno)
#initialize maze
maze = make_maze(int(WIDTH/65), int((HEIGHT/65)*0.70))
print(maze)
maze = maze.replace(' ', '4')
i=0
j=0
maze = maze.replace('+', str(random.randint(0, 3)))
maze = maze.replace('--', str(random.randint(0, 3)))
maze = maze.replace('|', str(random.randint(0, 3)))
maze = maze.replace('\n', '')
print(maze)
#-----------------------------------------------#

#Boucle infini du jeu
while isRunning:
    #frame of game
    clock.tick(60)    
    #initialize background
    screen.blit(background, (0, 0))
    for index, cell in enumerate(maze):
        y = index%WIDTH
        x = index-y
        screen.blit(bushs[int(cell)], (y*65+20, x*65+300))
    pygame.display.flip()
    #Verif if player shut the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                j += -5
            if event.key == pygame.K_DOWN:
                j += 5
            if event.key == pygame.K_LEFT:
                i += -5
            if event.key == pygame.K_RIGHT:
                i += 5
