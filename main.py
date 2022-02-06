import pygame
import random
import PIL
from PIL import Image
from functions import *

#initialize pygame \_(ツ)_/¯
pygame.display.init()
pygame.display.set_caption("DynoLand")
WIDTH = 1920
HEIGHT = 1020
screen = pygame.display.set_mode((WIDTH,HEIGHT))

#----------------Variables----------------------#
isRunning = True
clock = pygame.time.Clock()
i=0
j=0

#initialize background
background = pygame.image.load('assets/background.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
#load Bush image
bush_img = Func('assets/bush.png')
bush1 = bush_img.sprite(0, 0, 65, 65)
bush2 = bush_img.sprite(65, 0, 65, 65)
bush3 = bush_img.sprite(140, 0, 65, 65)
bush4 = bush_img.sprite(205, 0, 65, 65)
bushs = (bush1, bush2, bush3, bush4)
#initialize maze
maze = create_maze(int(WIDTH/65), int((HEIGHT/65)*0.70))
printMaze(maze, int(WIDTH/65), int((HEIGHT/65)*0.70))
for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == 'w':
                maze[y][x] = random.randint(0, 3)

#-----------------------------------------------#

#Boucle infini du jeu
while isRunning:
    #frame of game
    clock.tick(60)    
    #initialize background
    screen.blit(background, (0, 0))
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] != 'c':
                screen.blit(bushs[maze[y][x]], (x*65+20, y*65+300))
    pygame.display.flip()
    #Verif if julien shut the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                maze = create_maze(int(WIDTH/65), int((HEIGHT/65)*0.70))
                for y in range(len(maze)):
                    for x in range(len(maze[0])):
                        if maze[y][x] == 'w':
                            maze[y][x] = random.randint(0, 3)
            if event.key == pygame.K_DOWN:
                j += 5
            if event.key == pygame.K_LEFT:
                i += -5
            if event.key == pygame.K_RIGHT:
                i += 5
