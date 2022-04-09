import pygame, math
from classprojectiles import cprojectiles
from classtext import ctext




from pygame.locals import *
class cplayer(object):  # particle group class
    def __init__(self):
        # initialise player class
        self.lives = 3
        self.health = 100
        self.totalhealth = self.health
        self.speed = 2
        self.rotation = 0
        self.imagepath = "sprites/player2.png"
        self.image = pygame.image.load(self.imagepath)
        self.imageoriginal = self.image
        self.pos = pygame.Vector2(0, 0)
        self.poslast = pygame.Vector2(self.pos)
        self.validpos = []
        self.target = pygame.Vector2(self.pos)
        self.updatecenter() #pygame.Vector2((self.pos[0] - (self.image.get_width() / 2), self.pos[1] - (self.image.get_height() / 2)))
        self.set_target(pygame.Vector2(self.pos))
        self.updatecenter()
        self.projectiles = cprojectiles()
        self.otext = ctext()

    def setup(self, surf, offset):
        self.pos[0] = (surf.get_width() / 2) + offset[0]
        self.pos[1] = (surf.get_height() / 2) + offset[1]
        self.pos = pygame.Vector2(self.pos)
        self.poslast = self.pos
        self.target = self.pos
        self.updatecenter()
    
    def slide(self,slide,xy):
        self.poslast[xy] += -slide
        self.pos[xy] += -slide
        self.target[xy] += -slide
        self.updatecenter()
    
    def set_target(self, pos):
        self.target = pygame.Vector2(pos)
    
    def update(self, offset):
        if self.health > self.totalhealth:
            self.health = self.totalhealth
    
        if self.health < 0: 
            self.health = 0
        if self.health == 0:
            self.lives -= 1
            self.health = self.totalhealth
        self.speed = 5
                 
        move = self.target - self.pos
        move_length = move.length()
        if move_length < self.speed:
            self.target = self.pos
            self.speed = 0
        elif move_length != 0:
            move.normalize_ip()
            move = move * self.speed
            self.pos += move
            
        
        self.updatecenter()
        #self.updateposlast()
    def checkkeys(self, event):
        #for event in pygame.event.get():
        bshoot = 0 # ADD PROJECTILE?
        # CHECK EVENT AND BUTTON QUEUE 
        # CHECK MOUSE EVENTS
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1: # left click
                self.set_target(pygame.mouse.get_pos() + pygame.Vector2(self.image.get_width() / 2, self.image.get_width() / 2))
            if event.button == 3: # right click
                bshoot = 1
        # CHECK KEYDOWN EVENTS 
        elif event.type == KEYDOWN:               
            if event.key == K_SPACE:
                bshoot = 1
            if event.key == K_r:
                # RELOAD MAG (PLAYER PROJECTILES)
                if not self.projectiles.magcurrent == self.projectiles.magsize:
                    self.projectiles.reload = self.projectiles.reloadtime
                    self.projectiles.ammo = self.projectiles.ammo
                    self.projectiles.magcurrent = 0

        # CHECK KEYPRESS EVENTS
        keys = pygame.key.get_pressed()
        if keys[K_SPACE]:
            bshoot = 1
            
        # ADD PROJECTILE TO ARRAY?
        if bshoot: self.projectiles.seed(self.playercenter[0],self.playercenter[1],1,(255,255,255),self.rotation, pygame.mouse.get_pos())
            
    def updateposlast(self):
        self.poslast = pygame.Vector2(self.pos)
        
    def updatecenter(self):
        self.playercenter = pygame.Vector2((self.pos[0] - (self.image.get_width() / 2), self.pos[1] - (self.image.get_height() / 2)))
        
    def draw(self, surf):
        
        # DRAW PLAYER PROJECTILES
        self.projectiles.draw(surf)
    
        # CALCULATE PLAYER ROTATION
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.playercenter[0], mouse_y - self.playercenter[1]
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        self.rotation = angle
        
        # CALCULATE HEALTH BAR 
        healthbar = int(float(float(self.image.get_width() / self.totalhealth) * self.health))
        G = 255 / self.totalhealth * (self.health)
        R = 255 - 255 / self.totalhealth * (self.health)
        if R < 0:R = 0
        if R > 255:R = 255
        if G < 0:G = 0
        if G > 255:G = 255

        # DRAW HEALTH BAR 
        pygame.draw.line(surf,(int(R),int(G),0),(self.pos[0]-self.image.get_width(), self.pos[1] + self.image.get_height()/2),(self.pos[0] + healthbar - (self.image.get_width()), self.pos[1] + self.image.get_height()/2))
        
        # DRAW PLAYER IMAGE 
        surf.blit(pygame.transform.rotate(self.image, self.rotation), (self.playercenter[0] - self.image.get_width()/2, self.playercenter[1] - self.image.get_height()/2))
        
        # DRAW DEBUG DATA
        pygame.draw.circle(surf, (000,222,000), self.playercenter, 4) # RENDER DEBUG IMAGES
        pygame.draw.circle(surf, (222,000,000), self.poslast, 4) # RENDER DEBUG IMAGES
        pygame.draw.circle(surf, (000,000,222), self.target, 4) # RENDER DEBUG IMAGES
        pygame.draw.circle(surf, (000,255,000), self.pos, 4) # RENDER DEBUG IMAGES
        
        #def draw(self, surf, mytext, xy, mycolour, alpha, size, align = ""):
        
        self.otext.draw(surf, "POS:" + str(self.pos), (self.pos[0], self.pos[1]+20),(255,0,0),255, 18, "")
        
        
        
        