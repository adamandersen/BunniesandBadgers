# 1 import libarary
import pygame, sys, math
from pygame.locals import *

#import os

# 2 initialize the game
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
keys = [False, False, False, False]
playerpos = [200, 200]
acc = [0,0]
arrows = []

# 3 Load player images path to images:
# /home/adam/Documents/githubrepo/BunniesandBadgers/resources/images/
# change "/home/adam/Documents/githubrepo/" to the location of cloned code
player = pygame.image.load("/home/adam/Documents/githubrepo/BunniesandBadgers/resources/images/dude.png")
grass = pygame.image.load("/home/adam/Documents/githubrepo/BunniesandBadgers/resources/images/grass.png")
castle = pygame.image.load("/home/adam/Documents/githubrepo/BunniesandBadgers/resources/images/castle.png")
arrow = pygame.image.load("/home/adam/Documents/githubrepo/BunniesandBadgers/resources/images/bullet.png")

# 4 keep looping
while 1:
        # 5 clear the screen before drawing it again

        screen.fill(0)
        # 6 draw screen player elemtens
        for x in range(width/grass.get_width()+1):
            for y in range(height/grass.get_height()+1):
                screen.blit(grass,(x * 100, y * 100))
        screen.blit(castle,(0, 30))
        screen.blit(castle,(0, 135))
        screen.blit(castle,(0, 240))
        screen.blit(castle,(0, 345))

        # 6.1 set player position and rotation
        position = pygame.mouse.get_pos()
        angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
        playerrot = pygame.transform.rotate(player, 360-angle*57.29)
        playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
        screen.blit(playerrot, playerpos1)

        # 6.2 Draw arrows
        for bullet in arrows:
            index = 0
            velx = math.cos(bullet[0]) * 10
            vely = math.sin(bullet[0]) * 10
            bullet[1] += velx
            bullet[2] += vely
            if bullet[1] < -64 or bullet[1] > 640 or bullet[2] < -64 or bullet[2] > 480:
                arrows.pop(index)
            index += 1
            for projectile in arrows:
                arrow1 = pygame.transform.rotate(arrow, 360 - projectile[0] * 57.29)
                screen.blit(arrow1, (projectile[1], projectile[2]))

        # 7 update the screen
        pygame.display.flip()

        # 8 loop throug the events
        for event in pygame.event.get():
            # check if the event is the X button
            if event.type == pygame.QUIT:
                # if it is quit the game
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == K_w:
                    #print "UP True" # debug
                    keys[0] = True
                elif event.key == K_a:
                    #print "LEFT True" # debug
                    keys[1] = True
                elif event.key==K_s:
                    #print " True" # debug
                    keys[2] = True
                elif event.key == K_d:
                    #print "RIGHT True" #debug
                    keys[3] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    #print "UP False" # debug
                    keys[0] = False
                elif event.key == pygame.K_a:
                    #print "LEFT False" #debug
                    keys[1] = False
                elif event.key == pygame.K_s:
                    #print "DOWN False" #debug
                    keys[2] = False
                elif event.key == pygame.K_d:
                    #print "RIGHT False" # debug
                    keys[3] = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                acc[1] += 1
                arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])


        # 9 - Move player
            if keys[0]:
                playerpos[1]-=5
            elif keys[2]:
                playerpos[1]+=5
            if keys[1]:
                playerpos[0]-=5
            elif keys[3]:
                playerpos[0]+=5
            #print pygame.key.get_pressed() # debug
            #print pygame.key.get_focused() # debug
