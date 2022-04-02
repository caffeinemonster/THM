import pygame, time, sys, random
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

DSIZEX = DISPLAYSURF.get_width()
DSIZEY = DISPLAYSURF.get_height()

DATA = ["0,0,0,0,0,0,0,0,0,0",
        "0,0,0,0,0,0,0,0,0,0",
        "0,0,0,0,0,0,0,0,0,0",
        "0,0,0,0,0,0,0,0,0,0",
        "0,0,0,0,0,0,0,0,0,0",
        "0,0,0,0,0,0,0,0,0,0",
        "0,0,0,0,0,0,0,0,0,0",
        "0,0,0,0,0,0,0,0,0,0",
        "0,0,0,0,0,0,0,0,0,0",
        "0,0,0,0,0,0,0,0,0,0"]

GRIDSIZEX = len(DATA[0].split(","))
GRIDSIZEY = len(DATA)

GRIDX = DSIZEX / GRIDSIZEX
GRIDY = DSIZEY / GRIDSIZEY

GCLOCK = pygame.time.Clock()  # set game clock


#tartpos = (random.randint(0, GRIDSIZEX), random.randint(0, GRIDSIZEX))
#ndpos = (random.randint(0, GRIDSIZEX), random.randint(0, GRIDSIZEX))

endpos = (9,9)
#global path 
path = [[(0,0)]]
def getrandomcell():
    ireturn = (random.randint(0, GRIDSIZEX), random.randint(0, GRIDSIZEY))
    while getgridvalue(ireturn[0],ireturn[1]):
        ireturn = (random.randint(0, GRIDSIZEX), random.randint(0, GRIDSIZEY))
    return ireturn


    
def findpath(surf):
    #if len(path) == 0:
        #path[0][0] = startpos
        
        
    
    # draw grid 
    
    #while getgridvalue(startpos[0],startpos[0]):
        #startpos = (random.randint(0, GRIDSIZEX), random.randint(0, GRIDSIZEX))
    #endpos = (random.randint(0, GRIDSIZEX), random.randint(0, GRIDSIZEX))
    #while getgridvalue(endpos[0],endpos[0]):
    #    endpos = (random.randint(0, GRIDSIZEX), random.randint(0, GRIDSIZEX))
    startpos = getrandomcell()
    endpos = getrandomcell()
    direction = 0 # 0left 1right 2up 3down
    steps = 0
    
    while True:
        
        pygame.display.flip()
        pygame.display.update()
        steps +=1
        directionstep = 1
        #time.sleep(1)
        for y in range(0, GRIDSIZEY):
            for x in range(0, GRIDSIZEX):
                # draw cube 
                #print(str((x,y)))
                if int(DATA[y].split(',')[x]):
                    drawcell(DISPLAYSURF, x, y, (255,255,255), 1, 4)
                    #pygame.draw.rect(DISPLAYSURF, (255,255,255), (x*GRIDX, y*GRIDY, GRIDX, GRIDY))
                else:
                    drawcell(DISPLAYSURF, x, y, (255,0,0), 1, 4)
                    #pygame.draw.rect(DISPLAYSURF, (255,0,0), (x*GRIDX, y*GRIDY, GRIDX, GRIDY), 1,4)
                    
                #if (x,y) == startpos: pygame.draw.rect(DISPLAYSURF, (0,255,0), (x*GRIDX, y*GRIDY, GRIDX, GRIDY), 1,4)
                if (x,y) == startpos: drawcell(DISPLAYSURF, x, y, (0,255,0), 10, 4)
                
                #if (x,y) == endpos: pygame.draw.rect(DISPLAYSURF, (0,0,255), (x*GRIDX, y*GRIDY, GRIDX, GRIDY), 1,4)
                if (x,y) == endpos: drawcell(DISPLAYSURF, x, y, (0,0,255), 10, 4)
        
        for ipath in range(0,len(path)):
            #time.sleep(100)
            print("ipath = " + str(ipath))
            seekpos = path[ipath][len(path[ipath])-1]
            print("seek pos = " + str(seekpos))
            print("seeking = end pos")
            
            
            if steps >= 500: # path found
                print("path NOT found")
                path[ipath].append(endpos)
                #path[ipath][len(path[ipath])+1].append(endpos)
                highlightcell(surf, seekpos[0], seekpos[1], (128,128,128))
                #path = [[(0,0)],[(0,0)],[(0,0)],[(0,0)]]
                path[0] = [startpos]
                endpos = getrandomcell()
                startpos = getrandomcell()
                path[ipath] = [startpos]
                DISPLAYSURF.fill((0,0,0))
                steps = 0
                break 
                
            if seekpos == endpos: # path found
                time.sleep(5)
                print("path found")
                path[ipath].append(endpos)
                #path[ipath][len(path[ipath])+1].append(endpos)
                highlightcell(surf, seekpos[0], seekpos[1], (128,128,128))
                #path = [[(0,0)],[(0,0)],[(0,0)],[(0,0)]]
                path[0] = [startpos]
                endpos = getrandomcell()
                startpos = getrandomcell()
                path[ipath] = [startpos]
                DISPLAYSURF.fill((0,0,0))
                steps = 0
                break 
    
            if direction == 0:            
                if not getgridvalue(seekpos[0]+1, seekpos[1]): # can move right
                    print("can move right")
                    #path[ipath][len(path[ipath])+1].append(seekpos[0]+1, seekpos[1])
                    #if not isinpath(path[ipath], (seekpos[0]+1, seekpos[1])):
                    path[ipath].append((seekpos[0]+1, seekpos[1]))
                    highlightcell(surf, seekpos[0]+1, seekpos[1], (128,128,128))
                    break
                    
            if direction == 1:
                if not getgridvalue(seekpos[0], seekpos[1]+1): # can move down
                    print("can move down")
                    #if not isinpath(path[ipath], (seekpos[0], seekpos[1]+1)):
                    path[ipath].append((seekpos[0], seekpos[1]+1))
                    highlightcell(surf, seekpos[0], seekpos[1]+1, (128,128,128))
                    break
                

            if direction == 2:
                if not getgridvalue(seekpos[0]-1, seekpos[1]): # can move left
                    print("can move left")
                    #if not isinpath(path[ipath], (seekpos[0]-1, seekpos[1])):
                    path[ipath].append((seekpos[0]-1, seekpos[1]))
                    highlightcell(surf, seekpos[0]-1, seekpos[1], (128,128,128))
                    break
                

            if direction == 3:
                if not getgridvalue(seekpos[0], seekpos[1]-1): # can move up 
                    print("can move up")
                    #if not isinpath(path[ipath], (seekpos[0], seekpos[1]-1)):
                    path[ipath].append((seekpos[0], seekpos[1]-1))
                    highlightcell(surf, seekpos[0], seekpos[1]-1, (128,128,128))
                    break
                
                    
            
            
            if direction > 3: direction = 0
                
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
 
def pathseek(checkpos, ipath):
    if not getgridvalue(checkpos[0], checkpos[1]): # can move up 
        print("can move up")
        #path[ipath][len(path[ipath])+1].append(seekpos[0], seekpos[1]-1)
        if not isinpath(path[ipath], (checkpos[0], checkpos[1])):
            path[ipath].append((checkpos[0], checkpos[1]))
            highlightcell(surf, checkpos[0], checkpos[1], (128,128,128))
            return 1
    return 0
    
def isinpath(path, xy):
    if xy in path: 
        return 1
    else:
        return 0
    
def getgridvalue(x,y):
    if x < 0: return 1
    if y < 0: return 1
    try:
        return int(DATA[y].split(',')[x])
    except:
        return 1
def highlightcell(surf, x, y, colour):
    pygame.draw.rect(surf, colour, (x*GRIDX, y*GRIDY, GRIDX, GRIDY), 12, 12)
    
def drawcell(surf, x, y, colour, border, curve):
    pygame.draw.rect(DISPLAYSURF, colour, (x*GRIDX, y*GRIDY, GRIDX, GRIDY), border, curve)

while True: # main game loop
    DISPLAYSURF.fill((0,0,0)) # fill canvas black
    findpath(DISPLAYSURF)
    GCLOCK.tick(60)   

    
    