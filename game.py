"""
        Space 460 /\
            hellmak @ GitHub
copyright 2021, 2023
"""
#import
from sys import exit
from pygame import *
import pygame
import random

pygame.init()

#title
display.set_caption("Space 460")

######### ######### #########
##      2023 rewrite       ##
##          start          ##
######### ######### #########

INVINCIBILITY   = True # for troubleshooting
MAX_LIST_ITEMS  = 10
MAX_OFFSCREEN_WIDTH     = 100 #(my_screen.WIDTH) / 2
MAX_OFFSCREEN_HEIGHT    = 10

def remove_offscreen_list_items(input_list):
    items_to_remove = []
    for item in input_list:
        x, y = item.pos
        if not (-MAX_OFFSCREEN_WIDTH <= x <= MAX_OFFSCREEN_WIDTH) and (-MAX_OFFSCREEN_HEIGHT <= y <= MAX_OFFSCREEN_HEIGHT):
            items_to_remove.append(item)

    for item in items_to_remove:
        input_list.remove(item)

def enforce_list_size(input_list):
    while len(input_list) > MAX_LIST_ITEMS:
        del input_list[0]





######### ######### #########
##      2023 rewrite       ##
##           end           ##
######### ######### #########

#classes
class Color():
    def __init__(self):
        self.WHITE      = (255,     255,    255 )
        self.BLACK      = (0,       0,      0   )
        self.RED        = (230,     0,      100 )            #looks dope, must use if game uses colors in future.
        self.GRAY       = (153,     153,    153 )
        self.GREEN      = (0,       204,    0   )
        self.BLUE       = (117,     182,    243 )

        self.bg         = self.BLACK
        self.player     = self.WHITE
        self.bullet     = self.GREEN
        self.star       = self.GRAY
        self.enemy      = self.RED
        self.missile    = self.BLUE #FIXME add blue and change to blue
        self.TEXT       = self.RED

color       = Color()

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
        self.screen.fill(color.bg)

    def do(self):
        self.makeBackground()

my_screen    = MyScreen()

class Player():
    def __init__(self):
        self.pos        = [my_screen.CENTER_X,  my_screen.HEIGHT  - 50]
        self.size       = (16,  16)
        self.limit      = [(0), (my_screen.WIDTH - self.size[0]), (0), (my_screen.HEIGHT - self.size[1])]    #FIXME should be a two layer: ((x min, x max), (y min, y max))
        self.speed      = (5,   0)         #no y movement
        self.box        = Rect(self.pos, self.size)
        self.auto_fire  = False
        self.kills      = 0
        self.points     = 0
        self.lives      = 3 #for future updates

    #movement and shooting
    def move(self):
        keys    = pygame.key.get_pressed() # added pygame. for clarity

        if  keys[K_LEFT]    and self.pos[0] >= self.limit[0]:
            self.pos[0] -= self.speed[0]
            #print("left")
        if  keys[K_RIGHT]   and self.pos[0] <= self.limit[1]:
            self.pos[0] += self.speed[0]
            #print("right")

        if(keys[K_UP])      and self.pos[1] >= self.limit[2]:
            self.pos[1] -= self.speed[1]
            print("up")
        if(keys[K_DOWN])    and self.pos[1] <= self.limit[3]:
            self.pos[1] += self.speed[1]
            print("down")

        #y movement removed in self.speed[1]

    def draw(self):
        draw.rect(my_screen.screen, color.player, Rect(self.pos, self.size))
    
    def do(self):
        self.draw()
        self.move()

player      = Player()


class PlayerAmmo(object):
    def __init__(self):
        self.size       = [3,3]
        self.pos        = [(  player.pos[0] + ( (player.size[0]/2) - (self.size[0]/2) )  ), (player.pos[1] - player.size[0] - 1)]
        self.speed      = 2
        self.damage     = 1


    def draw(self):
        draw.rect(my_screen.screen, color.bullet, Rect(self.pos, self.size))

    def do(self):
        self.draw()

player_ammo = PlayerAmmo()                  #FIXME lazy temp for passing values to Star


class BgStar(object):
    def __init__(self):
        self.size_x = random.randint(1,5)   #FIX ME: wonky property name
        self.size   = [self.size_x,self.size_x]
        self.pos    = [random.randint((-10), (my_screen.WIDTH + 11)),-self.size[1]]
        self.speed  = round(random.uniform(0.5, 3), 3)
        self.damage = 1

    def draw(self):
        draw.rect(my_screen.screen, color.star, Rect(self.pos, self.size))
    
    def do(self):
        self.draw()


bg_star     = BgStar()                          #FIXME lazy temp for passing values to Star

class Enemy(object):
    def __init__(self, type = "standard", direction = "center", alt_pos = [0, 0]):
        self.size_x     = random.randint(10,12)   #FIX ME: wonky property name
        self.size       = [self.size_x,self.size_x]
        self.pos        = [random.randint((-10), (my_screen.WIDTH + 11)),-self.size[1]]
        self.speed      = round(random.uniform(0.5, 3), 3)
        self.damage     = 1
        self.type       = type #"standard" #standard, vfighter, missile
        self.clock      = 1
        self.direction  = direction
        self.color      = color.enemy
        self.alt_pos    = alt_pos


    def draw(self):
        if self.alt_pos[0] and self.alt_pos[1] == 0:
            draw.rect(my_screen.screen, self.color, Rect(self.alt_pos, self.size))
        else:
            draw.rect(my_screen.screen, self.color, Rect(self.pos, self.size))
    #enemy types
    def standard(self):
        pass
    """
    def v_fighter(self):
        #if (self.clock % 20 == 0): 
        if (random.randint(1,40)) == 1:
            self.clock = 1
            #create missile with positive y and positive x
            #create missile with positivt y and negative x
            if len(enemies_list) < 1000:            
                enemies_list.append(Enemy("missile", "left",    self.pos))
                enemies_list.append(Enemy("missile", "right",   self.pos))
        else:
            self.clock += 1
    """
    def missile(self):
        self.color = color.missile
        if(self.direction == "left"):
            # go x - 1
            print("place holder")
        else:
            # go y + 1
            print("place holder")
        
    #/enemy types

    def do(self):
        self.draw()
        if  (self.type == "vfighter"):
            self.v_fighter()
        elif(self.type == "missile"):
            self.missile()
        else:
            self.standard()


enemy_inst          = Enemy("standard")                          #FIXME lazy temp for passing values to enemy_instz #FIXME: 2023: the hell is this for?


enemies_list        = []
stars               = []
bullets             = []
bullet_clock        = 99999
star_clock          = 99999
star_spawn_rate     = 10
enemy_clock         = 99999
enemy_spawn_rate    = 20
bullet_fire_rate    = 7 #lower number higher rate
running             = True

flip_switch_bool    = True #used for missile direction, might be used for other things as well in future

players             = [player]  #makes it easier to make game multiplayer in future
non_lists           = []
do_objects          = [players, non_lists, stars, bullets, enemies_list] #only put lists in this list

my_clock            = time.Clock()
game_over           = False




# main loop / game loop
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        #toggle:
        elif evt.type == KEYDOWN: #tells you if event is relatet to keyboard -EMC235
            #toggle auto_fire:
            if evt.key == K_SPACE: #if the type of the event is KEYDOWN that means it has a .key attribute ant it van be any key -EMC235
                player.auto_fire = not player.auto_fire #reverse boolean value
                print(f"boolean auto_fire = {player.auto_fire}")



    #background
    my_screen.do() #before drawing anything else

    #/add speed/destroy
    if True:
        if len(stars) < 1000 and star_clock > star_spawn_rate: #max 999 bullets,
            star_clock = 0
            stars.append(BgStar())
    star_clock += 1

    #move stars
    for x in stars:
        x.pos[1] += x.speed

    #/background
    #enemies
    """ temporary enemy removal
    if enemy_clock > enemy_spawn_rate:
        if len(enemies_list) < 1000:
            enemy_clock = 0
            if False: #FIXME #(random.randint(1,10)) == 1: #FIXME rate should be decided by level #FIXME value should not be hardcoded
                enemies_list.append(Enemy("vfighter"))
            else:
                enemies_list.append(Enemy("standard")) 
    """
    #enemy movement
    for i in enemies_list: ##FIXME: move into class?
            i.pos[1] += i.speed
            
            if      i.direction == "left":
                i.pos[0] -= i.speed
            elif    i.direction == "right":
                i.pos[0] += i.speed



    enemy_clock += 1
    #/enemies

    #gun
    #move bullets
    for bullet in bullets:
            bullet.pos[1] -= bullet.speed


    #/add speed/destroy
    if player.auto_fire:
        if bullet_clock > bullet_fire_rate:
            bullet_clock = 0
            bullets.append(PlayerAmmo())
    bullet_clock += 1

    #/gun
    #collision
    #collide = pygame.Rect.colliderect(player_rect, player_rect2)
    for enemy in enemies_list:
        col1    = Rect(player.pos,  player.size)
        col2    = Rect(enemy.pos,   enemy.size)
        if pygame.Rect.colliderect(col1, col2):
            print("player death")
            if not INVINCIBILITY:
                game_over   = True

        for bullet in bullets:
            col1    = Rect(bullet.pos,  bullet.size)
            col2    = Rect(enemy.pos,   enemy.size)
            if pygame.Rect.colliderect(col1, col2):
                print("enemy death")
                player.points   += 1
                enemies_list.remove(enemy)
                bullets.remove(bullet)
    #/collision
    #display info
    #/display info
    #draw
    for obj in do_objects:
        for x in obj:
            x.do()


    #/draw
    #game over
    if game_over:
        my_screen.makeBackground()
        game_over_out = my_screen.font_out.render("game over. hit m to restart.", True, color.WHITE)
        my_screen.screen.blit(game_over_out, (100,100))
        bullets.clear()  #this is such a mess
        enemies_list.clear()
        keys    = key.get_pressed()
        if  keys[K_m]:
            print("restart")
            player.points   = 0
            game_over       = False
    #/game over
    #display score

    score_text = my_screen.font_out.render(f"score: {player.points}\n enemies: {len(enemies_list)}\n stars: {len(stars)}\n bullets:{len(bullets)}", True, color.TEXT)
    my_screen.screen.blit(score_text, my_screen.FONT_POS)
    #/display score

    ######### ######### #########
    ##      2023 rewrite       ##
    ##          start          ##
    ######### ######### #########


    #enemies_list = remove_offscreen_list_items(enemies_list)
    #stars = remove_offscreen_list_items(stars)
    remove_offscreen_list_items(bullets)

    #enemies_list = enforce_list_size(enemies_list)
    #stars = enforce_list_size(stars)
    enforce_list_size(bullets)


    ######### ######### #########
    ##      2023 rewrite       ##
    ##           end           ##
    ######### ######### #########


    ################################################################


    display.flip()
    my_clock.tick(60)


quit()
exit()


