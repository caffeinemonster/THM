import pygame, time, random
from pygame.locals import *
from classtext import ctext
from classtarget import ctarget
from classsounds import csounds


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
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                          "0,0,0,0,0,0,1,1,0,4,4,4,4,1,1,0,0",
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
                    otarget.opf.grid.data = self.leveldata
                    
                    if self.generated:
                        otarget.opf.configure(self.gridsize[0],self.gridsize[1], self.level)
                        otarget.opf.grid.configure(self.gridsize[0],self.gridsize[1], self.level)
                    #otarget.target = pygame.Vector2(otarget.pos[0] - (otarget.image.get_width() / 2), otarget.pos[1] - (otarget.image.get_height() / 2))
                    otarget.active = 0
                    self.targets.append(otarget)
                
    def drawtargets(self, surf):
        for t in self.targets:
            t.opf.grid.cellwidth = self.tilesize[0]
            t.opf.grid.cellwidth = self.tilesize[1]
            t.draw(surf, self.offset)
            
    def updatetargets(self, oplayer, surf):
        for targ in self.targets:
            self.calcpath(oplayer, targ,surf)
            move = targ.target - targ.pos
            move_length = move.length()
            if move_length < targ.speed:
                targ.target = targ.pos
                targ.speed = 0
            elif move_length != 0:
                move.normalize_ip()
                move = move * targ.speed
                targ.pos += move
            if targ.followplayer == 1:
                if targ.targettype == 4:
                    if targ.health > 0:
                        self.calcpath(oplayer, targ, surf)
                        # print(targ.opf.cellpath)
                        # tempcell = targ.opf.cellpath
                        # print("path:")
                        # while not tempcell == "":
                            # print(tempcell.pos)
                            # tempcell = tempcell.previouscell
                            
                            
                        # tempcell = targ.opf.cellpath
                        # olist = []
                        # while not tempcell == "":
                            # if not tempcell == "":
                                # olist.append(tempcell)
                                # tempcell = tempcell.previouscell
                                # print(tempcell)
                        # print(olist)
                        
                        
                        # previous = tempcell
                        
                        # while not tempcell == None:
                            # previous = tempcell
                            # tempcell = tempcell.previouscell
                            #if tempcell == "":break
                            
                        # if not previous == None:
                            # print("setting position")
                            # print(previous.pos)
                            # targ.target = targ.opf.grid.getxylocation(previous.pos)
                            
                        #if self.generated:
                        #print("TARG" + str(targ.opf.grid.getxy(targ.pos)))
                        #print("PLAY:" + str(targ.opf.grid.getxy(oplayer.pos - self.offset)))
                        #targ.target[0] = (oplayer.pos[0] - (oplayer.image.get_width()/2) - self.offset[0]) - targ.image.get_width()
                        #targ.target[1] = (oplayer.pos[1] - (oplayer.image.get_height()/2) - self.offset[1]) - targ.image.get_height()
                        #targ.target = oplayer.pos - self.offset - targ.image.get_size()    
            if targ.targettype == 4:
                if targ.timer <= 0: # retargeting timer
                    targ.timer = targ.timertotal
                    if random.randint(0,100) >= 0: # 5% chance of attacking player
                        # NEED TO ADD CODE TO IMPLEMENT PATH FINDING CLASS 
                        #targ.target[0] = (oplayer.pos[0] - (oplayer.image.get_width()/2) - self.offset[0]) - (targ.image.get_width()/2)
                        #targ.target[1] = (oplayer.pos[1] - (oplayer.image.get_height()/2) - self.offset[1]) - (targ.image.get_height()/2)
                        # tempcell = targ.opf.calcpath(targ.opf.grid.getxy(targ.pos + self.offset), targ.opf.grid.getxy(oplayer.playercenter), self.level)    
                        # while not tempcell.previouscell == "":
                            # tempcell = tempcell.previouscell
                        # # targ.target = targ.opf.grid.getxylocation(tempcell.pos)
                        # print("TARG" + str(targ.opf.grid.getxy(targ.pos)))
                        # print("PLAY:" + str(targ.opf.grid.getxy(oplayer.pos - self.offset)))
                        # tempcell = targ.opf.calcpath(targ.opf.grid.getxy(targ.pos), targ.opf.grid.getxy(oplayer.pos - self.offset), self.level)    
                        # while not tempcell.previouscell == "":
                            # tempcell = tempcell.previouscell
                        # targ.target = targ.opf.grid.getxylocation(tempcell.pos)
                        #targ.opf.data = self.leveldata
                        # tempcell = targ.opf.cellpath
                        # previous = tempcell
                        # while not targ.opf.grid.getxy(targ.pos) == tempcell.pos:
                            # previous = tempcell
                            # tempcell = tempcell.previouscell
                            # if tempcell == "":
                                # break
                        # if not previous == "":
                            # targ.target = targ.opf.grid.getxylocation(previous.pos)
                            
                        self.calcpath(oplayer, targ, surf)
                        targ.active = 1
                        targ.followplayer = 1
                        targ.speed = random.randint(1,4)
                        
                    else:
                        targ.followplayer = 0
                        targ.target = pygame.Vector2(random.randint(0,self.levelsize[0]), random.randint(0,self.levelsize[1]))
                        targ.speed = random.randint(1,2)
            if not targ.active:
                targ.speed = 0
                targ.target = targ.pos
    
    def calcpath(self, player, target, surf):
        #if self.leveldata == []:
        target.opf.data = self.leveldata
        target.opf.grid.configure(self.gridsize[0], self.gridsize[1], self.level)
        target.opf.grid.data = self.leveldata
        target.opf.grid.cellwidth = self.tilesize[0]
        target.opf.grid.cellheight = self.tilesize[1]
        #print(target.pos)
        #print(player.pos)
        
        print(target.opf.grid.getxy(target.pos))
        print(target.opf.grid.getxy(player.pos))
        
        tempcell = ""
        previous = ""
        
        if (not player.pos == None) and (not target.pos == None):
            print("claculating path")
            tempcell = target.opf.calcpath(target.opf.grid.getxy(target.pos), target.opf.grid.getxy(player.pos), surf)
        #try:
        olist = []
        while not tempcell == "":
            #if target.opf.grid.getxy(target.pos) == tempcell.pos:break 
            if tempcell == "":break
            print(target.pos)
            print("tempcellpos : " + str(tempcell.pos))
            olist.append(tempcell.pos)
            previous = tempcell
            tempcell = tempcell.previouscell
        
        print(olist)
            
        #if not previous == "":
        #target.target = target.opf.grid.getxylocation(olist[len(olist)-1])
        print("next target location")
        #print(target.opf.grid.getxylocation(pygame.Vector2(olist[len(olist)-1])))
        #print(olist[len(olist)-1])
        #print(target.opf.grid.getxylocation(olist[len(olist)-1]))
        #target.target = target.opf.grid.getxylocation(olist[len(olist)-1])
        target.target = target.opf.grid.getxylocation(pygame.Vector2(olist[1]))
        target.active = 1
#        except:pass
        
        #return target.cellpath
            
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