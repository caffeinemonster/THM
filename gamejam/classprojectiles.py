import pygame
from pygame.locals import *
from classsounds import csounds
from classprojectile import cprojectile
from classparticlecontroller import cparticlecontroller
class cprojectiles(object):
    def __init__(self):
        self.sfx = csounds()
        self.projectiles = []
        self.magsize = 120
        self.magcurrent = 120
        self.ammo = 5000
        self.ammotype = 0
        self.reloadtime = 100
        self.reload = self.reloadtime
        self.damage = 10
        self.delaytime = 1
        self.delay = self.delaytime
        self.imagepath = 'sprites/bullet1.png'
        self.image = pygame.image.load(self.imagepath)
        self.particles = cparticlecontroller()
        
    
    def seed(self,x,y,radius,colour,rotation,targpos):
        if self.reload <= 0:
            self.reload = 0
            
        if self.magcurrent == 0:
            return
            
        if self.ammo <= 0:
            self.ammo = 0
            return

        if not self.delay == 0:
            self.delay = self.delay - 1
            return
        
        if len(self.projectiles) < 300:
            self.ammo = self.ammo - 1
            self.magcurrent = self.magcurrent - 1
            obullet = cprojectile(x, y, 1, colour, 1, rotation)
            obullet.set_target(targpos)
            obullet.set_pos((x,y))
            obullet.imagepath = 'sprites/bullet1.png'
            obullet.image = self.image
            self.image = pygame.image.load(self.imagepath)
            self.projectiles.append(obullet)
            
            self.particles.seedemptyshell(x, y)
            
            self.sfx.fxshoot()
            self.delay = self.delaytime
            
    # def slide(self,slide,xy):
        # for p in self.projectiles:
            # p.pos[xy] += slide
            # p.target[xy] += slide 
        
    def draw(self, surf, pcollection = ""):
       
        if not self.delay == 0:
            self.delay = self.delay - 1
        
        if self.magcurrent == 0:
            self.reload = self.reload - 1
        
        if self.reload <= 0:
            self.reload = 0
        
        if self.reload <= 0:
            if self.ammo > 0:
                if self.magcurrent == 0:
                    if not self.ammo < self.magsize:
                        self.magcurrent = self.magsize
                        self.delay = self.reloadtime
                        self.sfx.fxreload()
                    else:
                        self.magcurrent = self.ammo
                        self.delay = self.reloadtime
                        self.sfx.fxreload()
                    self.reload = self.reloadtime
        
        for bullet in self.projectiles:
            bullet.update(pcollection)
            bullet.draw(surf)
            bremove = 0
            if bullet.target == bullet.pos:
                bremove = 1
            if bremove:
                self.projectiles.pop(self.projectiles.index(bullet))
                bullet = ""
                del(bullet)
        self.particles.draw(surf)
            
    def collide(self, targets):
        for bullet in self.projectiles:
            bremove = 0
            bulletcenter = (bullet.pos[0] + (bullet.image.get_width() / 2), bullet.pos[1] + (bullet.image.get_height() / 2))
            
            if bullet.life <= 0:
                bremove = 1

            for t in targets.targets:
                if bulletcenter[0] >= t.pos[0] and bulletcenter[0] <= t.pos[0] + t.image.get_width():
                    if bulletcenter[1] >= t.pos[1] and bulletcenter[1] <= t.pos[1] + t.image.get_height():
                        if t.damageable:
                            t.health = t.health - self.damage
                            t.active = 1
                            t.speed = 2
                        bremove = 1
                        self.sfx.fxhitwood()
                        
            if bullet.target == bullet.pos:
                bremove = 1
            if bremove:
                self.projectiles.pop(self.projectiles.index(bullet))
                bullet = ""
                del(bullet)