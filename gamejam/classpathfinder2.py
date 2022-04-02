import random, pygame, sys, time
from classgrid import cgrid 
from pygame.locals import *
class ccell(): # class to hold cell data for path analysis 
    def __init__(self, pos): 
        self.pos = pos # position 
        self.G = 0 #step count 
        self.H = 0 # estimated distance to target
        self.F = 0 # estimated distance +stepcount  
        self.previouscell = "" # previous cell object
        self.neighbours = [] # this cells neighbours as cell object list
        self.isstart = 0 # is the starting cell 
        self.isend = 0 # is the ending cell
        

class cpathfinder(): # class to find path through grid array 
    def __init__(self):
        
        self.startpos = (0,0) # vector of start position 
        self.endpos = (0,0) # vector of end position 
        self.osearch = [] # list to hold open cells 
        self.oclosed = [] # list to hold closed cells
        self.data = [] # array (list) to hold level data
        self.x = 0 # value calculated holds width of data
        self.y = 0 # value calculated holds heigh of data
        self.cellstart = ""
        self.cellend = ""
        self.cellcurrent = ""
        self.step = 0
        self.grid = cgrid(20,20,"")
        self.path = []

    def initialise(self):
        if self.data == [] : return # exit if no data 
        
        self.y = len(self.data) # calculate height of grid
        self.x = len(self.data[0].split(",")) # calculate width of grid 
        
        self.path = []
        self.osearch = [] # reset search list 
        self.oclosed = [] # reset closed list 
        
        self.cellstart = ccell(self.startpos)
        self.cellstart.isstart = 1
        
        self.cellend = ccell(self.endpos)
        self.cellstart.isend = 1
        
        self.cellpath = ccell(self.startpos)
        
        self.step = 0
        self.grid.data = self.data
        self.grid.x = self.x
        self.grid.y = self.y
        self.osearch.append(self.cellstart)
        
    def calcpath(self, startpos, endpos, surf = ""):
        self.startpos = startpos
        self.endpos = endpos
        self.initialise()
        self.grid.configure(self.x, self.y, surf)
        if not surf == "":
            self.grid.drawcell(surf, startpos[0], startpos[1], (0,255,0),10,10)
            self.grid.drawcell(surf, endpos[0], endpos[1], (0,0,255),10,10)
            pygame.display.flip()
            pygame.display.update()
        
        #neighbours = [(-1,1), (1,-1), (-1,0), (-1,-1), (1,1), (1,0), (0,-1), (0,1)] # uncomment for X+Y and diagnal searching
        neighbours = [(0,1), (1,0), (0,-1), (-1,0)]
        bexit = 0
        #istep = 0
        while 1:
            for s in self.osearch:
                #s.G = istep
                s.H = self.grid.calculatedistance(self.startpos, self.endpos) # calculate estimated distance to endpos 
                s.F = s.G + s.H # combine count and distance
                print (s.G)
                for n in neighbours:
                    ncell = ccell((s.pos[0] + n[0], s.pos[1] + n[1])) # create cell object 
                    bclosed = 0
                    for c in self.oclosed: # check not in closed list
                        if c.pos == ncell.pos:
                            bclosed = 1
                            continue
                    if bclosed: continue # move to next item if in closed list 
                    if self.grid.getgridvalue(ncell.pos[0], ncell.pos[1]):continue # check grid ref exists and is not a wall
                    if n in [(-1,0), (1,0), (0,-1), (0,1)]: # if moving horizontally or vertically
                        ncell.G = s.G + 10 # weighting for X+Y moves
                    else: # moving diagnally 
                        ncell.G = s.G + 14 # weighting for diagnal moves
                        
                    ncell.H = self.grid.calculatedistance(ncell.pos, endpos) * 10 # calculate distance to end point from neighbour cell
                    ncell.F = ncell.G + ncell.H # calculate F value
                    ncell.previouscell = s # set previous cell value (object)
                    
                    print (ncell.G)

                    for event in pygame.event.get(): # handle keyboard events
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                pygame.mixer.quit()
                                pygame.quit()
                                sys.exit()
                                
                    s.neighbours.append(ncell)                    
                    bappend = 1
                    for o in self.oclosed:
                        if ncell.pos == o.pos:
                            bappend = 0
                    if bappend: self.osearch.append(ncell)
                    
                    if ncell.pos == endpos:
                        self.cellpath = ncell
                        bexit = 1
                
                if s.pos == endpos:
                    self.cellpath = s
                    bexit = 1
                if bexit: break
                

                if not surf == "":
                    for O in self.osearch: 
                       self.grid.drawcell(surf, O.pos[0], O.pos[1], (0,128,255),4,4)
                    for O in self.oclosed: 
                       self.grid.drawcell(surf, O.pos[0], O.pos[1], (255,128,0),2,2)
                    pygame.display.flip()
                    pygame.display.update()
                    

                self.step += 1 
                self.osearch.pop(self.osearch.index(s))
                self.oclosed.append(s)
                if self.step > 2048 or len(self.osearch) == 0:
                    bexit = 1
                    break
            if bexit: break
        
        
        
        tempcell = self.cellpath            
        while not tempcell.previouscell == "":
            pygame.draw.line(surf, (255,0,0), (tempcell.pos[0]*self.grid.cellwidth +(self.grid.cellwidth/2), tempcell.pos[1]*self.grid.cellheight+(self.grid.cellheight/2)), (tempcell.previouscell.pos[0]*self.grid.cellwidth+(self.grid.cellwidth/2), tempcell.previouscell.pos[1]*self.grid.cellheight+(self.grid.cellheight/2)), width=5) # draws path
            pygame.draw.circle(surf, (0,128,128),(tempcell.pos[0]*self.grid.cellwidth +(self.grid.cellwidth/2), tempcell.pos[1]*self.grid.cellheight+(self.grid.cellheight/2)) , 10) # highlights points with circles 
            tempcell = tempcell.previouscell

        pygame.display.flip() # swap screen buffer 
        pygame.display.update() # update screen
        
        return self.path
        
    