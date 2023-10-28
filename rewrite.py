#copyright 2023, for now. will probably convert to open source in the future

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

        self.BG         = self.BLACK
        self.player     = self.WHITE
        self.bullet     = self.GREEN
        self.star       = self.GRAY
        self.enemy      = self.RED
        self.missile    = self.BLUE #FIXME add blue and change to blue
        self.TEXT       = self.RED

colors       = Colors()

class MyScreen():
    def __init__(self):
        self.WIDTH      = 500
        self.HEIGHT     = 500
        self.SIZE       = [self.WIDTH, self.HEIGHT]
        self.CENTER_X   = self.WIDTH/2
        self.CENTER_Y   = self.HEIGHT/2
        self.CENTER     = (self.WIDTH/2, self.HEIGHT/2)
        self.screen     = display.set_mode((self.WIDTH, self.HEIGHT))

        self.FONT_POS   = (10, 10)
        self.FONT_SIZE  = 16
        self.FONT_TYPE  = "Verdana"
        self.font_out   = pygame.font.SysFont(self.FONT_TYPE, self.FONT_SIZE) #pygame.

    def makeBackground(self):
        self.screen.fill(colors.BG)

    def do(self):
        self.makeBackground()

my_screen    = MyScreen()

class Enemy():
    def __init__(self, enemy_type):
        self.enemy_type = enemy_type


def spawn_enemy(enemy_type = "standard"):
    pass
    #FIXME: create instance





objects_with_do_method = [my_screen]

#main loop
while(True):
    for a in objects_with_do_method:
        for b in a:
            b.do()
