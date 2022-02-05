import pygame

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

#generate random maze 
def create_maze(w, h):
    maze = []
    for i in range(0, h):
        line = []
        for j in range(0, w):
            line.append('u')
        maze.append(line)
    return maze


    
