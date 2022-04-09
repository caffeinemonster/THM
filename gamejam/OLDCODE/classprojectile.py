import pygame
from pygame.locals import *
class cprojectile(object):
    def __init__(self,x,y,radius,color,facing,rotation):
        pygame.sprite.Sprite.__init__(self)
        self.radius = radius
        self.color = color
        self.facing = facing
        self.rotation = rotation
        self.vel = 8 * facing
        self.speed = 8
        self.pos = pygame.Vector2(x,y)
        self.target = pygame.Vector2(x,y)
        self.imagepath = "sprites/bullet2.png"
        self.image = pygame.image.load(self.imagepath)
        self.life = 200
        
    def update(self, pcollection=""):
        self.life -= 1
        move = self.target - self.pos
        move_length = move.length()
        if move_length < self.speed:
            self.pos = self.target
            if not pcollection == "":
                pcollection.seedfireballs(self.pos[0], self.pos[1])
        elif move_length != 0:
            move.normalize_ip()
            move = move * self.speed
            self.pos += move
        
    def set_target(self, pos):
        self.target = pygame.Vector2(pos)
    
    def set_pos(self, pos):
        self.pos = pygame.Vector2(pos)

    def draw(self,surf):
        surf.blit(pygame.transform.rotate(self.image, self.rotation), (self.pos[0], self.pos[1]))
        