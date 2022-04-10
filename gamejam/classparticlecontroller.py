import pygame
from pygame.locals import *
import random
from classparticle import cparticle
from classparticles import cparticles

class cparticlecontroller(object):  # particle group class
    def __init__(self):
        self.collection = []
       
    def seedfireballs(self, x, y):
        for icount in range(1, 2):
            parts = cparticles()
            parts.imagepath = "sprites/fireball.png"
            parts.detectbounds = 1
            parts.draworder = 0
            if icount == 1:
                parts.draworder = 0
                #def seed(self, x, y, speed, life, amount, rgbcolour, size):
                parts.seed(x, y, random.randint(3, 7), random.randint(1, 15), random.randint(1, 15), (255,255,255), 10) #cloud
                parts.detectbounds = 0
                for p in parts.particles:
                    p.gravity = [0,-1]
                    p.speedx = random.randint(-3,3)
                    if p.speedy < 0:
                        p.speedy = +p.speedy*2 
                    irgb = random.randint(0, 255)
                    p.colour = (irgb, irgb, irgb)
            if icount > 0:
                #    def seedrandom(self, xy, amount, life, size): 
                parts.seedrandom((x, y), 3, 5, 1) # SPARKS
                parts.draworder = 2
            self.collection.insert(0, parts)
            
    def seedemptyshell(self, x, y):
        #for icount in range(1, 2):
        parts = cparticles()
        parts.detectbounds = 1
        parts.draworder = 1
        parts.imagepath = "sprites/shell.png"
        #def seedrandom(self, xy, amount, life, size):
        parts.seedrandom((x, y), 1, 2, 2)
        for p in parts.particles:
            p.gravity = [0,0]
        self.collection.insert(0, parts)
        
    def seedstars(self, x, y):
        #for icount in range(1, 2):
        parts = cparticles()
        parts.detectbounds = 1
        parts.draworder = 1
        parts.imagepath = "sprites/star.png"
        #def seedrandom(self, xy, amount, life, size):
        parts.seedrandom((x, y), 3, 2, 1)
        for p in parts.particles:
            p.gravity = [0,0]
        self.collection.insert(0, parts)
    
    def seedfiresmall(self, x, y):
        #for icount in range(1, 2):
        parts = cparticles()
        parts.detectbounds = 1
        parts.draworder = 1
        parts.imagepath = "sprites/fireball.png"
        #def seedrandom(self, xy, amount, life, size):
        parts.seedrandom((x, y), 1, 3, 3)
        for p in parts.particles:
            p.respawns = 10
            p.gravity = [0,0]
        self.collection.insert(0, parts)
    
    def seedrain(self, surf):
        parts1 = cparticles()
        parts2 = cparticles()
        parts3 = cparticles()
        parts4 = cparticles()
        parts1.imagepath = "sprites/water1.png"
        parts2.imagepath = "sprites/water2.png"
        parts3.imagepath = "sprites/water3.png"
        parts4.imagepath = "sprites/water4.png"
        parts1.draworder = 0
        parts2.draworder = 0
        parts3.draworder = 0
        parts4.draworder = 0
        
        x = random.randint(0, surf.get_width())
        y = random.randint(0, surf.get_height() / 30)
        
        parts1.seedrandom((x, y), random.randint(1, 20), random.randint(1, 10), random.randint(10, 10))
        parts2.seedrandom((x, y), random.randint(1, 20), random.randint(1, 10), random.randint(10, 10))
        parts3.seedrandom((x, y), random.randint(1, 10), random.randint(1, 50), random.randint(10, 500))
        parts4.seedrandom((x, y), random.randint(1, 10), random.randint(1, 50), random.randint(10, 500))
        self.collection.insert(0, parts1)
        self.collection.insert(0, parts2)
        self.collection.insert(0, parts3)
        self.collection.insert(0, parts4)
        
    def seedsnow(self, surf):
        parts1 = cparticles()
        parts2 = cparticles()
        parts3 = cparticles()
        parts4 = cparticles()
        parts1.imagepath = "sprites/snowflake1.png"
        parts2.imagepath = "sprites/snowflake2.png"
        parts3.imagepath = "sprites/snowflake1.png"
        parts4.imagepath = "sprites/snowflake2.png"
        parts1.draworder = 0
        parts2.draworder = 0
        parts3.draworder = 0
        parts4.draworder = 0
        parts1.detectbounds = 0
        parts1.detectbounds = 0
        parts1.detectbounds = 0
        parts1.detectbounds = 0
        x = random.randint(0, surf.get_width())
        y = random.randint(0, surf.get_height() / 30)
        parts1.seedrandom((x, y), random.randint(1, 20), random.randint(100, 500), random.randint(10, 15))
        x = random.randint(0, surf.get_width())
        y = random.randint(0, surf.get_height() / 30)
        parts2.seedrandom((x, y), random.randint(1, 20), random.randint(100, 100), random.randint(10, 15))
        x = random.randint(0, surf.get_width())
        y = random.randint(0, surf.get_height() / 30)
        parts3.seedrandom((x, y), random.randint(1, 20), random.randint(100, 250), random.randint(10, 15))
        x = random.randint(0, surf.get_width())
        y = random.randint(0, surf.get_height() / 30)
        parts4.seedrandom((x, y), random.randint(1, 20), random.randint(100, 500), random.randint(10, 15))
        self.collection.insert(0, parts1)
        self.collection.insert(0, parts2)
        self.collection.insert(0, parts3)
        self.collection.insert(0, parts4)
        for p in self.collection:
            p.detectbounds = 0
    
    def seedblood(self, xy):
        #for icount in range(1, 4):
        parts = cparticles()
        parts.detectbounds = 1
        parts.draworder = 1
        #def seed(self, x, y, speed, life, amount, rgbcolour, size):
        ispeed = 10
        ilife = random.randint(30, 200)
        iamount = 2
        ocolour = (random.randint(128,255),0,0)
        isize = random.randint(4, 10)
        parts.seed(xy[0], xy[1], ispeed, ilife, iamount, ocolour, isize)
        #def seed(self,x,y,radius,colour,rotation,targpos):
        #def seed(self,x,y,radius,colour,rotation,targpos):
        
        for p in parts.particles:
            p.colour = (random.randint(128,255),0,0)
            p.speedx = 0
            p.speedy = 0
            #p.gravity = [int([-1,0,1][random.randrange(3)]),int([-1,0,1][random.randrange(3)])]
            p.gravity = [0,0]
        self.collection.insert(0, parts)            
        
    def seedcloudmagic(self, xy):
        for icount in range(1, 4):
            parts = cparticles()
            parts.detectbounds = 1
            parts.draworder = 1
            parts.seed(xy[0], xy[1], random.randint(1, 100), random.randint(30, 100), random.randint(10, 30), (0,0,0), random.randint(10, 20))
            for p in parts.particles:
                p.colour = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
                p.gravity = [0,0]
            self.collection.insert(0, parts)
    
    def seedcloud(self, surf):
        for x in range(1, 50):
            parts = cparticles()
            parts.detectbounds = 0
            parts.draworder = 1
            x = random.randint(0, surf.get_width())
            y = random.randint(0, surf.get_height() / 20)
            irgb = random.randint(0, 255)
            #def seed(self, x, y, speed, life, amount, rgbcolour, size):
            parts.seed(x, y, random.randint(10, 20), random.randint(10, 70), random.randint(1, 10), (irgb,irgb,irgb), random.randint(80,150))
            for p in parts.particles:
                irgb = random.randint(200, 255)
                p.colour = (irgb,irgb,irgb)
                p.gravity = [0,0]
            self.collection.insert(0, parts)
    
    def killold(self):
        #self.collection.insert(0, parts)
        for p in self.collection:
            #print(len(p.particles))
            #print("Particle in collection:" + str(len(p.particles)))
            if len(p.particles) == 0:
                self.collection.pop(self.collection.index(p))
                p = ""
                del(p)
                
    def draw(self, surf):
        self.killold()
        for x in range(0,9):
            for p in self.collection:
                if len(p.particles) == 0:
                    self.collection.remove(p)
                    break
                if p.draworder == x:
                    p.draw(surf)