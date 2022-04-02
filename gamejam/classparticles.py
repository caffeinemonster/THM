import pygame
from pygame.locals import *
from classparticle import cparticle
from classtext import ctext
import random



class cparticles(object):  # particle group class
    def __init__(self):
        self.detectbounds = 1
        self.particles = []
        self.imagepath = ""
        self.draworder = 9
        self.x = 0
        self.y = 0
        self.otext = ctext()

    def seed(self, x, y, speed, life, amount, rgbcolour, size):
        self.x = x
        self.y = y
        self.killold()  # remove old particles
        for i in range(0, amount):  # loop for amount
            part = cparticle()  # create new particle
            # seed(self, xy, speed, isize, rgbcolour, ilife) # reference
            # part.seedrandom((x, y))  # seed particle at xy
            part.seed((x, y), (1, speed), size, rgbcolour, life)
            self.particles.insert(0, part)

    def seedrandom(self, xy, amount, life, size):  # seed random amount of particles at xy
        #print(xy)
        self.x = xy[0]
        self.y = xy[1]
        
        #self.killold()  # remove old particles
        for i in range(0, amount):  # loop for amount
            part = cparticle()  # create a particle
            part.life = random.randint(1, life)
            part.size = random.randint(1, size)
            part.seedrandom(xy)  # seed particle at xy location
            part.sizex = part.size 
            part.sizey = part.size
            #print(self.imagepath)
            if self.imagepath == "":
                part.imagepath = "sprites/fireball.png"
            else:
                part.imagepath = self.imagepath
            #part.gravity = [random.randint(-1,1),random.randint(-1,1)]
            self.particles.insert(0, part)  # add particle to array

    def move(self):  # moves the particles
        for p in self.particles:  # for all particles
            p.move()  # move the particle

    def killold(self):  # removes old particles
        for p in self.particles:  # for all particles
            #if p.alive == 0:  # if they are dead or less than dead
            if p.life <= 0:
                self.particles.remove(self.particles.index(p))
                del(p)
        #if len(self.particles) == 0:
        #    print("emitter empty")
                
    def collisions(self, surf):
        #self.killold()
        for p in self.particles:
            if self.detectbounds:  # if bound detection is enabled
                # check X bounds
                if p.x > surf.get_width() - p.sizex: # has particle hit right wall
                    if p.speedx > 0: # if particle is moving right
                        p.speedx = -p.speedx # invert particle direction
                    p.x = surf.get_width() - p.sizex # set particle to be on screen 
                    p.totallife = p.life +2 
                    
                if p.x < 0: # has particle hit left wall 
                    if p.speedx < 0:
                        p.speedx = -p.speedx
                    p.x = p.sizex
                    p.totallife = p.life +2
                
                # check Y bounds
                if p.y > surf.get_height() - p.sizey: # has particle hit bottom
                    if p.speedy > 0:
                        p.speedy = -p.speedy
                    p.y = surf.get_height() - p.sizey
                    p.totallife = p.life +2
                    
                if p.y < 0: # has particle hit top
                    if p.speedy < 0:
                        p.speedy = -p.speedy
                    p.totallife = p.life +2
            
            #if not self.detectbounds:
            if p.y < -p.sizey or p.y > surf.get_height() + p.sizey or p.x < -p.sizex or p.x > surf.get_width() + p.sizex:
                p.kill()
                self.particles.pop(self.particles.index(p))
                del(p)
                return
 
    def draw(self, surf):
        self.move()
        self.collisions(surf)
        #self.otext.draw(surf, "(Particle emitter) " + str(len(self.particles)), (self.x, self.y), (255,255,255), 255, 21,"")
        for p in self.particles:  # draw particles
            if p.alive == 1:  # if the particle is alive
                image = p.getimage()
                if not image == "":
                    image.set_alpha((255 / p.totallife) * p.life)
                    surf.blit(pygame.transform.rotate(image, p.rotation), (p.x, p.y))
                else:
                    surface = pygame.Surface((p.sizex, p.sizey))
                    surface.set_colorkey((0,0,0))
                    surface.set_alpha((255 / p.totallife) * p.life)
                    pygame.draw.circle(surface, p.colour, (p.sizex/2, p.sizey/2), p.size / 2)
                    surf.blit(surface, (p.x -p.sizex / 2, p.y - p.sizey / 2))
                #def draw(self, surf, mytext, xy, mycolour, alpha, size, align):
                
                p.rotation = p.rotation + p.rotationdirection
                if p.rotation > 360:
                    p.rotation = 0
                if p.rotation < 0:
                    p.rotation = 360
            else:
                p.kill()
                self.particles.pop(self.particles.index(p))
                del(p)
                return
    