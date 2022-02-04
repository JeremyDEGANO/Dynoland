import pygame

pygame.display.init()
pygame.display.set_caption("DynoLand")
screen = pygame.display.set_mode((1080,720))

isRunning = True
clock = pygame.time.Clock()

#initialize background
background = pygame.image.load('assets/background.jpg')

#Boucle infini du jeu
while isRunning:
    clock.tick(30)   

    #initialize background
    screen.blit(background, (0, 0))
    pygame.display.flip()
    #Verif if player shut the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
            pygame.quit()
