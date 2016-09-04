import pygame
from pygame.locals import *

# initialize the game
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Load player images
player = pygame.image.load('dude.png')

# keep looping
while 1:
        # clear the screen before drawing it again
        sceen.fill(0)
        # draw screen elemtens
        screen.blit(player, (100, 100))
        pygame.display.flip()
        for event in pygame.event.get():
            # check if the event is the X button
            if event.type == pygame.QUIT:
                # if it is quit the game
                pygame.quit()
                exit(0)
