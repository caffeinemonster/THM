import pygame 
from pygame.locals import *
class ctext(object):  # particle group class
    def __init__(self):
        self.size = 21
        self.font = pygame.font.SysFont(None, self.size)
        self.font = pygame.font.Font("fonts/Futura.ttf", self.size)

    def draw(self, surf, mytext, xy, mycolour, alpha, size, align = ""):
        #self.font = pygame.font.SysFont(None, size)
        self.font = pygame.font.Font("fonts/Futura.ttf", size)
        img = self.font.render(mytext, True, mycolour)
        img.set_alpha(alpha)
        img.set_colorkey((0,0,0))
        if align == "center":
            surf.blit(img, (surf.get_width() / 2 - img.get_rect().width / 2, surf.get_height() / 2 - img.get_rect().height / 2))
            return
        if align == "centertop":
            surf.blit(img, (surf.get_width() / 2 - img.get_rect().width / 2, surf.get_height() / 10 - img.get_rect().height / 2))
            return
        if align == "centerbottom":
            surf.blit(img, (surf.get_width() / 2 - img.get_rect().width / 2, (surf.get_height() / 10 * 9) - img.get_rect().height / 2))
            return
        if align == "":
            surf.blit(img, (xy[0] , xy[1]))
            return