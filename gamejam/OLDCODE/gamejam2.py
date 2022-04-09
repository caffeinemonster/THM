import pygame
from classglobal import cglobal
from pygame.locals import *
oglobal = cglobal()

def main():
    while 1:
        oglobal.update()
        oglobal.checkkeys()
        oglobal.draw()
        
if __name__ == "__main__":
    main()