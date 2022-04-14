import pygame 
from pygame.locals import *
class ctext(object):  # particle group class
    def __init__(self, surf):
        self.size = 32
        self.font = pygame.font.Font("fonts/Futura.ttf", self.size)
        self.surf = surf
        self.alpha = 255
        self.colourkey = (0,0,0)
    def draw(self, xy, colour, text, align = ""):
        img = self.font.render(text, True, colour)
        img.set_alpha(self.alpha)
        img.set_colorkey(self.colourkey)
        if align == "center":
            self.surf.blit(img, (self.surf.get_width() / 2 - img.get_rect().width / 2, self.surf.get_height() / 2 - img.get_rect().height / 2))
            return
        if align == "centertop":
            self.surf.blit(img, (self.surf.get_width() / 2 - img.get_rect().width / 2, self.surf.get_height() / 10 - img.get_rect().height / 2))
            return
        if align == "centerbottom": 
            self.surf.blit(img, (self.surf.get_width() / 2 - img.get_rect().width / 2, (self.surf.get_height() / 10 * 9) - img.get_rect().height / 2))
            return
        if align == "": # no align data blit to xy
            self.surf.blit(img, (xy[0] , xy[1]))
            return
            