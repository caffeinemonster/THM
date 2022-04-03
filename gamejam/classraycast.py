import random, pygame, sys, math  # import required librarys 
from pygame.locals import * # import pygame constants 
from classgrid import cgrid 

class craycast(object):
    def __init__(self, surf):
        self.grid = cgrid(10,10,surf)
        self.grid.create()
        self.surf = surf
        self.angle = math.pi
        self.xy = (surf.get_width() / 2,surf.get_height()/2)
        
        self.FOV = math.pi / 3
        self.HALF_FOV = self.FOV / 2
        self.CASTED_RAYS = 32
        self.STEP_ANGLE = self.FOV / self.CASTED_RAYS
        self.MAX_DEPTH = 100
        
        #int(self.grid.x * self.grid.cellwidth)/3
        
    
    def checkkeys(self):    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: self.angle -= 0.1
        if keys[pygame.K_RIGHT]: self.angle += 0.1
        if keys[pygame.K_UP]:
            self.xy = (self.xy[0] - math.sin(self.angle) * 5, self.xy[1])
            self.xy = (self.xy[0], self.xy[1] + math.cos(self.angle) * 5)
        if keys[pygame.K_DOWN]:
            self.xy = (self.xy[0] + math.sin(self.angle) * 5, self.xy[1])
            self.xy = (self.xy[0], self.xy[1] - math.cos(self.angle) * 5)
            
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
    
    def draw(self, surf):
        surf.fill((0,0,0))
        for y in range(0, len(self.grid.data)):
            for x in range(0, len(self.grid.data[0].split(','))):
                if not int(self.grid.getgridvalue(x, y)): continue
                rect = (x * self.grid.cellwidth, y * self.grid.cellheight, self.grid.cellwidth, self.grid.cellheight)
                pygame.draw.rect(surf, (255,255,255), rect)
        pygame.draw.circle(surf, (0,0,255), self.xy, 10) # player xy 
        pygame.draw.line(surf, (0, 255, 0), (self.xy[0], self.xy[1]),
                                       (self.xy[0] - math.sin(self.angle) * 50,
                                        self.xy[1] + math.cos(self.angle) * 50), 3)
                                        
        pygame.draw.line(surf, (0, 255, 0), (self.xy[0], self.xy[1]),
                                       (self.xy[0] - math.sin(self.angle - self.HALF_FOV) * 50,
                                        self.xy[1] + math.cos(self.angle - self.HALF_FOV) * 50), 3)                                         
        
        pygame.draw.line(surf, (0, 255, 0), (self.xy[0], self.xy[1]),
                                       (self.xy[0] - math.sin(self.angle + self.HALF_FOV) * 50,
                                        self.xy[1] + math.cos(self.angle + self.HALF_FOV) * 50), 3)
        self.castrays(surf)
        
    def castrays(self, surf):
        fangle = self.angle - self.HALF_FOV
        for ray in range(self.CASTED_RAYS):
            for depth in range(self.MAX_DEPTH):
                target_x = self.xy[0] - math.sin(fangle) * depth
                target_y = self.xy[1] + math.cos(fangle) * depth
                col = int(target_x / self.grid.cellwidth)
                row = int(target_y / self.grid.cellheight)
                pygame.draw.line(surf, (255, 255, 0), (self.xy[0], self.xy[1]), (target_x, target_y))
                if int(self.grid.getgridvalue(col, row)):
                    pygame.draw.rect(surf, (0, 255, 0), (col * self.grid.cellwidth,
                                                        row * self.grid.cellheight,
                                                        self.grid.cellwidth,
                                                        self.grid.cellheight))
                    
                    break
            fangle += self.STEP_ANGLE

                
        