import random, pygame, math
from pygame.locals import *
from classtext import ctext
class cgrid():
    def __init__(self, x, y, surf):
        self.otext = ctext()
        self.data = []
        self.x = x 
        self.y = y 
        #self.width = 0
        #self.height = 0
        #self.cellwidth = 0
        #self.cellheight = 0
        self.width = surf.get_width()
        self.height = surf.get_height()
        self.cellwidth = self.width / x
        self.cellheight = self.height / y
        
    def configure(self, x, y, surf):
        self.x = x
        self.y = y
        self.width = surf.get_width()
        self.height = surf.get_height()
        self.data = []
        
        #self.cellwidth = 0
        #self.cellheight = 0
        
        #if surf == "":return
        #self.width = surf.get_width()
        #self.height = surf.get_height()
        #self.cellwidth = self.width / x
        #self.cellheight = self.height / y
        
    def getgriddata(self): # returns grid variables as a text string used for debugging
        sreturn = [attr for attr in dir(self) if not callable(getattr(self,attr)) and not attr.startswith("__")]
        for property, value in vars(self).items():
            sreturn += str(property) + ":" + str(value)
        return sreturn 
        
    def getgridvalue(self, x, y): # return grid value from x y pos (wall or not wall)
        if x < 0: return 1
        if y < 0: return 1
        if x > self.x: return 1
        if y > self.y: return 1
        try:
            return int(self.data[y].split(',')[x])
        except:
            return 1
    
    def getxy(self, xypos):
        for y in range(0, self.y - 1):
            for x in range(0, self.x - 1):
                if xypos[0] <= (x * self.cellwidth):
                    if xypos[1] <= (y * self.cellheight):
                        return (x-1,y-1)
                        
    def getxylocation(self, xypos):
        # print(xypos[0])
        # print(xypos[1])
        # print("CW : " + str(self.cellwidth))
        # print("CH : " + str(self.cellheight))
        return pygame.Vector2((xypos[0] * self.cellwidth, xypos[1] * self.cellheight))
        
    def getrandomcell(self): # get a random cell that isnt a wall 
        T = (random.randint(0, self.x), random.randint(0, self.y))
        while self.getgridvalue(T[0],T[1]):
            T = (random.randint(0, self.x), random.randint(0, self.y))
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
        pos1 = pygame.Vector2(pos1)
        pos2 = pygame.Vector2(pos2)
        AB = pygame.Vector2(pos1) - pygame.Vector2(pos2) # subtract positions to get xy distance  
        C = math.sqrt(AB[0]**2 + AB[1]**2) # pythagorus (calculates distance between pos1 and pos2)
        return C

    def drawtext(self, surf, x, y, text, size): # used to draw cells 
        self.otext.draw(surf,text,(x*self.cellwidth, y*self.cellheight),(255,255,255),255,size)
   
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
        
    def drawgrid(self, surf): # draws the generated grid to the screen
        for y in range(0, len(self.data)):
            for x in range(0, len(self.data[y].split(','))):
                if int(self.data[y].split(',')[x]):
                    self.drawcell(surf, x, y, (255,255,255), 0, 0) # draw wall 
                    self.drawcell(surf, x, y, (128,0,0), 1, 1)
                else:
                    self.drawcell(surf, x, y, (128,0,0), 1, 1) # draw not wall
    
