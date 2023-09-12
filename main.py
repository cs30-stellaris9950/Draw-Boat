# Import a library of functions called 'pygame'
import pygame
# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
GREEN = (   0, 255,   0)
RED = ( 255,   0,   0)
BLUE = (   0,   0, 255)
PI = 3.141592653

size = (700, 500)
screen = pygame.display.set_mode(size)

# Loop until the user clicks the close button.
close_screen = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not close_screen:
    # --- Main event loop
    for event in pygame.event.get(): # User did something


        if event.type == pygame.QUIT: # If user clicked close
            close_screen = True # Flag that we are done so we exit this loop

    # --- Game logic should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)