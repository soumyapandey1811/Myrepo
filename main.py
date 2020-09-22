import pygame
import random

#initialize the pygame
pygame.init()

#create the game screen
screen= pygame.display.set_mode((800,600))

#Title and icon
pygame.display.set_caption("Soumya's Space Invader")
icon=pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)
#......

# player aka spaceship
playerimg=pygame.image.load("spcship.png")
playerX=370
playerY=470
playerX_change=0

#enemy akaa monster
enemyimg=pygame.image.load("monsters.png")
enemyX=random.randint(0,800)
enemyY=random.randint(50,200)
enemyX_change=0

def player(x,y):
    screen.blit(playerimg,(x,y)) #blit method to draw image on screen

def enemy(x,y):
    screen.blit(enemyimg,(x,y)) 

#Game loop
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #if keystroke is pressed check whether its right or left using events
        if event.type == pygame.KEYDOWN: #keydown is pressing key
            if event.key==pygame.K_LEFT:
                playerX_change=-0.3
            if event.key==pygame.K_RIGHT:
                playerX_change=0.3
                
        if event.type == pygame.KEYUP:  
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0
                  

    #RGB---red green blue
    screen.fill((0,0,0))

    playerX+=playerX_change

    #creating boundaries for the spaceship
    if playerX<=0:
        playerX=0
    elif playerX>=736: #800-size of spaceship will be coonsidered as limit
        playerX=736
    #.............
    enemyX+=enemyX_change

    #creating boundaries for the enemy
    if enemyX<=0:
        enemyX=0
    elif enemyX>=736: #800-size of spaceship will be coonsidered as limit
        enemyX=736

    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()

