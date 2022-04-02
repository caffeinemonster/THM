import pygame, sys, random, time
from classtext import ctext
from classbackground import cbackground
from classsounds import csounds
from classplayer import cplayer

from classparticles import cparticles
from classparticlecontroller import cparticlecontroller
from classprojectile import cprojectile
from classprojectiles import cprojectiles
from classtarget import ctarget 
from classlevel import clevel
from pygame.locals import *

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('music/TRACK1.mp3')  # queue random track
pygame.mixer.music.play()  # play music
pygame.mixer.music.set_volume(0.05)


DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
DSIZEX = DISPLAYSURF.get_width()
DSIZEY = DISPLAYSURF.get_height()

GCLOCK = pygame.time.Clock()  # set game clock
pygame.display.set_caption('FUTURA')


projectiles = cprojectiles()
particles = cparticles() # particle group
pcollection = cparticlecontroller()



olevel = clevel()
#olevel.offset = pygame.Vector2(0,0)
obackground = cbackground()
oplayer = cplayer()
otext = ctext()
sfx = csounds()

olevel.offset[0] =  DISPLAYSURF.get_width() / 2 - olevel.levelsize[0] / 2
olevel.offset[1] =  DISPLAYSURF.get_height() / 2 - olevel.levelsize[1] / 2
#oplayer.pos[0] = (DISPLAYSURF.get_width() / 2) + olevel.offset[0]
#oplayer.pos[1] = (DISPLAYSURF.get_height() / 2) + olevel.offset[1]
oplayer.pos = pygame.Vector2(oplayer.pos)
oplayer.poslast = oplayer.pos
oplayer.target = oplayer.pos
oplayer.setup(DISPLAYSURF, olevel.offset)

targets = []
icount = 1

while True: # main game loop
                  
    DISPLAYSURF.fill((0,0,0)) # fill canvas black
    obackground.draw(DISPLAYSURF)
    projectiles.collide(DISPLAYSURF, olevel.targets, pcollection, olevel.offset)
    
    
    for targ in olevel.targets:
       targ.collide(DISPLAYSURF, olevel.targets, oplayer, pcollection, projectiles, olevel.offset)
    olevel.killtargets(pcollection)
    
    bshoot = 0 
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
            if event.key == K_r:
                # reload mag 
                if not projectiles.magcurrent == projectiles.magsize:
                    projectiles.reload = projectiles.reloadtime
                    projectiles.ammo = projectiles.ammo
                    projectiles.magcurrent = 0

    keys = pygame.key.get_pressed()
    xy = 0 # move in x or y direction 0=x 1=y 
    islide = 0 # variable to store positive negative slide value depending on keypress
    slideamount = 10 # amount to increment sceen slide amount 
        
    if pygame.mouse.get_pos()[1] == 0 or keys[K_w]: #slide up 
        xy = 1
        islide = +slideamount
                
    if pygame.mouse.get_pos()[1] == DISPLAYSURF.get_height()-1 or keys[K_s]: #slide down 
        xy = 1
        islide = -slideamount
    
    if pygame.mouse.get_pos()[0] == DISPLAYSURF.get_width()-1 or keys[K_d]: #slide right 
        xy = 0
        islide = -slideamount
    
    if pygame.mouse.get_pos()[0] == 0 or keys[K_a]: #slide left 
        xy = 0
        islide = +slideamount
        
    if islide:
        if not oplayer.pos == oplayer.target:
            oplayer.slide(-islide,xy)
        else:
            oplayer.slide(-islide*.5,xy)
        projectiles.slide(+islide,xy)
        olevel.offset[xy] += islide
        olevel.collide(oplayer, pcollection)
        #oplayer.update(olevel.offset)
        #else:
        #    olevel.collide(oplayer, pcollection)

        if keys[K_SPACE]:
            bshoot = 1
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1: # left click
                oplayer.set_target(pygame.mouse.get_pos() + pygame.Vector2(oplayer.image.get_width() / 2, oplayer.image.get_width() / 2))
            if event.button == 3: # right click
                bshoot = 1
    
    state = pygame.mouse.get_pressed()
    if state[2] == 1: bshoot = 1 # right button pressed
    if bshoot: projectiles.seed(oplayer.playercenter[0],oplayer.playercenter[1],1,(255,255,255),oplayer.rotation,pygame.mouse.get_pos(),pcollection)
    
    

    olevel.draw(DISPLAYSURF)
    

    # add code for osd 
    otext.draw( DISPLAYSURF, 
    "Lives:(" + str(oplayer.lives) + ")" + 
    "Health:(" + str(oplayer.health) + ")" + 
    "Ammo:(" + str(projectiles.ammo) + ")" + 
    "Magazine:(" + str(projectiles.magcurrent) + ")" 
    , (0,0), (255,255,255), (200), 50, "centerbottom")
    
    if oplayer.lives <= 0:
        oplayer.lives = 0
        otext.draw( DISPLAYSURF, 
        "GAME OVER" 
        , (0,0), (255,255,255), (200), 200, "center")

    olevel.drawtargets(DISPLAYSURF)
    
    olevel.collide(oplayer, pcollection)
    olevel.updatetargets(oplayer)
    oplayer.update(olevel.offset)
    projectiles.draw(DISPLAYSURF, pcollection)
    oplayer.draw(DISPLAYSURF)
    
    pcollection.draw(DISPLAYSURF)
    pygame.display.flip()
    pygame.display.update()    
    GCLOCK.tick(60) 