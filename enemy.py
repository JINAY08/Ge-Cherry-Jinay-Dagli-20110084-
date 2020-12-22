# # this file is mainly for initialising the coordinates of enemies and changing and displaying them at their final positions. # #

import pygame
import random
pygame.init()
enemies = []
enemy1_x,enemy1_y = random.randint(12,15),random.randint(13,14)
enemy2_x,enemy4_x,enemy2_y,enemy4_y = random.randint(12,14),random.randint(14,16),random.randint(13,14),random.randint(13,14)
enemy3_x = random.randint(13,17)
enemy3_y = random.randint(14,16)
enemy1_xchange,enemy1_ychange = 1,0
enemy2_xchange,enemy2_ychange = 0,-1
enemy4_xchange,enemy4_ychange = 0,-1
enemy1img = pygame.image.load('enemy1.png')
enemy2img = pygame.image.load('enemy2.png')
enemy3img = pygame.image.load('enemy3.png')
enemy4img = pygame.image.load('enemy2.png')

