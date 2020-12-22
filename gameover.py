# # this file helps in displaying the gameover screen once the vectors of player position and enemy position becomes equal # #

import pygame
pygame.init()
screen = pygame.display.set_mode((620,680))
gameover = pygame.image.load('game-over.png')
def game_over():
    screen.blit(gameover,(180,50))
run = True
while run:
    game_over()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.update()