import pygame, random, math, os
#from os.path import exists
from pygame.locals import *
from classsounds import csounds
from classtarget import ctarget
from classgrid import cgrid
from classparticlecontroller import cparticlecontroller

class ctargets(object):  # target group class
    def __init__(self):
        self.targets = []
        self.particles = cparticlecontroller()
    
    def draw(self, surf):
        self.particles.draw(surf)
        for t in self.targets:
            t.draw(surf)
    
    def update(self):
        for t in self.targets:
            move = t.target - t.pos
            move_length = move.length()
            if move_length < t.speed:
                t.target = t.pos
                t.speed = 0
            elif move_length != 0:
                move.normalize_ip()
                move = move * t.speed
                t.pos += move
                
            
                
            if t.targettype == 4:
                if t.target == t.pos:
                    
                    if t.timer == 0:
                        inumber = random.randint(0,1)
                        
                        if inumber == 0:
                            t.image = pygame.image.load(t.imagepath)
                        else:
                            simage = t.imagepath.replace("png", "") + "idle1.png"
                            t.image = pygame.image.load(simage)
                else:
                    inumber = random.randint(0,1)
                    if inumber == 0:
                        t.image = pygame.image.load(t.imagepath)
                    else:
                        simage = t.imagepath.replace("png", "") + "walk1.png"
                        if os.path.exists(simage):
                            t.image = pygame.image.load(simage)
                            
                    #if t.timer == 0:
                        
                if t.timer <= 0: # reteting timer
                    t.timer = random.randint(0, t.timertotal)
                else: t.timer -= 1
            if not t.active:
                t.speed = 0
                t.target = t.pos
                
        self.killtargets() # removes tets that have 0 life
        
    
    def collide(self, level, player):
        bremove = 0
        for t in self.targets:
            if player.playercenter[0] >= t.pos[0] - t.image.get_width()/2 and player.playercenter[0] <= t.pos[0] + t.image.get_width()/2:
                if player.playercenter[1] >= t.pos[1] - t.image.get_height()/2 and player.playercenter[1] <= t.pos[1] + t.image.get_height()/2:
                    
                    if t.damageable:                            
                        bremove = 1
                    else:
                        player.pos = player.poslast
                        player.target = player.poslast
                        player.speed = 0
                    
                    if int(t.targettype) == 0:
                        t.playereffect = t.playereffect #do nothing
                    
                    if int(t.targettype) == 1:    
                        bremove = 1
                        t.health = 0
                        player.health += t.playereffect
                        
                    if int(t.targettype) == 2:
                        bremove = 1
                        t.health = 0
                        player.projectiles.ammo += t.playereffect
                        
                    if int(t.targettype) == 3:
                        bremove = 1
                        t.health = 0
                        player.lives += t.playereffect
                    
                    if int(t.targettype) == 4: #enemy
                        
                        bremove = 1
                        player.health -= t.playereffect
                        if t.timer <= 0: # retargeting timer
                            t.timer = t.timertotal
                            if random.randint(0,100) >= 95: # 5% chance of attacking player         
                                t.target = player.playercenter
                            else:
                                t.target = pygame.Vector2(random.randint(0,level.levelsize[0]), random.randint(0,level.levelsize[1]))
                        if not t.active:
                            t.speed = 0
                            t.target = t.pos
            
            if bremove: # needs fixing to respawn on square that isnt a wall 
                s = pygame.Surface((level.levelsize[0], level.levelsize[1]))
                og = cgrid(level.gridsize[0],level.gridsize[1], s)
                og.data = level.leveldata
                c = og.getrandomcell()
                cloc = og.getxylocation(c)
                
                cloc[0] = (cloc[0] + (level.tilesize[0] / 2))
                cloc[1] = (cloc[1] + (level.tilesize[1] / 2))
                
                if t.targettype == 4: self.particles.seedslime(t.pos + (random.randint(0,10)-5, random.randint(0,10)-5), "GREEN")
                
                if t.targettype == 4:
                    otarget = ctarget(cloc, 'sprites/enemy'  + str(random.randint(4,4)) + '.png', random.randint(10,50), 1, 4)
                else:
                    otarget = ctarget(cloc, 'sprites/crate'  + str(random.randint(1,6)) + '.png', random.randint(5,10), random.randint(0,1), random.randint(1,4))
                
                otarget.pos[0] = otarget.pos[0] - otarget.image.get_width()/2
                otarget.pos[1] = otarget.pos[1] - otarget.image.get_height()/2
                
                self.targets.append(otarget)
                self.targets.remove(t)
                bremove = 0
                
    def killtargets(self):
        for targ in self.targets:
            if targ.health <= 0:
                self.targets.remove(targ)
        