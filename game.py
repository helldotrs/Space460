import pygame
import random
import sys

pygame.init()

# Constants
WIDTH = 500
HEIGHT = 500
SIZE = (WIDTH, HEIGHT)
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2
CENTER = (CENTER_X, CENTER_Y)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (230, 0, 100)
GRAY = (153, 153, 153)
GREEN = (0, 204, 0)
BLUE = (117, 182, 243)

# Initialize Pygame
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Space 460")

# Clock Rates
BULLET_FIRE_RATE = 7
STAR_SPAWN_RATE = 10
ENEMY_SPAWN_RATE = 20

# Classes
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
            
class Player():
    def __init__(self):
        self.pos        = [my_screen.CENTER_X,  my_screen.HEIGHT  - 50]
        self.size       = (16,  16)
        self.limit      = [(0), (my_screen.WIDTH - self.size[0]), (0), (my_screen.HEIGHT - self.size[1])]    #FIXME should be a two layer: ((x min, x max), (y min, y max))
        self.speed      = (5,   0)                                                                           #no y movement
        self.box        = Rect(self.pos, self.size)
        self.keys       = key.get_pressed()     #this way does not work and I dont know why
        self.auto_fire  = False
        self.kills      = 0
        self.points     = 0
        self.lives      = 3 #for future updates

    #movement and shooting
    def move(self):
        keys    = key.get_pressed()


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

# Game objects
color = Color()
my_screen = MyScreen()
player = Player()
player_ammo = PlayerAmmo()
bg_star = BgStar()
enemy_inst = Enemy("standard")
enemies_list = []
stars = []
bullets = []

# Helper functions
def detect_collisions():
    global player, player_ammo, enemies_list, bullets

    player_rect = pygame.Rect(player.pos, player.size)

    for enemy in enemies_list[:]:
        enemy_rect = pygame.Rect(enemy.pos, enemy.size)
        if player_rect.colliderect(enemy_rect):
            print("player death")
            return True

        for bullet in bullets[:]:
            bullet_rect = pygame.Rect(bullet.pos, bullet.size)
            if bullet_rect.colliderect(enemy_rect):
                print("enemy death")
                player.points += 1
                enemies_list.remove(enemy)
                bullets.remove(bullet)

    return False

def handle_game_over():
    global game_over, bullets, enemies_list

    my_screen.makeBackground()
    game_over_out = my_screen.font_out.render("game over. hit m to restart.", True, color.WHITE)
    my_screen.screen.blit(game_over_out, (100, 100))
    bullets.clear()
    enemies_list.clear()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_m]:
        print("restart")
        player.points = 0
        player.lives = 3
        player.pos = [CENTER_X, HEIGHT - 50]
        game_over = False

# Game loop
my_clock = pygame.time.Clock()
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Handle player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        player.auto_fire = not player.auto_fire
        print(f"auto_fire = {player.auto_fire}")

    # Game logic
    my_screen.makeBackground()

    if len(stars) < 1000:
        if random.randint(1, STAR_SPAWN_RATE) == 1:
            stars.append(BgStar())

    for star in stars[:]:
        if star.pos[1] < HEIGHT:
            star.pos[1] += star.speed
        else:
            stars.remove(star)

    if len(enemies_list) < 1000:
        if enemy_clock > ENEMY_SPAWN_RATE and random.randint(1, 10) == 1:
            enemy_clock = 0
            enemy_type = "vfighter" if random.randint(1, 40) == 1 else "standard"
            enemies_list.append(Enemy(enemy_type))
        else:
            enemy_clock += 1

    for enemy in enemies_list:
        if enemy.pos[1] < HEIGHT:
            enemy.pos[1] += enemy.speed
            if enemy.direction == "left":
                enemy.pos[0] -= enemy.speed
            elif enemy.direction == "right":
                enemy.pos[0] += enemy.speed

    if player.auto_fire:
        if len(bullets) < 1000:
            if bullet_clock > BULLET_FIRE_RATE:
                bullet_clock = 0
                bullets.append(PlayerAmmo())
            else:
                bullet_clock += 1

    # Draw objects
    for obj in [stars, bullets, enemies_list, player]:
        for x in obj:
            x.do()

    # Detect collisions and handle game over
    if detect_collisions():
        game_over = True

    # Display score
    score_text = my_screen.font_out.render(f"Score: {player.points}", True, color.RED)
    my_screen.screen.blit(score_text, my_screen.FONT_POS)

    pygame.display.flip()
    my_clock.tick(60)

# Quit the game
pygame.quit()
sys.exit()
