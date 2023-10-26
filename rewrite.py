from sys import exit
import pygame
import random

class Colors():
    def __init__(self):
        self.WHITE      = (255,     255,    255 )
        self.BLACK      = (0,       0,      0   )
        self.RED        = (230,     0,      100 )           
        self.GREEN      = (0,       204,    0   )
        self.BLUE       = (117,     182,    243 )

        self.bg         = self.BLACK
        self.player     = self.WHITE
        self.bullet     = self.GREEN
        self.star       = self.GRAY
        self.enemy      = self.RED
        self.missile    = self.BLUE #FIXME add blue and change to blue
        self.TEXT       = self.RED

colors       = Colors()

#main loop
while(True):
    pass