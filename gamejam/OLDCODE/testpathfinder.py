import pygame, sys, time, random
from pygame.locals import *
from classgrid import cgrid
from classpathfinder import cpathfinder


pygame.init()
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('PATHFINDERTEST!') # set window caption

ogrid = cgrid(32,18,DISPLAYSURF) # create new grid class 
ogrid.create() # create a new grid

opf = cpathfinder()
opf.data = ogrid.data

startpos = ogrid.getrandomcell() # pick random cell 
endpos = ogrid.getrandomcell() # pick random cell 
        
while endpos == startpos: # make sure endpos is not startpos 
    endpos = ogrid.getrandomcell() # get new end pos 

update = 0 # variable to time updates

while True: # main game loop
    DISPLAYSURF.fill((0,0,0))
    startpos = ogrid.getrandomcell() # pick random cell 
    endpos = ogrid.getrandomcell() # pick random cell 
    ogrid.drawgrid(DISPLAYSURF) # draw grid
    opf.data = ogrid.data
    bstop = 0
    while not bstop: # make sure endpos is not startpos 
        endpos = ogrid.getrandomcell() # get new end pos 
        if not int(ogrid.getgridvalue(endpos[0], endpos[1])):
            if not(endpos == startpos):
                bstop = 1
    
    opf.data = ogrid.data
    opf.initialise(DISPLAYSURF)
    cellpath = opf.calcpath(startpos, endpos, DISPLAYSURF)    
    
    
    tempcell = cellpath
    while not tempcell.previouscell == "":
        ogrid.drawcell(DISPLAYSURF, tempcell.pos[0], tempcell.pos[1], (255,0,0),0,0)
        
        #pygame.draw.circle(DISPLAYSURF, (0,255,0),(startpos[0]*ogrid.cellwidth +(ogrid.cellwidth/2), startpos[1]*ogrid.cellheight+(ogrid.cellheight/2)) , 10) # highlights points with circles 
        #pygame.draw.circle(DISPLAYSURF, (0,0,255),(endpos[0]*ogrid.cellwidth +(ogrid.cellwidth/2), endpos[1]*ogrid.cellheight+(ogrid.cellheight/2)) , 10) # highlights points with circles 
        pygame.draw.line(DISPLAYSURF, (128,128,128), (tempcell.pos[0]*ogrid.cellwidth +(ogrid.cellwidth/2), tempcell.pos[1]*ogrid.cellheight+(ogrid.cellheight/2)), (tempcell.previouscell.pos[0]*ogrid.cellwidth+(ogrid.cellwidth/2), tempcell.previouscell.pos[1]*ogrid.cellheight+(ogrid.cellheight/2)), width=4) # draws path
        pygame.draw.circle(DISPLAYSURF, (0,255,0),(tempcell.pos[0]*ogrid.cellwidth +(ogrid.cellwidth/2), tempcell.pos[1]*ogrid.cellheight+(ogrid.cellheight/2)) , 5) # highlights points with circles 
        tempcell = tempcell.previouscell
        
    pygame.draw.circle(DISPLAYSURF, (0,255,0),(startpos[0]*ogrid.cellwidth +(ogrid.cellwidth/2), startpos[1]*ogrid.cellheight+(ogrid.cellheight/2)) , 10) # highlights points with circles 
    pygame.draw.circle(DISPLAYSURF, (0,0,255),(endpos[0]*ogrid.cellwidth +(ogrid.cellwidth/2), endpos[1]*ogrid.cellheight+(ogrid.cellheight/2)) , 10) # highlights points with circles 
        
    ogrid.create()
    for event in pygame.event.get(): # handle keyboard events
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.mixer.quit()
                pygame.quit()
                sys.exit()
                
    pygame.display.flip() # flip display buffer 
    pygame.display.update() # update display 
    time.sleep(1) # display results for a second     