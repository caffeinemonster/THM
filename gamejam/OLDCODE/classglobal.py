import pygame, sys
from pygame.locals import *
from classbackground import cbackground
from classlevel import clevel
from classplayer import cplayer
from classgrid import cgrid
from classtext import ctext
from classparticlecontroller import cparticlecontroller

class cglobal(object):
    def __init__(self):
        # INITIALISE PYGAME 
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load('music/TRACK1.mp3')  
        pygame.mixer.music.play()  
        pygame.mixer.music.set_volume(0.05)
        
        # SET CORE VARIABLES 
        self.DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)    
        self.DSIZEX = self.DISPLAYSURF.get_width()
        self.DSIZEY = self.DISPLAYSURF.get_height()
        self.GCLOCK = pygame.time.Clock()
        pygame.display.set_caption('GAMEJAMMER')
        
        # INITIALISE CLASSES
        self.background = cbackground()
        self.particles = cparticlecontroller()
        self.level = clevel()
        self.player = cplayer()
        self.targets = []
        self.otext = ctext()
        
        # CONFIGURE CLASS
        self.player.setup(self.DISPLAYSURF, self.level.offset)
    
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
            # CHECK PLAYER KEYS
            self.player.checkkeys(event)
            
        # SLIDE SCREEN CALCULATIONS
        keys = pygame.key.get_pressed()
        islide = 0
        xy = 0
        slideamount = 20
        if pygame.mouse.get_pos()[1] == 0 or keys[K_w]: #slide up 
            xy = 1
            islide = +slideamount
        if pygame.mouse.get_pos()[1] == self.DISPLAYSURF.get_height()-1 or keys[K_s]: #slide down 
            xy = 1
            islide = -slideamount
        if pygame.mouse.get_pos()[0] == self.DISPLAYSURF.get_width()-1 or keys[K_d]: #slide right 
            xy = 0
            islide = -slideamount
        if pygame.mouse.get_pos()[0] == 0 or keys[K_a]: #slide left 
            xy = 0
            islide = +slideamount
        
        if islide:
            # SET LEVEL OFFSET 
            self.level.offset[xy] += islide
            # SLIDE PLAYER 
            self.player.target = self.player.pos
            self.player.slide(-islide/2 ,xy)
            self.player.projectiles.slide(+islide,xy)
                    
    def update(self):
        # UPDATE GAME ELEMENTS       
        self.player.projectiles.collide(self.DISPLAYSURF, self.level.targets, self.particles, self.level.offset) # CHECK PLAYER BULLET COLLISIONS
        self.level.updatetargets(self.player, self.DISPLAYSURF) 
        self.player.update(self.level.offset) # MOVE PLAYER 
        self.level.collide(self.player, self.particles)  # CHECK PLAYER / LEVEL COLLISIONS
        
        # UPDATE TARGETS
        for t in self.level.targets:
            #print("targetcollide")
            #t.opf.data = self.level.leveldata
            #t.opf.grid.cellwidth = (self.DISPLAYSURF.get_width() / self.level.tilesize[0])
            #t.opf.grid.cellheight = (self.DISPLAYSURF.get_height() / self.level.tilesize[1])
            #    def collide(self, level, player, pcollection):
            
            t.collide(self.level, self.player, self.particles, self.DISPLAYSURF)
        self.level.killtargets(self.particles) # REMOVE OLD TARGETS 
        
    def draw(self):
        # DRAW GAME ELEMENTS 
        self.DISPLAYSURF.fill((0,0,0)) # FILL CANVAS BLACK
        self.background.draw(self.DISPLAYSURF) # DRAW BACKGROUND
        self.level.draw(self.DISPLAYSURF) # DRAW LEVEL
        self.player.draw(self.DISPLAYSURF) # DRAW PLAYER
        
        
        self.otext.draw(self.DISPLAYSURF, "XY:" + str(self.level.pfinder.grid.getxy(self.player.pos - self.level.offset)), (self.player.pos[0], self.player.pos[1]+50),(255,0,0),255, 18, "")
        for t in self.level.targets:
            t.draw(self.DISPLAYSURF, self.level.offset) # DRAW TARGETS
        
        # UPDATE DISPLAY
        pygame.display.flip() # UPDATE DISPLAY BUFFER
        pygame.display.update() # UPDATE DISPLAY BUFFER
        self.GCLOCK.tick(60) # SET FRAMERATE 