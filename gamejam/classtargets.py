import pygame, random, math
from pygame.locals import *
from classsounds import csounds
from classtarget import ctarget

class ctargets(object):  # target group class
    def __init__(self):
        self.targets = []
    
    def draw(self, surf):
        for t in self.targets:
            t.draw(surf, (0,0))
    
    def update(self):
        for targ in self.targets:
            move = targ.target - targ.pos
            move_length = move.length()
            if move_length < targ.speed:
                targ.target = targ.pos
                targ.speed = 0
            elif move_length != 0:
                move.normalize_ip()
                move = move * targ.speed
                targ.pos += move
            
            if targ.targettype == 4:
                if targ.timer <= 0: # retargeting timer
                    targ.timer = targ.timertotal
                    if random.randint(0,100) >= 50:
                        targ.active = 1
                        targ.followplayer = 1
                        targ.speed = random.randint(1,4)
                    else:
                        targ.speed = random.randint(1,2)
                else: targ.timer -= 1
            if not targ.active:
                targ.speed = 0
                targ.target = targ.pos
                
        self.killtargets() # removes targets that have 0 life
        
    
    def collide(self, level, player):
        bremove = 0
        for t in self.targets:
            if player.playercenter[0] >= t.pos[0]+level.offset[0] and player.playercenter[0] <= t.pos[0]+level.offset[0] + t.image.get_width():
                if player.playercenter[1] >= t.pos[1]+level.offset[1] and player.playercenter[1] <= t.pos[1]+level.offset[1] + t.image.get_height():
                    if t.damageable:                            
                        bremove = 1
                    else:
                        player.pos = player.poslast
                        player.tet = player.poslast
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
                                t.target = pygame.Vector2(random.randint(0,level.levelsize[0])+level.offset[0], random.randint(0,level.levelsize[1]+level.offset[1]))
                        if not t.active:
                            t.speed = 0
                            t.target = t.pos
            
            if bremove: # needs fixing to respawn on square that isnt a wall 
                self.targets.remove(t)
                #del(t)
                spawnx = random.randint(0, level.levelsize[0])
                spawny = random.randint(0, level.levelsize[1])
                otarget = ctarget((-level.offset[0] + spawnx, -level.offset[1] + spawny), 'sprites/crate'  + str(random.randint(1,6)) + '.png', random.randint(5,10), random.randint(0,1), random.randint(1,4))
                
                self.targets.append(otarget)
                bremove = 0
    def killtargets(self):
        for targ in self.targets:
            if targ.health <= 0:
                self.targets.remove(targ)
        