import pygame, sys, time, random
from pygame.locals import *
from classgrid import cgrid

pygame.init()
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
ogrid = cgrid(10,10,DISPLAYSURF.get_width(), DISPLAYSURF.get_height()) # create new grid class 
pygame.display.set_caption('GRIDTEST!') # set window caption
ogrid.create() # create a new grid
update = 0 # variable to time updates
while True: # main game loop
    DISPLAYSURF.fill((0,0,0))
    
    ogrid.drawgrid(DISPLAYSURF) # draw grid
    update += 1 # increase update timer
    
    if update >= 10: # check update timer
        update = 0 # reset timer
        ogrid = cgrid(32,18,DISPLAYSURF.get_width(), DISPLAYSURF.get_height()) # create new grid class
        ogrid.create() # generate new grid
        
    for event in pygame.event.get(): # handle keyboard events
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.mixer.quit()
                pygame.quit()
                sys.exit()
    pygame.display.flip() # flip display buffer 
    pygame.display.update() # update display 