# import pygame library and core modules 
import pygame, sys, time
from pygame.locals import *

# import game engine classes
from classtext import ctext
from classpathfinder import cpathfinder 
from classbackground import cbackground

# import game classes 
from classplayer import cplayer
from classlevel import clevel

class cglobal(object):
    def __init__(self):
        self.debug = 1
        # INITIALISE PYGAME
        if self.debug == 1: print("Initialise pygame.")
        pygame.init()
        pygame.mixer.init()
        
        # INITIALISE PYGAME MIXER
        if self.debug == 1: print("Initialise pygame mixer.")
        pygame.mixer.music.load('music/TRACK1.mp3')  
        pygame.mixer.music.play(-1)  
        pygame.mixer.music.set_volume(0.01)
        
        # SET CORE VARIABLES 
        if self.debug == 1: print("Initialise display surface.")
        self.DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)    
        if self.debug == 1: print("Set core variables.")
        self.DSIZEX = self.DISPLAYSURF.get_width()
        self.DSIZEY = self.DISPLAYSURF.get_height()
        self.GRIDX = 32
        self.GRIDY = 18
        self.FRAMERATE = 60
        
        if self.debug == 1: print("Set clock.")
        self.GCLOCK = pygame.time.Clock()
        
        if self.debug == 1: print("Set window caption.")
        pygame.display.set_caption('GAMEJAMMER')
        
        # INITIALISE CORE CLASSES
        if self.debug == 1: print("Initialise core classes.")
        self.background = cbackground() # core class - controls background image 
        self.text = ctext(self.DISPLAYSURF) # core class - used to render text to surfaces 
        self.pfinder = cpathfinder(self.DISPLAYSURF, (self.GRIDX, self.GRIDY))
        self.updatetimer = 0
        if self.debug == 1: print("Global initialisation complete.")
        
        # INITIALISE GAME CLASSES
        # todo add game classes.
        self.player = cplayer()
        self.player.setup(self.DISPLAYSURF, (0,0))
        self.level = clevel(self.DISPLAYSURF)
        
        # POST LOAD CONFIGURATION
        self.pfinder.grid.data = self.level.leveldata
        
    def checkkeys(self):
        # GLOBAL KEYBOARD EVENTS
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
            
    def update(self):
        self.player.update((0,0))
        self.level.update()
        self.level.collide(self.player)
        #pass # code added here to update game elements before drawing 
        
    def draw(self):
        # DRAW GAME ELEMENTS
        self.DISPLAYSURF.fill((0,0,0)) # FILL CANVAS BLACK
        self.background.draw(self.DISPLAYSURF) # DRAW BACKGROUND
        self.level.draw(self.DISPLAYSURF)
        # TEST TEXT CLASS
        #self.text.draw((200,200), (255,255,255), "HELLO WORLD")
        
        # TEST PATHFINDER CLASS
        #self.pfinder.grid.draw(self.DISPLAYSURF)

        # TEST RENDER MOUSE POS TO GRID
        #self.pfinder.grid.draw(self.DISPLAYSURF)
        mousex,mousey=pygame.mouse.get_pos()
        gridxy = self.pfinder.grid.getxy((mousex,mousey))
        if not int(self.pfinder.grid.getgridvalue(gridxy[0], gridxy[1])): self.pfinder.pos_start = gridxy
        if self.updatetimer > 250:
            self.updatetimer = 0
            self.pfinder.randomise()
        else: self.updatetimer +=1
        
        o = self.pfinder.calcpath(self.DISPLAYSURF)
        if self.debug:self.pfinder.grid.drawcell(self.DISPLAYSURF, gridxy[0], gridxy[1],(0,255,0),0,0)
        if self.debug:self.text.draw((mousex,mousey+40), (255,255,255), str((mousex,mousey)))
        
        tempcell = o
        while not tempcell == None:
            if tempcell == "": break
            if tempcell.previousnode == None: break
            if tempcell.previousnode == "": break
            if self.debug:self.pfinder.grid.drawcell(self.DISPLAYSURF, tempcell.xy[0], tempcell.xy[1], (128,255,0), 5, 4)
            if self.debug:self.pfinder.grid.drawtext(self.DISPLAYSURF, tempcell.xy[0], tempcell.xy[1], str(int(tempcell.f)), 8)
            tempcell = tempcell.previousnode
        if self.debug:self.pfinder.grid.drawcell(self.DISPLAYSURF, self.pfinder.pos_start[0], self.pfinder.pos_start[1], (0,255,0), 5, 4)
        if self.debug:self.pfinder.grid.drawcell(self.DISPLAYSURF, self.pfinder.pos_end[0], self.pfinder.pos_end[1], (255,0,0), 5, 4)
        if self.debug:self.text.draw((mousex,mousey+20), (255,255,255), str(gridxy), "")
        
        
        self.player.draw(self.DISPLAYSURF)
        
        #time.sleep(0.1)
        #pygame.display.flip()
        #pygame.display.update()
        #time.sleep(1)
        # SET START POS BASED ON MOUSE POS
        #self.pfinder.grid.drawtext(self.DISPLAYSURF, gridxy[0], gridxy[1], str(gridxy), 8)
        #self.grid.drawcell(surf, self.pos_start[0], self.pos_start[1], (0,255,0),0,0)
        #self.pfinder.create(self.DISPLAYSURF, (self.GRIDX, self.GRIDY))
        

        
        
        # UPDATE DISPLAY
        if self.debug == 1: print("Updating global display buffer.")
        pygame.display.flip() # UPDATE DISPLAY BUFFER
        pygame.display.update() # UPDATE DISPLAY BUFFER
        self.GCLOCK.tick(self.FRAMERATE) # SET FRAMERATE