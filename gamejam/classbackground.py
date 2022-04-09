import pygame
from pygame.locals import *
class cbackground(object):
    def __init__(self):
        self.image = pygame.image.load("tiles/256grass.png")
        self.background = ""
        
    def generateimage(self, surf, id = ""):
        if id == "":
            if self.background == "":
                self.background = pygame.Surface((surf.get_width(), surf.get_height()))
                for x in range (0, int(surf.get_width() / self.image.get_width())+1):
                    for y in range (0,  int(surf.get_height() / self.image.get_height())+1):
                        self.image.set_alpha(64)
                        self.background.blit(self.image, (x*self.image.get_width(), y*self.image.get_height()))
            return 
        if id == 1: # background style 
            return 
        
        
    def draw(self, surf):
        self.generateimage(surf)
        if not self.background == "":
            surf.blit(self.background, (0, 0))