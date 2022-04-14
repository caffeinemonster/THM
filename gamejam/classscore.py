import pygame
from pygame.locals import *

class cscore():  # score class
    def __init__(self):
        self.score = 0  # var to hold score

    def add(self, s):  # add score
        self.score = self.score + s