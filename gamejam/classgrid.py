import random, pygame, math
from pygame.locals import *
from classtext import ctext
class cgrid():
    def __init__(self, x, y, surf):
        self.otext = ctext(surf)
        self.data = []
        self.x = x 
        self.y = y 
        self.width = surf.get_width()
        self.height = surf.get_height()
        self.cellwidth = int(self.width / x)
        self.cellheight = int(self.height / y)
        
    def configure(self, x, y, surf):
        self.x = x
        self.y = y
        self.width = surf.get_width()
        self.height = surf.get_height()
        self.cellwidth = int(self.width / x)
        self.cellheight = int(self.height / y)
        self.data = []
    
    def fill(val):
        self.data = []
        s = ""
        y = 0 # loop variable for x position 
        while y <= self.y: # loop through x grid size 
            y +=1 
            if not s == "": # add data if data exists 
                self.data.append(s)
            x = 0 # define variable for y axis loop 
            s = "" # reset row data 
            s = val
            while x < self.x-1: # loop through y grid size 
                s += "," + str(val) # fill with value
                x += 1 
        return self.data
        
            
    
    def getgriddata(self): # returns grid variables as a text string used for debugging
        sreturn = [attr for attr in dir(self) if not callable(getattr(self,attr)) and not attr.startswith("__")]
        for property, value in vars(self).items():
            sreturn += str(property) + ":" + str(value)
        return sreturn 
        
    def getgridvalue(self, x, y): 
        # return grid value from x y pos (wall or not wall) 
        # also return 1 if OB 
        if x < 0: return 1
        if y < 0: return 1
        if x > self.x: return 1
        if y > self.y: return 1
        try:
            return int(self.data[y].split(',')[x])
        except:
            return 1
    
    def getxy(self, xypos): # retruns grid co-ords
        for y in range(0, self.y):
            for x in range(0, self.x):
                if xypos[0] <= (x * self.cellwidth) + self.cellwidth:
                    if xypos[1] <= (y * self.cellheight) + self.cellheight:
                        return (x, y)
                        
    def getxylocation(self, xypos):
        return pygame.Vector2((xypos[0] * self.cellwidth, xypos[1] * self.cellheight))
        
    def getrandomcell(self, itype = 0): # get a random cell that isnt a wall (1)
        T = (random.randint(0, self.x-1), random.randint(0, self.y-1))
        if itype == 0:
            while self.getgridvalue(T[0],T[1]):
                T = (random.randint(0, self.x-1), random.randint(0, self.y-1))
            return T
        
        if itype == 1:
            while not self.getgridvalue(T[0],T[1]):
                T = (random.randint(0, self.x-1), random.randint(0, self.y-1))
            return T
        
    def create(self): # create grid
        self.data = []
        s = ""
        y = 0 # loop variable for x position 
        while y <= self.y: # loop through x grid size 
            y +=1 # increment x var 
            if not s == "": # add data if data exists 
                self.data.append(s)
            x = 0 # define variable for y axis loop 
            s = "" # reset row data 
            s = str("0" if (random.randint(0,100)<75) else "1") # create 1st value in row 
            while x < self.x-1: # loop through y grid size 
                s += "," + str("0" if (random.randint(0,100)<75) else "1") # create wall / not wall area 
                x += 1 # increment y
        return self.data
    
    def calculatedistance(self, pos1, pos2): # calculate distance between cells
        AB = pygame.Vector2(pos1) - pygame.Vector2(pos2) # subtract positions to get xy distance  
        C = math.sqrt(AB[0]**2 + AB[1]**2) # pythagorus (calculates distance between pos1 and pos2)
        return C

    def drawtext(self, surf, x, y, text, size): # used to draw cells 
        # def draw(self, xy, colour, text, align = ""):
        self.otext.draw(((x*self.cellwidth), (y*self.cellheight) + (self.cellheight/2)),(255,255,255), text,"")
   
    def drawcell(self, surf, x, y, colour, border, curve): # used to draw cells 
        if not (border and curve):
            pygame.draw.rect(surf, colour, 
                            (x*self.cellwidth, y*self.cellheight, 
                            self.cellwidth, self.cellheight))
        else:
            pygame.draw.rect(surf, colour, 
                            (x*self.cellwidth, y*self.cellheight, 
                            self.cellwidth, self.cellheight), 
                            border, curve)
        
    def draw(self, surf): # draws the generated grid to the screen
        for y in range(0, len(self.data)):
            for x in range(0, len(self.data[y].split(','))):
                if int(self.data[y].split(',')[x]):
                    self.drawcell(surf, x, y, (255,255,255), 0, 0) # draw wall 
                    self.drawcell(surf, x, y, (128,0,0), 1, 1)
                else:
                    self.drawcell(surf, x, y, (128,0,0), 1, 1) # draw not wall