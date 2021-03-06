from encodings import utf_8
import pygame
import random
import os
import time
import json
from colorama import init
from colorama import Fore, Back, Style
from random import shuffle, randrange
from maze import create_maze

class Func:
    def __init__(self, file):
        self.file = file
        self.img_to_crop = pygame.image.load(file).convert()

    #Function Sprite to crop image
    def sprite(self, x, y, w, h):
        sprite = pygame.Surface((w,h))
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.img_to_crop, (0, 0), (x, y, w, h))
        return sprite

def listen_event(width, height, x, y, move, maze):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y-1 <0 or maze[y-1][x] != 'c':
                    return x, y
                y += -1
                move[0] = 1
                move[1] = (move[1] + 1)%4
            if event.key == pygame.K_DOWN:
                if y+1 >len(maze)-1 or maze[y+1][x] != 'c':
                    return x, y
                y += 1
                move[0] = 0
                move[1] = (move[1] + 1)%4
            if event.key == pygame.K_LEFT:
                if x-1 < 0 or maze[y][x-1] != 'c':
                    return x, y
                x += -1
                move[0] = 2
                move[1] = (move[1] + 1)%4
            if event.key == pygame.K_RIGHT:
                if x+1 >len(maze[0])-1 or maze[y][x+1] != 'c':
                    return x, y
                x += 1
                move[0] = 3
                move[1] = (move[1] + 1)%4
            if event.key == pygame.K_SPACE:
                maze = create_maze(int(width/65), int((height/65)*0.70))
                for h in range(len(maze)):
                    for w in range(len(maze[0])):
                        if maze[h][w] == 'w':
                            maze[h][w] = random.randint(0, 3)
    return x, y

def write_score(score, name):
    # check if size of file is 0
    file_path = '.\score.json'
    if os.stat(file_path).st_size == 0:
        dataplayer ={"score" : {name : score}}
        json_object = json.dumps(dataplayer, indent = 4)
        with open('score.json', 'w') as outfile:
            outfile.write(json_object)
    else:
        # get actual score in score.json
        with open('score.json') as json_file:
            data = json.load(json_file)
        # merge score
        saved_scores = data['score']
        if name in saved_scores:
            saved_scores[name] = score if score > saved_scores[name] else saved_scores[name]
        else:
            saved_scores[name] = score
        sorted_scores = dict(sorted(saved_scores.items(), key=lambda t: t[1], reverse=True))
        json_object = json.dumps({"score": sorted_scores}, indent = 4)
        with open('score.json', 'w') as outfile:
            outfile.write(json_object)
