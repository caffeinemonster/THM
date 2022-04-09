import pygame
from classglobal import cglobal
from pygame.locals import *
oglobal = cglobal()

def main():
    while 1:
        if oglobal.debug == 1: print("Starting global object update.")
        oglobal.update()
        if oglobal.debug == 1: print("Starting global keyboard checks.")
        oglobal.checkkeys()
        if oglobal.debug == 1: print("Starting global draw routine.")
        oglobal.draw()
        
if __name__ == "__main__":
    if oglobal.debug == 1: print("Starting main program loop.")
    main()