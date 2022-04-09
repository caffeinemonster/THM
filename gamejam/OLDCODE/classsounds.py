import pygame
from pygame.locals import *

class csounds():  # sound effects class
    def __init__(self):  # init sound class
        self.enabled = 1  # sfx enabled
        self.volume = 0.30
        
        #LOAD SOUNDS
        self.sndeat = self.load('sfx/beep.wav')
        self.snddead = self.load('sfx/dead.wav')
        self.sndbonus = self.load('sfx/bonus.wav')
        self.sndshoot = self.load('sfx/shoot.wav')
        self.sndhitwood = self.load('sfx/hitwood.wav')
        self.sndreload = self.load('sfx/reload.wav')
    
    def toggle_enable(self):
        if self.enabled:
            self.enabled = 0  # disable sfx
            pygame.mixer.music.pause()  # stop music
        else:
            pygame.mixer.music.play()  # play music
            self.enabled = 1  # enable sfx

    def fxdead(self):  # dead
        if self.enabled:
            self.snddead.play()

    def fxeat(self):  # eat
        if self.enabled:
            self.sndeat.play()

    def fxbonus(self):  # bonus
        if self.enabled:
            self.sndbonus.play()
            
    def fxreload(self):  # bonus
        if self.enabled:
            self.sndreload.play()
            
    def fxbonus(self):  # bonus
        if self.enabled:
            self.sndbonus.play()
            
    def fxshoot(self):  # bonus
        if self.enabled:
            self.sndshoot.play()
            
    def fxhitwood(self):  # bonus
        if self.enabled:
            self.sndhitwood.play()
            
    def play(self, soundpath):
        sound = pygame.mixer.Sound(soundpath)
        if self.enabled:
            sound.play()
        return sound
            
    def load(self, soundpath):
        sound = pygame.mixer.Sound(soundpath)
        sound.set_volume(self.volume)
        return sound