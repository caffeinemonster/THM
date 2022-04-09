import pygame, time, random
from pygame.locals import *
from classtext import ctext
from classtarget import ctarget
from classsounds import csounds
from classpathfinder import cpathfinder
from classlog import clog


#from classtargets import ctargets

class clevel(object):
    def __init__(self):
        self.leveldata = ["1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
                          "1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1",
                          "1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1",
                          "1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1",
                          "1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1",
                          "1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1",
                          "1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1",
                          "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1",
                          "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1",
                          "1,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,1",
                          "1,0,0,1,1,1,1,1,0,0,1,0,0,0,0,1,1",
                          "1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,1",
                          "1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,1",
                          "1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1",
                          "1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1",
                          "1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1"]
                          
        self.spawns =    ["0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"]
        
        self.overlay =  [["0,0,0,0,0,11,11,11,11,0,0,0,0,0,0,0,0",
                          "0,0,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,2,0,3,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,4,0,5,5,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,8,8,8,7,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,9,9,9,0,0,0,0,0,0,0,0,0",
                          "11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"],
                         ["10,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "10,10,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,2,0,3,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,4,0,5,5,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,8,8,8,7,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,6,7,0,0,0,0,0,5,3,2,4,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"]]
                          
        self.rotation = [["0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"],
                         ["1,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "2,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,4,3,2,1,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"]]
        
        self.targets = []
                                                   
        self.imagepath = "tiles/tile0.png"
        self.image = pygame.image.load(self.imagepath) 
        self.tilesize = (self.image.get_width(), self.image.get_height())
        self.gridsize = (self.leveldata[0].count(',')+1, len(self.leveldata))
        self.levelsize = (self.tilesize[0] * self.gridsize[0], self.tilesize[1] * self.gridsize[1])
        #self.sprite = pygame.sprite.Sprite()
        #self.sprite.image = pygame.image.load(self.imagepath)
        #self.sprite.rect = self.sprite.image.get_rect()
        self.level = pygame.surface.Surface(self.levelsize)
        self.offset = pygame.Vector2(0,0)
        self.otext = ctext()
        self.generated = 0
        self.sfx = csounds()
        self.pfinder = cpathfinder(self.level, self.gridsize)
        self.pfinder.grid.data = self.leveldata
        self.log = clog()
        
        
        
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
    
    def killtargets(self, pcollection):
        for targ in self.targets:
            if targ.health <= 0:
                pcollection.seedfireballs(targ.pos[0], targ.pos[1])
                self.targets.pop(self.targets.index(targ))
                self.sfx.fxbonus()
    
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
                    otarget.active = 1
                if itartgettype > 0:
                    tempsurf = pygame.Surface((self.levelsize[0], self.levelsize[0]), pygame.SRCALPHA)
                    otarget = ctarget((x * self.tilesize[0] + (self.tilesize[0]/2), y * self.tilesize[1]+ (self.tilesize[1]/2)), simage, ihealth, idamgaeable, itartgettype, tempsurf)
                    otarget.pos = pygame.Vector2(otarget.pos[0] - (otarget.image.get_width() / 2), otarget.pos[1] - (otarget.image.get_height() / 2))
                    otarget.target = otarget.pos
                    
                    self.pfinder.pos_start = self.pfinder.grid.getxy(otarget.pos - self.offset)
                    
                    self.pfinder.pos_end = self.pfinder.grid.getrandomcell()
                    while self.pfinder.grid.getgridvalue(self.pfinder.pos_end[0], self.pfinder.pos_end[1]):
                        self.pfinder.pos_end = self.pfinder.grid.getrandomcell()
                    #self.pfinder.calcpath()
                    #otarget.opf.grid.data = self.leveldata
                    #if self.generated:
                        #otarget.opf.configure(self.gridsize[0],self.gridsize[1], self.level)
                        #otarget.opf.grid.configure(self.gridsize[0],self.gridsize[1], self.level)
                    #otarget.target = pygame.Vector2(otarget.pos[0] - (otarget.image.get_width() / 2), otarget.pos[1] - (otarget.image.get_height() / 2))
                    otarget.active = 0
                    self.targets.append(otarget)
                
    def drawtargets(self, surf):
        for t in self.targets:
            #t.opf.grid.cellwidth = self.tilesize[0]
            #t.opf.grid.cellwidth = self.tilesize[1]
            t.draw(surf, self.offset)
            
    def updatetargets(self, oplayer, surf):
        for targ in self.targets:
            #self.calcpath(oplayer, targ,surf)
            move = targ.target - targ.pos
            move_length = move.length()
            if move_length < targ.speed:
                targ.target = targ.pos
                targ.speed = 0
            elif move_length != 0:
                move.normalize_ip()
                move = move * targ.speed
                targ.pos += move
                
            #if targ.followplayer == 1:
                #if targ.targettype == 4:
                    #if targ.health > 0:
                        #pass
                        #self.calcpath(oplayer, targ, surf)
                        #print(targ.health)
                        #self.calcpath(targ, oplayer, surf)
                        
                        # self.pfinder.pos_start = self.pfinder.grid.getxy(targ.pos)
                        # self.pfinder.pos_end = self.pfinder.grid.getxy(oplayer.pos)
                        
                        # #self.pfinder.grid.drawgrid(self.level)
                        # n = self.pfinder.calcpath(self.level)
                        # tempcell=n
                        # while not tempcell == "": # while temp cell is still available 
                            # if not tempcell == None: # ensure the object exists 
                                # self.pfinder.grid.drawcell(self.level, tempcell.xy[0], tempcell.xy[1], (255,0,0), 5, 5) # highlight route
                                # if not tempcell.previousnode == "":
                                    # # draw nodes and link by line to show path 
                                    # pygame.draw.line(self.level, (0,255,0), (tempcell.xy[0]*self.pfinder.grid.cellwidth +(self.pfinder.grid.cellwidth/2), tempcell.xy[1]*self.pfinder.grid.cellheight+(self.pfinder.grid.cellheight/2)), (tempcell.previousnode.xy[0]*self.pfinder.grid.cellwidth+(self.pfinder.grid.cellwidth/2), tempcell.previousnode.xy[1]*self.pfinder.grid.cellheight+(self.pfinder.grid.cellheight/2)), width=2) # draws path
                                    # pygame.draw.circle(self.level, (0,0,255),(tempcell.xy[0]*self.pfinder.grid.cellwidth +(self.pfinder.grid.cellwidth/2), tempcell.xy[1]*self.pfinder.grid.cellheight+(self.pfinder.grid.cellheight/2)) , 3) # highlights points with circles 
                            # if not tempcell == "":
                                # if not tempcell == None:
                                    # tempcell = tempcell.previousnode
                                # else: break
                            # else: break
                            
                        # while not n == "":
                            # if n == None: break
                            # print("PATH : " + str(n.xy))
                            # if n.previousnode == "": break 
                            # if self.pfinder.grid.getxy(targ.pos) == self.pfinder.grid.getxy(n.xy): break
                            # n = n.previousnode
                        
                        # if not n == None:
                            # targ.target = self.pfinder.grid.getxylocation(n.xy)
                            # print(n.xy)
                            # print(self.pfinder.grid.getxylocation(n.xy))
  
            if targ.targettype == 4:
                if targ.timer <= 0: # retargeting timer
                    targ.timer = targ.timertotal
                    if random.randint(0,100) >= 50: # 5% chance of attacking player
                        
                        self.calcpath(targ, oplayer, surf)
                        targ.active = 1
                        targ.followplayer = 1
                        targ.speed = random.randint(1,4)
                    else:
                        #targ.followplayer = 0
                        #targ.target = pygame.Vector2(random.randint(0,self.levelsize[0]), random.randint(0,self.levelsize[1]))
                        targ.speed = random.randint(1,2)
                else: targ.timer -= 1
            if not targ.active:
                targ.speed = 0
                targ.target = targ.pos
                
    def calcpath(self, targ, oplayer, surf):
        
        if targ == None: return 
        if oplayer == None: return 
        
        self.pfinder = cpathfinder(self.level, self.gridsize)
        self.pfinder.grid.data = self.leveldata
        
        self.pfinder.pos_start = self.pfinder.grid.getxy(targ.pos - self.offset)
        self.pfinder.pos_end = self.pfinder.grid.getxy(oplayer.pos - self.offset)
        
        #self.pfinder = 
        print("Targ origin " + str(targ.pos - self.offset))
        print("Player origin " + str(oplayer.pos - self.offset))
        
        print("target xy:" + str(self.pfinder.grid.getxy(targ.pos - self.offset)))
        print("player xy:" + str(self.pfinder.grid.getxy(oplayer.pos - self.offset)))
        
        print("pfinder end pos:" + str(self.pfinder.pos_end))
        print("pfinder start pos:" + str(self.pfinder.pos_start))
        
#        
        
        #self.pfinder.grid.drawgrid(self.level)
        n = self.pfinder.calcpath(self.level)
        print("path calculated")
        tempcell=n
        while not tempcell == "": # while temp cell is still available 
            if not tempcell == None: # ensure the object exists 
                self.pfinder.grid.drawcell(self.level, tempcell.xy[0], tempcell.xy[1], (255,0,0), 5, 5) # highlight route
                if not tempcell.previousnode == "":
                    # draw nodes and link by line to show path 
                    pygame.draw.line(self.level, (0,255,0), (tempcell.xy[0]*self.pfinder.grid.cellwidth +(self.pfinder.grid.cellwidth/2), tempcell.xy[1]*self.pfinder.grid.cellheight+(self.pfinder.grid.cellheight/2)), (tempcell.previousnode.xy[0]*self.pfinder.grid.cellwidth+(self.pfinder.grid.cellwidth/2), tempcell.previousnode.xy[1]*self.pfinder.grid.cellheight+(self.pfinder.grid.cellheight/2)), width=2) # draws path
                    pygame.draw.circle(self.level, (0,0,255),(tempcell.xy[0]*self.pfinder.grid.cellwidth +(self.pfinder.grid.cellwidth/2), tempcell.xy[1]*self.pfinder.grid.cellheight+(self.pfinder.grid.cellheight/2)) , 3) # highlights points with circles 
                    
            #else: break 
            
            if not tempcell == "":
                if not tempcell == None:
                    tempcell = tempcell.previousnode
                else: break
            else: break
            
        while not n == "":
            if n == None: break
            print("PATH : " + str(n.xy))
            if n.previousnode == "": break 
            #if self.pfinder.grid.getxy(targ.pos - self.offset) == n.xy: break
            n = n.previousnode
        
        # if not n == None:
            # targ.target = self.pfinder.grid.getxylocation(n.xy)
            # print(n.xy)
            # print(self.pfinder.grid.getxylocation(n.xy))

        #def drawcell(self, surf, x, y, colour, border, curve): # used to draw cells 
        if not n == None:
            self.pfinder.grid.drawcell(self.level, n.xy[0], n.xy[1], (128,128,128), 3, 4)
        
    def collide(self, oplayer, pcollection):
        for x in range (0, int(self.gridsize[0])):
            for y in range (0,  int(self.gridsize[1])):                    
                if oplayer.playercenter[0] >= x*self.tilesize[0]+self.offset[0] and oplayer.playercenter[0] <= x*self.tilesize[0]+self.offset[0] + self.tilesize[0]:
                    if oplayer.playercenter[1] >= y*self.tilesize[1]+self.offset[1] and oplayer.playercenter[1] <= y*self.tilesize[1]+self.offset[1] + self.tilesize[1]:
                        # PLAYER IS ON MAP
                        tileid = self.leveldata[y].split(',')[x]
                        if int(tileid) > 0: # COLLISION STOP PLAYER    
                            pcollection.seedstars(oplayer.playercenter[0], oplayer.playercenter[1])
                            oplayer.pos = oplayer.poslast
                            oplayer.target = oplayer.poslast
                            oplayer.speed = 0
                            return 1
                        else: # NO COLLISION
                            oplayer.updateposlast()
                            return 0
        # PLAYER IS OUT OF MAP 
        return 0