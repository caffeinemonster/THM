import pygame, time, random
from pygame.locals import *
#from classtext import ctext
from classtarget import ctarget
from classtargets import ctargets
from classsounds import csounds
from classlog import clog

class clevel(object):
    def __init__(self, surf):
        self.debug = 1
        self.leveldata = ["1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
                          "1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
                          "1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
                          "1,0,1,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
                          "1,0,1,0,0,0,0,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
                          "1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
                          "1,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
                          "1,1,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
                          "1,0,0,0,1,0,0,0,0,1,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1",
                          "1,0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1",
                          "1,0,1,1,1,0,0,0,0,1,0,1,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1",
                          "1,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
                          "1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
                          "1,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
                          "1,0,0,0,0,0,0,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
                          "1,0,1,1,1,1,1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
                          "1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1",
                          "1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1"]
        
        self.spawns =    ["0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,3,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"]
        
        self.overlay =   [["0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,2,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"]]
                          
        self.rotation = [["0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"]]
        
        #self.targets = []
                                                   
        self.imagepath = "tiles/tile0.png"
        self.image = pygame.image.load(self.imagepath) 
        self.gridsize = (self.leveldata[0].count(',')+1, len(self.leveldata))
        self.tilesize = (surf.get_width() / self.gridsize[0], surf.get_height() / self.gridsize[1])
        
        self.levelsize = (self.tilesize[0] * self.gridsize[0], self.tilesize[1] * self.gridsize[1])
        self.level = pygame.surface.Surface(self.levelsize)
        self.offset = pygame.Vector2(0,0)
        
        self.targets = ctargets()
        
        #self.otext = ctext()
        self.generated = 0
        self.sfx = csounds()
        
    def generatelevel(self, surf):
        if self.generated == 0:
            # base layer (leveldata)
            for x in range (0, int(self.gridsize[0])):
                for y in range (0,  int(self.gridsize[1])):                    
                    tileid = self.leveldata[y].split(',')[x]
                    imagestring = "tiles/tile0.png"
                    if int(tileid) >= 1: imagestring = "tiles/tile" + tileid + ".png"
                    drawpos = (x*self.tilesize[0], y*self.tilesize[1])
                    self.image = pygame.image.load(imagestring)
                    self.image = pygame.transform.scale(self.image, (self.tilesize[0], self.tilesize[1]))
                    self.level.blit(self.image, (drawpos[0], drawpos[1]))
            # overlay level (overlay)
            for i in range (0, len(self.overlay)):
                for x in range (0, int(self.gridsize[0])):
                    for y in range (0,  int(self.gridsize[1])):                    
                        tileid = self.overlay[i][y].split(',')[x]
                        if not int(tileid) == 0:
                            imagestring = "tiles/tile0.png"
                            if int(tileid) >= 1: imagestring = "tiles/tile" + tileid + ".png"
                            drawpos = (x*self.tilesize[0], y*self.tilesize[1])
                            self.image = pygame.image.load(imagestring)
                            self.image = pygame.transform.scale(self.image, (self.tilesize[0], self.tilesize[1]))
                            irotate = int(self.rotation[i][y].split(',')[x])
                            if irotate > 0:
                                if irotate == 1: irotate = 0
                                if irotate == 2: irotate = 90
                                if irotate == 3: irotate = 180
                                if irotate == 4: irotate = 270
                            self.level.blit(pygame.transform.rotate(self.image, irotate), (drawpos[0], drawpos[1]))
            self.spawntargets()
            self.generated = 1
            
    def draw(self, surf):
        self.generatelevel(surf)
        if not self.level == "":
            surf.blit(self.level, self.offset)
        self.targets.draw(surf)
    
    def spawntargets(self):
        for x in range (0, int(self.gridsize[0])):
            for y in range (0,  int(self.gridsize[1])):                    
                tileid = self.leveldata[y].split(',')[x]
                imagestring = "tiles/tile0.png"
                itartgettype  = int(self.spawns[y].split(',')[x])
                idamgaeable = random.randint(0,1)
                ihealth = random.randint(30,75)
                simage = ""
                if not itartgettype == 4:
                    simage = 'sprites/crate' + str(random.randint(1,9)) + '.png'
                else:
                    simage = 'sprites/enemy' + str(random.randint(1,4)) + '.png'
                    idamgaeable = 1
                if itartgettype > 0:
                    #tempsurf = pygame.Surface((self.levelsize[0], self.levelsize[0]), pygame.SRCALPHA)
                    otarget = ctarget((x * self.tilesize[0] + (self.tilesize[0]/2), y * self.tilesize[1]+ (self.tilesize[1]/2)), simage, ihealth, idamgaeable, itartgettype)
                    otarget.pos = pygame.Vector2(otarget.pos[0] - (otarget.image.get_width() / 2), otarget.pos[1] - (otarget.image.get_height() / 2))
                    otarget.target = otarget.pos
                    otarget.active = 0
                if itartgettype > 0:
                    self.targets.targets.append(otarget)
    
    # def pathfind(self, pfinder, player, surf):
        # for t in self.targets.targets:
            # if t.active:
                # if t.targettype == 4:
                    # # if not t.pos == t.target: continue
                    # pfinder.pos_start = pfinder.grid.getxy(player.pos)
                    # pfinder.end_pos =  pfinder.grid.getxy(t.pos)
                    # print("target xy grid location : " + str(pfinder.grid.getxy(t.pos)))
                    # print("target xy pos (screen) location : " + str(t.pos))
                    
                    # # print(t.pos)
                    # o = pfinder.calcpath()
                    
                    # if o is None: continue 
                    # if o == "": continue 
                    # if o.previousnode is None: continue 
                    # if o.previousnode == "": continue 
                    # t.target = pfinder.grid.getxylocation(o.xy)
                    # t.target = pfinder.grid.getxylocation(o.previousnode.xy)
                    # tempcell = o
                    # while not tempcell == None:
                       # if tempcell == "": break
                       # if tempcell is None: break
                       # if tempcell.previousnode is None: break
                       # if tempcell.previousnode == "": break
                       # if self.debug:pfinder.grid.drawcell(surf, tempcell.xy[0], tempcell.xy[1], (128,255,0), 5, 4)
                       # tempcell = tempcell.previousnode
                       
        # pygame.display.flip()
        # pygame.display.update()
                    
    
    def update(self):
        self.targets.update()
        
    def collide(self, player):
        # TARGET COLLISION CODE:
        self.targets.collide(self, player)
        player.projectiles.collide(self.targets)
        
        # LEVEL PLAYER COLLISION CODE - STOPS PLAYER TRAVELLING THROUGH WALLS 
        for x in range (0, int(self.gridsize[0])):
            for y in range (0,  int(self.gridsize[1])):                    
                if player.playercenter[0] >= x*self.tilesize[0]+self.offset[0] and player.playercenter[0] <= x*self.tilesize[0]+self.offset[0] + self.tilesize[0]:
                    if player.playercenter[1] >= y*self.tilesize[1]+self.offset[1] and player.playercenter[1] <= y*self.tilesize[1]+self.offset[1] + self.tilesize[1]:
                        # PLAYER IS ON MAP
                        tileid = self.leveldata[y].split(',')[x]
                        if int(tileid) > 0: # COLLISION STOP PLAYER    
                            player.pos = player.poslast
                            player.target = player.poslast
                            player.speed = 0
                            return
                        else: # NO COLLISION
                            player.updateposlast()
                            return
        # PLAYER IS OUT OF MAP
        #return 0