import pygame, sys, random 
from pygame.locals import *
from classraycast import craycast

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    GCLOCK = pygame.time.Clock()
    rayc = craycast(DISPLAYSURF)
    while 1:
        rayc.checkkeys()
        rayc.draw(DISPLAYSURF)
        pygame.display.flip()
        pygame.display.update()
        GCLOCK.tick(60)
main()

