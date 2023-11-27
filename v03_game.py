# double hashsign to start a segment
## import external
import pygame
import time
import v03_pt_enemy_spawn

## variables
game_running = True
pause_length = 1

## mainloop
while game_running:
  time.pause(pause_length) 
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pygame")

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update game logic here
    add_standard_enemy()

    # Draw graphics here

    # Refresh the display
    pygame.display.flip()

