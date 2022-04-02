import pygame
from pygame.locals import *
from classsound import csound
from classprojectile import cprojectile
class cprojectiles(object):
    def __init__(self,x,y,radius,color,facing,rotation):
        sfx = csound()
        self.projectiles = []
        self.projectilesmax = 100
        self.timereload = 10
        self.damage = 10
        self.ammotype = 0
        
    def seed(self,x,y,radius,colour,facing,rotation,targpos,pcollection):
        if len(bullets) < self.projectilesmax:
            obullet = cprojectile(x, y, 1, colour, 1, oplayer.rotation)
            obullet.set_target(targpos)
            obullet.set_pos(x,y)
            self.projectiles.append(obullet)
            pcollection.seedemptyshell(x, y)
            sfx.fxshoot()
            
    def draw(self, surf):
        for bullet in self.projectiles:
            bullet.update(pcollection)
            bullet.draw(DISPLAYSURF)
            
    def collide(targets,pcollection):
        for bullet in self.projectiles:
            bremove = 0
            bulletcenter = (bullet.pos[0] + (bullet.image.get_width() / 2), bullet.pos[1] + (bullet.image.get_height() / 2))
            if bulletcenter[0] < 0 or bulletcenter[0] > DISPLAYSURF.get_width():
                bremove = 1
            if bulletcenter[1] < 0 or bulletcenter[1] > DISPLAYSURF.get_height():
                bremove = 1
            for targ in targets:
                if bulletcenter[0] >= targ.pos[0] and bulletcenter[0] <= targ.pos[0] + targ.image.get_width():
                    if bulletcenter[1] >= targ.pos[1] and bulletcenter[1] <= targ.pos[1] + targ.image.get_height():
                        targ.health = targ.health - 1
                        pcollection.seedfireballs(bulletcenter[0], bulletcenter[1])
                        pcollection.seedstars(bulletcenter[0], bulletcenter[1])
                        bremove = 1
                        sfx.fxhitwood()
            if bremove:
                bullets.pop(bullets.index(bullet))
                bullet = ""
                del(bullet)