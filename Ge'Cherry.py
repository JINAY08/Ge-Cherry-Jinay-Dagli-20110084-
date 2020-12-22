import pygame
import random
import math
import os
# importing enemy file ###
from enemy import *
pygame.init()                               # initialising pygame
from pygame import mixer                    # importing mixer module for adding sound effects
vector = pygame.math.Vector2                # importing vector module and referring it as 'vector'

# creating some empty lists ####
walls = []
coins = []
l1 = []
l2 = []
l3 = []
l4 = []

# # # setting up some initial display,icon,caption and font types # # #
screen = pygame.display.set_mode((620,680))
font = pygame.font.Font('freesansbold.ttf',26)
pygame.display.set_caption("Ge'Cherry : A modified game of Pacman")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# # #  assigning initial values to some variables # # #
score = 0
w,h = 620,680           # # # actual dimensions of screen # # #
wbuff,hbuff = 60,60     # # # leaving some buffer space(margins) on all four sides # # #
W,H = w - wbuff,h-hbuff
x_size = W//28           # dimensions of the grid # # #
y_size = H//30
player_x = 55
player_y = 53
player_x_change = 0
player_y_change = 0

# # # loading some images and storing them in the same directory as our game ###
backgroundimg = pygame.image.load('maze.png')
playerimg = pygame.image.load('pacman.png')
bonusimg = pygame.image.load('bonus.png')
gameover = pygame.image.load('game-over.png')

# # # # we define some functions that we will be using in our code thereafter # # #
def grid():
    for x in range(W):
        for y in range(H):
            rect = pygame.Rect(x*x_size, y*y_size,x_size,y_size)
            # pygame.draw.rect(backgroundimg,(200,200,200),rect,1)  # to define grid according to the walls coordinates
# # defines the position of final square # #
def final_score(x,y):
    final_score = font.render(' Your Score: ' + str(score),True,(255,255,255))
    screen.blit(final_score,(x,y))
# # converts coordinates in pixels to grid coordinates # #
def gridcoord(x,y):
    return((x-30)//x_size, (y-30)//y_size)                 # # 30 = wbuff/2 = hbuff/2 # #
# # converts grid coordinates to coordinates in pixels
def pixcoord(x,y):
    return((x*x_size)+30, (y*y_size)+30)
# # defines the position of the player # #
def player(x,y):
    screen.blit(playerimg,(x,y))
# # function that checks if the player collided with any of the walls # #
def check(x,y):
    a,b = gridcoord(x,y)
    for wall in walls[1:len(walls)]:
        if vector(a,b) == wall:
            return False
    return True
# # defines the position of the four enemies # #
def enemy1(x,y):
    a,b = pixcoord(x,y)
    screen.blit(enemy1img,(a,b))
def enemy2(x,y):
    a, b = pixcoord(x, y)
    screen.blit(enemy2img,(a,b))
def enemy3(x,y):
    a, b = pixcoord(x, y)
    screen.blit(enemy3img,(a,b))
def enemy4(x,y):
    a, b = pixcoord(x, y)
    screen.blit(enemy4img, (a, b))
# # defines the position of bonus cherry # #
def bonus(x,y):
    screen.blit(bonusimg,(x,y))
# # to define the position of game over image # #
def game_over():
    screen.blit(gameover,(0,0))

# # # # we will need to open and use some data from other files that we will store in the same directory # # # #
# # # the walls file represents the grid coordinates in terms of some characters # # #
# # # where the character is 0 , it will remain empty # # #
# # open walls text file : it will create a wall(boundary) whenever the grid coordinates are W, will create a coin whenever the coordinates are C(refer walls.txt) # #
with open('walls.txt','r') as file:
    for yindex,line in enumerate(file):
        for xindex,char in enumerate(line):
            if char == 'W':
                walls.append(vector(xindex,yindex))
            elif char == 'C':
                coins.append(vector(xindex,yindex))
            elif char == '2' or '3' or '4':
                enemies.append(vector(xindex,yindex))       # # to define initial positions of enemies # #
# # open and read highscore text file : it helps in storing and displaying the high score # #
with open('highscore.txt','r') as doc:
    hsc = doc.read()

# # setting up background music that plays on loop # #
mixer.music.load('pacman_beginning.wav')
mixer.music.play(-1)

running = True                              # # # assigning some variable a True value # # #

while running:
    screen.fill((0,0,0))                    # # # fills up the screen with black color # # #
    screen.blit(backgroundimg,(wbuff//2,hbuff//2))    # displaying the background image #
    a, b = gridcoord(player_x, player_y)              # converting pixel coordinates of players into grid coordinates #
    bonus(300,310)
    grid()                                            # calling the grid function #

    # # # appending coordinates of player, to lists l1,l2,l3,l4 if the adjacent grids of the current player position are walls # # #
    for wall in walls:
        if vector(a+1,b) == wall:                  # the vector function helps us to directly compare the grid coordinates to wall coordinates(as wall is also a vector) #
            l1.append(vector(a,b))
        elif vector(a-1,b) == wall:
            l2.append(vector(a,b))
        elif vector(a,b+1) == wall:
            l3.append(vector(a,b))
        elif vector(a,b-1) == wall:
            l4.append(vector(a,b))
    # # # determining player movements with the help of keyboard keys # # #
    for event in pygame.event.get():
        xforward = True
        xbackward = True
        yupwards = True
        ydownwards = True
        if event.type == pygame.QUIT:
            running = False
        if check(player_x,player_y) is True:
            if event.type == pygame.KEYDOWN:
                if xforward is True:
                    if event.key == pygame.K_RIGHT:
                        if vector(gridcoord(player_x,player_y)) not in l1:          # # # makes sure that when we press the right key,
                            player_x_change = x_size*(0.2)                          # # # the player does not hit the wall.
                        elif vector(gridcoord(player_x,player_y)) in l1:            # # # If the player is in l1,and we press the right key,it will hit the wall.
                            xforward = False                                        # # # Hence, ensuring it does not hit wall.
                            player_x_change = 0
                            break
                if xbackward is True:
                    if event.key == pygame.K_LEFT:
                        if vector(gridcoord(player_x, player_y)) not in l2:         # # # makes sure that when we press the left key,
                            player_x_change = -x_size*(0.2)                         # # # the player does not hit the wall.
                        elif vector(gridcoord(player_x, player_y)) in l2:           # # # If the player is in l2,and we press the left key,it will hit the wall.
                            xbackward = False                                       # # # Hence, ensuring it does not hit wall.
                            player_x_change = 0
                            break
                if yupwards is True:
                    if event.key == pygame.K_UP:
                        if vector(gridcoord(player_x, player_y)) not in l4:          # # # makes sure that when we press the up key,
                            player_y_change = -y_size*(0.2)                          # # # the player does not hit the wall.
                        elif vector(gridcoord(player_x, player_y)) in l4:            # # # If the player is in l4,and we press the up key, it will hit the wall.
                            yupwards = False                                         # # # Hence, ensuring it does not hit wall.
                            player_y_change = 0
                            break
                if ydownwards is True:
                    if event.key == pygame.K_DOWN:
                        if vector(gridcoord(player_x, player_y)) not in l3:          # # # makes sure that when we press the down key,
                            player_y_change = y_size*(0.2)                           # # # the player does not hit the wall.
                        elif vector(gridcoord(player_x, player_y)) in l3:            # # # If the player is in l3,and we press the down key, it will hit the wall.
                            ydownwards = False                                       # # # Hence, ensuring it does not hit the wall.
                            player_y_change = 0
                            break
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    player_x_change = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    player_y_change = 0

    # # # setting up boundaries for the enemies # # #
    if enemy4_y<=1:
        enemy4_y = 1
        enemy4_ychange = 1.5
        enemy4_xchange = -0.2
    elif enemy4_y>=30:
        enemy4_y = 30
        enemy4_ychange = -1.5
        enemy4_xchange = 0.2
    # # boundary for enemy 2 # #
    if enemy2_y<=1:
        enemy2_y = 1
        enemy2_ychange = 0.6
        enemy2_xchange = -0.1
    elif enemy2_y>=30:
        enemy2_y = 30
        enemy2_ychange = -0.6
        enemy2_xchange = 0.1
    # # boundary for enemy 1 # #
    if enemy1_x>= 28:
        enemy1_x = 28
        enemy1_xchange = -0.6
        enemy1_ychange = 0.1
    elif enemy1_x <= 1:
        enemy1_x = 1
        enemy1_xchange = 0.6
        enemy1_ychange = -0.1
    # # random positions of enemy 3 # #
    enemy3_x = random.randint(13,17)
    enemy3_y = random.randint(14,16)

    # # # calculating the final positions of the player and the enemies # # #
    player_x += player_x_change
    player_y += player_y_change
    enemy1_x += enemy1_xchange
    enemy1_y += enemy1_ychange
    enemy2_y += enemy2_ychange
    enemy2_x += enemy2_xchange
    enemy4_y += enemy4_ychange
    enemy4_x += enemy4_xchange

    # # # setting up boundaries for our player # # #
    if player_x >= 550:
        player_x_change = 0
        player_x = 550
    elif player_x <= 50:
        player_y_change = 0
        player_x = 50
    if player_y <= 50:
        player_y_change = 0
        player_y = 50
    elif player_y >= 620:
        player_y_change = 0
        player_y = 620

    # # # making and displaying coins by drawing circles # # #
    for coin in coins:
        pygame.draw.circle(backgroundimg,(255,255,0),((coin.x*20)+10,(coin.y*20)+10),3)
        if vector(gridcoord(int(player_x), int(player_y))) == coin:                         # # # if the vector of player positon equals that of a coin, then remove that
            l = len(coins)                                                                  # # # coin from the list and draw a black circle to show that the coin has been eaten.
            coins.remove(coin)
            mixer.music.load('pacman_chomp.wav')                                            # # # playing chomping sound when eating.
            mixer.music.play()
            mixer.music.load('pacman_beginning.wav')
            mixer.music.play(-1)
            m = len(coins)
            pygame.draw.circle(backgroundimg,(0,0,0),((coin.x*20)+10,(coin.y*20)+10),3)
            score += l-m                                                                    # # # updating score # # #

    if vector(gridcoord(int(player_x), int(player_y))) == vector(gridcoord(300,310)):       # # # if the player eats the bonus cherry, it gets a giant leap of 500 credits # # #
        score += 500
        mixer.music.load('pacman_eatfruit.wav')
        mixer.music.play()
        player_x = 55
        player_y = 53
    if score > int(hsc):                                                                    # # if the current score exceeds the highscore on highscore file, it gets printed on the screen.
        hsc = score

    high_score = font.render('HIGH SCORE: '+ str(hsc),True,(255,255,255))                   # # displaying high score # #
    screen.blit(high_score,(380,6))
    for wall in walls:
        pygame.draw.rect(backgroundimg, (250, 214, 165), (int((wall.x) * x_size), int((wall.y) * y_size), x_size, y_size))  # # solidifying the walls # #
    enemy1(enemy1_x,enemy1_y)
    enemy2(enemy2_x,enemy2_y)
    enemy3(enemy3_x,enemy3_y)
    enemy4(enemy4_x,enemy4_y)
    if (((a - enemy1_x) ** 2) + (b - enemy1_y) ** 2) ** (0.5) <= 1 or  (((a - enemy2_x) ** 2) + (b - enemy2_y) ** 2) ** (0.5) <= 1 or (((a - enemy3_x) ** 2) + (b - enemy3_y) ** 2) ** (0.5) <= 1:
        mixer.music.load('pacman_death.wav')                                        # # if the player hits the enemy, the game's over # #
        mixer.music.play()
        running = False                                     # # As soon as the player hits the enemy, running is changed to False and run is changed to True,
        run = True                                          # # which displays screen2,i.e,the screen of gameover.
        screen2 = pygame.display.set_mode((560,620))
        if run is True:
            from gameover import *
            os.system('gameover.py')
    player(player_x,player_y)                              # # final position of player # #
    final_score(6,6)                                       # # final score # #
    with open('highscore.txt', 'w') as doc:                # # We then need to update the highscore on the highscore file. # #
        doc.write(str(hsc))                                # doc.write() enables us to write on the doc.
    pygame.display.update()