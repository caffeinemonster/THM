from pygame.locals import * # import pygame constants 
import pygame, math, sys, time # import required librarys 
from classgrid import cgrid # import grid class
from classcolour import ccolour # new instance of colour class

class node(object):
    def __init__(self, xy):
        self.xy = xy # set grid / xy location (x,y)
        self.f = float('inf') # set up float value equal to +infinity
        self.h = float('inf') # set up float value equal to +infinity
        self.g = float('inf') # set up float value equal to +infinity
        self.previousnode = "" # holds parent node data
        
class cpathfinder(object):
    def __init__(self, surf, xy): # initialise class variables 
        self.step = 0 # variable to hold steps taken towards goal 
        self.pos_start = (0,0) # variable to hold start pos 
        self.pos_end = (0,0) # variable to hold end pos 
        self.grid = cgrid(xy[0],xy[1], surf) # grid class instance (holds level data)
        self.grid.create() # generaates initial level data 
        self.surf = surf # assigns DISPLAYSURF to self.surf (for eaasy access and debugging)
        self.pos_start = self.grid.getrandomcell() # pick random cell 
        self.pos_end = self.grid.getrandomcell() # pick random cell
        self.stats = [] # holds heat map (every cells calculatyed distance to end pos)
        while self.pos_start == self.pos_end: # make sure endpos is not startpos 
            self.pos_end = self.grid.getrandomcell() # get new end pos
        self.open = [] # list to store array of open search locations 
        self.closed  = [] # list of closed search locations 
        self.open.append(node(self.pos_start)) # append start pos to open list sets 1st node to search 
       
    def checkkeys(self):
        # function to detect key presses 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.mixer.quit()
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.mixer.quit()
                    pygame.quit()
                    sys.exit()

    def checknode(self, o, c): # checks to see if node (c) is a better match than the original node (o)
        # determine between nodes which is a better next step ?
        cellreturn = o
        if o.f > c.f: # check f score (distance to endpos + steps)
            return c
        if o.f == c.f:
           if o.g > c.g: # check g score (steps)
               return c
        if o.h > c.h: # check distance to end pos
            return c   
        return cellreturn # if not return original cell
        
    def calcpath(self, surf = ""): #, surf): # calculates A* optimal path / route
        ocolour = ccolour() 
        # build stats map for grid.
        for y in range(0,self.grid.y):
            for x in range(0,self.grid.x):
                onode = node((x,y)) # creates new stats node
                if self.grid.getgridvalue(onode.xy[0], onode.xy[1]) > 0:continue # check grid ref exists and is not a wall
                onode.h = self.grid.calculatedistance(onode.xy, self.pos_end) # calculates distance 
                self.stats.append(onode) # adds node to stats (cell distance away from goal)
        # CALCULATION STARTS HERE        
        bexit = 0
        neighbours = [(0,1), (1,0), (0,-1), (-1,0)] # variable used to calculate neighbour poitions
        while not bexit: # dont exit till bexit is true
            for o in self.open: # loop through open nodes
                self.checkkeys() # check user keys 
                # sanity check ... are we looking for a path that doesnt exist or costs to much time to calculate 
                if self.step > self.grid.x * self.grid.y: # any more than 50 steps assume failure (no route to goal)
                    bexit = 1 
                    break 
                # check there isnt a more optimal node available in the search list 
                for on in self.open: # check there is not another node available with a better score in open list
                    o = self.checknode(o, on) # check node and return/set optimal 
                o.g = self.step  # add steps to node
                o.h = self.grid.calculatedistance(o.xy, self.pos_end) # calculate distance to end goal 
                o.f = o.g + o.h # heuristic value (distance + steps)                
                if self.grid.getgridvalue(o.xy[0], o.xy[1]):continue # check grid ref exists and is not a wall
                for n in neighbours: # check neighbour squares 
                    onode = node((o.xy[0] + n[0], o.xy[1] + n[1])) # create node
                    bskip = 0 # skip this node variable 
                    if self.grid.getgridvalue(onode.xy[0], onode.xy[1]): continue # check grid ref exists and is not a wall
                    for on in self.closed: # check node not in closed list 
                        if on.xy == o.xy:
                            bskip = 1
                            break        
                    if bskip:break # move to next neighbour
                    onode.g = o.g + 1 # set steps value 
                    onode.h = self.grid.calculatedistance(o.xy, self.pos_end) # set distance value 
                    onode.f = onode.g + onode.f # set heuristic value (step + distance)
                    onode.previousnode = o # set previous node to trace path 
                    
                    if not surf == "": self.grid.drawcell(surf, onode.xy[0], onode.xy[1], ocolour.getrgb("YELLOW"), 3, 2) # highlight search 
                    self.open.append(onode) # add node to serach list 
                self.step += 1 # increase step count by one
                if o.xy == self.pos_end: # if path found (end goal reached)
                    return o # return current node 
                    bexit = 1 # exit routine 
                    break # quit for loop 
                self.closed.append(o) # append current node to closed list 
                try:
                    self.open.remove(o) # remove current node from open list 
                except: pass
                if len(self.open) == 0: # if all search possibilities have been reached exit routine
                    return node(self.pos_start) # return the startpos if no path found 
                    bexit = 1 # exit routine 
                    break # break for lopp 
