import pygame, random, math
from pygame.locals import *
from classsounds import csounds
from classparticlecontroller import cparticlecontroller 
#from classpathfinder import cpathfinder
#from classgrid import cgrid

class ctarget(object):  # particle group class
    def __init__(self, pos, imagepath, health, damageable, targettype):
        self.pos = pygame.Vector2(pos)
        self.imagepath = imagepath
        self.image = ""
        self.health = health #object health
        self.totalhealth = health #total health 
        self.damageable = damageable # is object damageable
        self.drawhealth = 1 # draw the health bar
        self.followplayer = 1
        self.active = 0
        self.speed = random.randint(0,5)
        self.speedmax = self.speed
        self.target = pygame.Vector2(self.pos) # targets target movement position
        self.targettype = targettype #int(random.randint(0,4)) # target type  
        self.timer = random.randint(100,400)
        self.timertotal = self.timer
        self.getimage() # returns and loads target image
        self.rotation = 0 #random.randint(0,360) # target rotation
        self.playereffect = random.randint(25,50)
        self.particles = cparticlecontroller()

    def getimage(self):
        if self.image == "":
            if not self.imagepath == "":
                self.image = pygame.image.load(self.imagepath)
                #print(self.imagepath)
        return self.image
        
    def draw(self, surf):
        if not self.image == "": # check the sprite exists 
            self.timer -= 1 # decrease target reset timer 
            if self.timer <= 0: # if timer expires
                self.timer = 0 # ensure timer is set to 0
                
            if self.targettype == 4: # ENEMY TURN TO TARGET DIRECTION
                if self.pos == self.target:
                    if self.timer == 0:
                        self.rotation = random.randint(0,360)
                else:                
                    player_x, player_y = pygame.Vector2(self.target)
                    rel_x, rel_y = pygame.Vector2(self.pos) - pygame.Vector2(self.target)
                    angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
                    self.rotation = angle
                
                
                
            surf.blit(pygame.transform.rotate(self.image, self.rotation), (self.pos[0], self.pos[1]))
            healthbar = int(float(float(self.image.get_width() / self.totalhealth) * self.health))
            G = 255 / self.totalhealth * self.health
            R = 255 - (255 / self.totalhealth * self.health)
            if R < 0 : R = 0
            if R > 255 : R = 255
            if G < 0 : G = 0
            if G > 255 : G = 255
            C = (int(R),int(G),0)
            if self.damageable:
                if self.drawhealth == 1:
                    pygame.draw.line(surf,C,(self.pos[0], self.pos[1] + self.image.get_height()),(self.pos[0] + healthbar, self.pos[1] + self.image.get_height()))
        self.particles.draw(surf)
            
    # def collide(self, level, player, surf):
        # bremove = 0
        # for t in level.targets:
            # if player.playercenter[0] >= t.pos[0]+level.offset[0] and player.playercenter[0] <= t.pos[0]+level.offset[0] + t.image.get_width():
                # if player.playercenter[1] >= t.pos[1]+level.offset[1] and player.playercenter[1] <= t.pos[1]+level.offset[1] + t.image.get_height():
                    # if t.damageable:                            
                        # # pcollection.seedstars(player.playercenter[0], player.playercenter[1])
                        # bremove = 1
                        # # self.sfx.fxeat()
                    # else:
                        # player.pos = player.poslast
                        # player.tet = player.poslast
                        # player.speed = 0
                    
                    # if int(t.targettype) == 0:
                        # self.playereffect = self.playereffect #do nothing
                    
                    # if int(t.targettype) == 1:    
                        # bremove = 1
                        # t.health = 0
                        # player.health += t.playereffect
                    # if int(t.targettype) == 2:
                        # bremove = 1
                        # t.health = 0
                        # player.projectiles.ammo += t.playereffect
                    # if int(t.targettype) == 3:
                        # bremove = 1
                        # t.health = 0
                        # player.lives += t.playereffect
                    
                    # if int(t.targettype) == 4: #enemy
                        # bremove = 1
                        # player.health -= self.playereffect
                        # if t.timer <= 0: # retargeting timer
                            # t.timer = t.timertotal
                            # if random.randint(0,100) >= 95: # 5% chance of attacking player         
                                # t.target = player.playercenter
                            # else:
                                # t.target = pygame.Vector2(random.randint(0,level.levelsize[0])+level.offset[0], random.randint(0,level.levelsize[1]+level.offset[1]), surf)
                        # if not t.active:
                            # t.speed = 0
                            # t.target = t.pos
            
            # if bremove:
                # level.targets.pop(level.targets.index(t))
                # del(t)
                # spawnx = random.randint(0, level.levelsize[0])
                # spawny = random.randint(0, level.levelsize[1])
                # otarget = ctarget((-level.offset[0] + spawnx, -level.offset[1] + spawny), 'sprites/crate'  + str(random.randint(1,6)) + '.png', random.randint(5,10), random.randint(0,1), random.randint(1,4), surf)
                # level.targets.append(otarget)
                # bremove = 0