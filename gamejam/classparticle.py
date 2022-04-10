import random
import pygame
from pygame.locals import *
class cparticle(object):  # particle class
    def __init__(self):
        # set init vars
        self.size = 0
        self.sizex = 0
        self.sizey = 0
        self.x = 0
        self.y = 0
        self.spawnx = 0
        self.spawny = 0 
        self.speedx = 10
        self.speedy = 10
        self.rotation = 0
        self.rotationdirection = 0 
        self.life = 0
        self.totallife = 0
        self.lifeoriginal = 0
        self.alive = 0
        self.respawns = 1
        self.colour = (255, 255, 255)
        self.gravityenable = 1
        self.gravity = [0, 1]
        self.imagepath = ""
        self.image = ""
        #self.gravitymax = [10,10]

    def seedrandom(self, xy): # seed random particle
        self.x = xy[0]  # set xloc
        self.y = xy[1]  # set yloc
        #self.colour = (random.randint(1, 200), random.randint(1, 200), random.randint(1, 200))
        self.rotation = random.randint(0,360)
        self.rotationdirection = random.randint(-10,10)
        self.seed(xy,(random.randint(1, 5), random.randint(5, 10)), random.randint(1, 16), (255, 255, 255), random.randint(10, 50))  # seed
        self.colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # set random colour

    def seed(self, xy, speed, isize, rgbcolour, ilife):  # seed particle
        self.life = random.randint(1, ilife)  # set life
        self.totallife = self.life  # set totlife
        self.lifeoriginal = self.life  # set totlife
        self.colour = rgbcolour  # set rgb colour
        self.size = random.randint(1, isize)  # random particle size
        self.sizex = self.size
        self.sizey = self.size
        self.x = xy[0]  # set xloc
        self.y = xy[1]  # set yloc
        self.spawnx = xy[0]  # set xloc
        self.spawny = xy[1]  # set yloc
        
        if random.randint(0, 1):  # random left/right
            self.speedx = random.randint(speed[0], speed[1])
        else:
            self.speedx = -random.randint(speed[0], speed[1])
            
        if random.randint(0, 1):  # random up/down
            self.speedy = random.randint(speed[0], speed[1])
        else:
            self.speedy = -random.randint(speed[0], speed[1])
            
        self.alive = 1  # make it live
        
    def kill(self):
        if self.life > 0:
            return 
            
        if self.respawns > 0:
            self.respawns = self.respawns - 1
            self.x = self.spawnx
            self.y = self.spawny
            self.life = self.lifeoriginal
            self.alive = 1
            self.totallife = self.lifeoriginal
            #print("respawning")
        else:
            self.life = 0
            self.alive = 0
            self.respawns = 0
            
    def getimage(self):
        if self.image == "":
            if not self.imagepath == "":
                self.image = pygame.image.load(self.imagepath)
                self.image.set_colorkey((0,0,0))
                self.sizex = self.image.get_width()
                self.sizey = self.image.get_height()
                self.image.set_alpha(128)
                self.randomisesize()
        return self.image
        
    def randomisesize(self):
        randx = random.randint(1,self.image.get_width())
        randy = randx
        self.image = pygame.transform.scale(self.image, (randx, randy))
        self.sizex = self.image.get_width()
        self.sizey = self.image.get_height()
    
        
    def move(self):  # move the particle
        if self.life > 0:
            GRAVX = 0
            GRAVY = 0
            if self.gravityenable:
                GRAVX = self.gravity[0] * (self.totallife - self.life) 
                GRAVY = self.gravity[1] * (self.totallife - self.life)
            self.x = self.x + self.speedx + GRAVX
            self.y = self.y + self.speedy + GRAVY
            self.life -= 1
        else:
            self.alive = 0
            self.respawns = self.respawns - 1
