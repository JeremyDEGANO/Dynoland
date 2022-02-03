import pygame

pygame.display.init()
pygame.display.set_caption("DynoLand")
pygame.display.set_mode((1080,720))

isRunning = True

#initialize background
#background = pygame.image.load()

#Boucle infini du jeu
while isRunning:

    #Verif if player shut the game
    for event in pygame.event.get():
        if event == pygame.QUIT:
            isRunning = False
            pygame.quit()
            print('the game as been closed')
