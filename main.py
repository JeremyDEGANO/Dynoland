import pygame
import random
import sys
import PIL
from PIL import Image
from functions import *
from maze import *

#initialize pygame \_(ツ)_/¯
pygame.init()
pygame.display.init()
pygame.display.set_caption("DynoLand")
WIDTH = 1920
HEIGHT = 1020
screen = pygame.display.set_mode((WIDTH,HEIGHT))

#----------------Variables----------------------#
isRunning = True
clock = pygame.time.Clock()

score = 0
myfont = pygame.font.SysFont( 'monospace', 20, bold=pygame.font.Font.bold)
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
#load dyno image
dyno_img = Func('assets/dyno_sprite_back_front.png')
dyno_front1 = dyno_img.sprite(0, 0, 65, 65)
dyno_front2 = dyno_img.sprite(65, 0, 65, 65)
dyno_front3 = dyno_img.sprite(140, 0, 65, 65)
dyno_front4 = dyno_img.sprite(205, 0, 65, 65)
dynos_front = (dyno_front1, dyno_front2, dyno_front3, dyno_front4)
#back Dyno
dyno_back1 = dyno_img.sprite(0, 96, 65, 65)
dyno_back2 = dyno_img.sprite(65, 96, 65, 65)
dyno_back3 = dyno_img.sprite(140, 96, 65, 65)
dyno_back4 = dyno_img.sprite(205, 96, 65, 65)
dynos_back = (dyno_back1, dyno_back2, dyno_back3, dyno_back4)
#right Dyno
dyno_img_left_right = Func('assets/dyno_sprite_right_left.png')
dyno_right1 = dyno_img_left_right.sprite(0, 0, 65, 65)
dyno_right2 = dyno_img_left_right.sprite(65, 0, 65, 65)
dyno_right3 = dyno_img_left_right.sprite(140, 0, 65, 65)
dyno_right4 = dyno_img_left_right.sprite(205, 0, 65, 65)
dynos_right = (dyno_right1, dyno_right2, dyno_right3, dyno_right4)
#left Dyno
dyno_left1 = dyno_img_left_right.sprite(0, 96, 65, 65)
dyno_left2 = dyno_img_left_right.sprite(65, 96, 65, 65)
dyno_left3 = dyno_img_left_right.sprite(140, 96, 65, 65)
dyno_left4 = dyno_img_left_right.sprite(205, 96, 65, 65)
dynos_left = (dyno_left1, dyno_left2, dyno_left3, dyno_left4)

#initialize movement
dyno = (dynos_front, dynos_back, dynos_left, dynos_right)
move = [0, 0]
#initialize maze
maze = create_maze(int(WIDTH/65), int((HEIGHT/65)*0.70))
printMaze(maze, int(WIDTH/65), int((HEIGHT/65)*0.70))
for h in range(len(maze)):
        for w in range(len(maze[0])):
            if maze[h][w] == 'w':
                maze[h][w] = random.randint(0, 3)

x=20
y=35
x = [x for x, value in enumerate(maze[len(maze)-1]) if value == 'c'][0]
y = len(maze)-1
#-----------------------------------------------#

#Boucle infini du jeu
while isRunning:
    #frame of game
    clock.tick(60)    
    #initialize background
    screen.blit(background, (0, 0))
    #define score text
    scoretext = myfont.render("Score = "+str(score), 1, (255,255,255))
    screen.blit(scoretext, (5, 10))
    screen.blit(dyno[move[0]][move[1]], (x*65+20,y*65+300))
    for h in range(len(maze)):
        for w in range(len(maze[0])):
            if maze[h][w] != 'c':
                screen.blit(bushs[maze[h][w]], (w*65+20, h*65+300))
    pygame.display.flip()
    x, y = listen_event(WIDTH, HEIGHT, x, y, move, maze)
    #Verif if julien shut the game
