import pygame, time, sys, random, math
from classtext import ctext
from pygame.locals import *

class Cell:
    def __init__(self, pos):
        self.pos = pos # position 
        self.G = 0 #step count 
        self.H = 0 # estimated distance to target
        self.F = 0 # estimated distance +stepcount  
        self.previouscell = "" # previous cell object 
        

pygame.init() # initialise pygame 
otext = ctext() # define new text class instance 
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # create display surface 

DSIZEX = DISPLAYSURF.get_width() # holds display size x
DSIZEY = DISPLAYSURF.get_height() # holds display size y

xsize = 18 # defines grid size 
ysize = 32 # defines grid size 

strdata = "" # string used to build initial level data 

DATA = [] # used to store level data (walls and not walls)
xloop = 0 # loop variable for x position 
while xloop <= xsize: # loop through x grid size 
    xloop +=1 # increment xloop var 
    if not strdata == "": # add data if data exists 
        DATA.append(strdata)
    yloop = 0 # define variable for y axis loop 
    strdata = "" # reset row data 
    strdata = str("0" if (random.randint(0,100)<80) else "1") # create 1st value in row 
    while yloop <= ysize: # loop through y grid size 
        strdata += "," + str("0" if (random.randint(0,100)<80) else "1") # create wall / not wall area 
        yloop += 1 # increment yloop 

#print(DATA) # output level data to console

GRIDSIZEX = len(DATA[0].split(",")) # calculate width in cells from DATA
GRIDSIZEY = len(DATA) # calculate height in cells from DATA

GRIDX = DSIZEX / GRIDSIZEX # divide screen by grid width
GRIDY = DSIZEY / GRIDSIZEY # divide screen by height 

GCLOCK = pygame.time.Clock()  # define game clock

def getrandomcell(): # get a random cell that isnt a wall 
    ireturn = (random.randint(0, GRIDSIZEX), random.randint(0, GRIDSIZEY))
    while getgridvalue(ireturn[0],ireturn[1]):
        ireturn = (random.randint(0, GRIDSIZEX), random.randint(0, GRIDSIZEY))
    return ireturn
    
def getgridvalue(x,y): # return grid value from x y pos (wall or not wall)
    if x < 0: return 1
    if y < 0: return 1
    if x > GRIDSIZEX: return 1
    if y > GRIDSIZEY: return 1
    try:
        return int(DATA[y].split(',')[x])
    except:
        return 1

def calculatedistance(pos1,pos2): # calculate distance between cells 
    AB = pygame.Vector2(pos1) - pygame.Vector2(pos2) # subtract positions to get xy distance  
    C = math.sqrt(AB[0]**2 + AB[1]**2) # pythagorus (calculates distance between pos1 and pos2)
    return C
    
def highlightcell(surf, x, y, colour): # used to highlight cells 
    pygame.draw.rect(surf, colour, (x*GRIDX, y*GRIDY, GRIDX, GRIDY), 5, 5)

def drawnode(surf, ncell, text, colour = ""): # used to draw nodes
    x,y = ncell.pos[0]*GRIDX, ncell.pos[1]*GRIDY
    if colour == "":
        pygame.draw.rect(surf, (128,128,128), (x, y, GRIDX, GRIDY))
    else:
        pygame.draw.rect(surf, colour, (x, y, GRIDX, GRIDY))
    #otext.draw(surf, text, (x, y), (255,0,0), 128, 21, text)
    celltext(surf, ncell.pos[0],ncell.pos[1], text)
    
def drawcell(surf, x, y, colour, border, curve): # used to draw cells 
    if not (border and curve):
        pygame.draw.rect(DISPLAYSURF, colour, (x*GRIDX, y*GRIDY, GRIDX, GRIDY))
    else:
        pygame.draw.rect(DISPLAYSURF, colour, (x*GRIDX, y*GRIDY, GRIDX, GRIDY), border, curve)
    #celltext(DISPLAYSURF, x,y, "")
    
def checkcell(list, cell): # returns cell object if position cell passed is found in list if the cell is not in the list function returns empty string 
    for o in list:
        if o.pos == cell.pos:
            return o
    return ""

def celltext(surf, x, y, text): # set the text of a cell
    otext.draw(surf, text, (x*GRIDX, y*GRIDY), (255,255,255), 255, 10, "")
    
def drawgrid(surf): # draws the generated grid to the screen 
    for y in range(0, GRIDSIZEY):
            for x in range(0, GRIDSIZEX):
                if int(DATA[y].split(',')[x]):
                    drawcell(surf, x, y, (255,255,255), 0, 0) # draw wall 
                else:
                    drawcell(surf, x, y, (128,0,0), 1, 4) # draw not wall 
                if (x,y) == startpos: drawcell(surf, x, y, (0,255,0), 10, 4) # draw startpos
                if (x,y) == endpos: drawcell(surf, x, y, (0,0,255), 10, 4) # draw endpos 
                
while True: # main game loop
    DISPLAYSURF.fill((0,0,0)) # fill canvas black 
    startpos = getrandomcell()
    endpos = getrandomcell()
    while endpos == startpos: # make sure endpos != startpos 
        endpos = getrandomcell() # get new end pos 
    
    ocell = Cell(startpos) # create new instance of cell object (defined at top)
    ocell.G = 0 # step count 
    ocell.H = calculatedistance(startpos, endpos) # calculate estimated distance to endpos 
    ocell.F = ocell.G + ocell.H # combine count and distance 
    ocell.previouscell = "" # no previous cell 
    
    osearchlist=[] # define searchlist holds cell objects
    oclosedlist=[] # define closedlist holds cell objects
    
    osearchlist.append(ocell) # add starting cell to search array
    
    search = osearchlist[0] # set 1st item (search) to the cell object of the 1st cell to be checked
    
    step = 0 # set step count to 0 (amount of tries before quitting)
    path = [] # list to hold path from startpos to endpos
    
    while True:
        DISPLAYSURF.fill((0,0,0)) # fill screen black
        drawgrid(DISPLAYSURF) # draw grid to screen 
        #neighbours = [(-1,0), (0,-1), (1,0), (0,1)] # uncomment for horizontal and vertical searching 
        # UP RIGHT DOWN LEFT 
        #neighbours = [(0,1), (1,0), (0,-1), (-1,0)]
        neighbours = [(-1,1), (1,-1), (-1,0), (-1,-1), (1,1), (1,0), (0,-1), (0,1)] # uncomment for X+Y and diagnal searching
        #neighbours = [(0,1), (1,0), (0,-1), (-1,0)]
        bexit = 0 # boolean variable if set to true search will reset
        
        # select next cell 
        for s in osearchlist:
            bclosed = 0
            for c in oclosedlist: # check not in closed list
                if c.pos == s.pos:
                    bclosed = 1
                    break
            if bclosed: continue # move to next item if in closed list 
            
            if s.F < search.F: # is item closest (overall cost) to endpos 
                search = s # set current cell

            if s.H < search.H: # is item distance to endpos less
                search = s # set current cell
            
            if s.F == search.F: # if item tied
                if s.G >= search.G: # check to see if count is greater ?
                    search = s # set current cell



        step += 1 # increment step value 
        for neighbour in neighbours: # iterate through neighbour cells
            ncell = Cell((search.pos[0] + neighbour[0], search.pos[1] + neighbour[1])) # create cell object 
            if getgridvalue(ncell.pos[0], ncell.pos[1]):continue # check grid ref exists and is not a wall
            
            if neighbour in [(-1,0), (1,0), (0,-1), (0,1)]: # if moving horizontally or vertically
                ncell.G = search.G + 10 # weighting for X+Y moves
            else: # moving diagnally 
                ncell.G = search.G + 14 # weighting for diagnal moves
                
            ncell.H = calculatedistance(ncell.pos, endpos) * 10 # calculate distance to end point from neighbour cell
            ncell.F = ncell.G + ncell.H # calculate F value
            ncell.previouscell = search # set previous cell value (object)
            
            text = "pos:" + str(ncell.pos) # build text string for debug / screen output
            text += " G:" + str(ncell.G)
            text += " H:" + str(ncell.H)
            text += " F:" + str(ncell.H)
            
            drawnode(DISPLAYSURF, ncell, text) # draw current node (with debug text)
            osearchlist.append(ncell) # add neighbour cell to searchlist
            
            for O in osearchlist: # draw closed list on grid 
                text = "G:" + str(O.G) # build text string for debug / screen output
                text += "H:" + str(O.H)
                text += "F:" + str(O.H)
                drawnode(DISPLAYSURF, O, text, (0,128,128))    
            
            for C in oclosedlist: # draw closed list on grid 
                text = "G:" + str(C.G) # build text string for debug / screen output
                text += "H:" + str(C.H)
                text += "F:" + str(C.H)
                drawnode(DISPLAYSURF, C, text, (128,128,0))
            
            
            pygame.display.flip() # flip screen buffer
            pygame.display.update() # update display 
            
            if step > 100 or len(osearchlist)==0: # is step count exceeded or no more items to search
                bexit = 1
                break
                
            if ncell.pos == endpos: #path to endpos has been found!
                DISPLAYSURF.fill((0,0,0)) # fill screen black 
                drawgrid(DISPLAYSURF) # draw grid to screen 
                while not ncell.previouscell == "": # loop backwards through results to create / draw path
                    pygame.draw.line(DISPLAYSURF, (255,0,0), (ncell.pos[0]*GRIDX +(GRIDX/2), ncell.pos[1]*GRIDY+(GRIDY/2)), (ncell.previouscell.pos[0]*GRIDX+(GRIDX/2), ncell.previouscell.pos[1]*GRIDY+(GRIDY/2)), width=10) # draws path
                    pygame.draw.circle(DISPLAYSURF, (0,128,128),(ncell.pos[0]*GRIDX +(GRIDX/2), ncell.pos[1]*GRIDY+(GRIDY/2)) , 10) # highlights points with circles 
                    ncell = ncell.previouscell # set next ncell value to the previous object 
                pygame.display.flip() # swap screen buffer 
                pygame.display.update() # update screen
                time.sleep(3) # display results for a second                    
                bexit = 1 # exit search routine and reset 
                break # break out of loop

            if bexit: break # break out of loop if bexit = true 
            
            for event in pygame.event.get(): # check for keyboard events 
                if event.type == QUIT: # quit event
                    pygame.mixer.quit() # close pygame mixer
                    pygame.quit() # quit pygame 
                    sys.exit() # exit sys app cleanly 
                elif event.type == KEYDOWN: # check for key presses 
                    if event.key == K_ESCAPE: # close app is esc is pressed
                        pygame.mixer.quit() # close pygame mixer
                        pygame.quit() # close pygame 
                        sys.exit() # exit sys app cleanly 
                        
        oclosedlist.append(search) # add node just searched to closed list 
        try:
           osearchlist.pop(osearchlist.index(search)) # remove search node from osearchlist
        except:
           pass # skip this step on error 
        if bexit: break # if bexit = true exit search 
        
    pygame.display.flip() # swap screen buffer 
    pygame.display.update() # update screen 