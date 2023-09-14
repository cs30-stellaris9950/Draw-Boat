# Import a library of functions called 'pygame'
import pygame
import random
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
pygame.display.set_caption("Draw")
# Loop until the user clicks the close button.
close_screen = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# First, clear the screen to white. Don't put other drawing commands above this,
# or they will be erased with this command.
screen.fill(WHITE)
pygame.display.flip()


def testDraw():
    rand_x = random.randrange(10, 600)
    rand_y = random.randrange(10, 400)
    # pygame.draw.rect(screen, BLACK, [rand_x, rand_y, 100, 100], 2)
    pygame.draw.line(screen, BLACK, (rand_x, rand_y + 100), (rand_x + 100, rand_y + 100), 2)
    pygame.draw.line(screen, BLACK, (rand_x - 100, rand_y), (rand_x + 200, rand_y), 2)
    pygame.draw.arc(screen, BLACK, (rand_x - 100, rand_y - 100, 200, 200), PI, 1.5 * PI, 2)
    pygame.draw.arc(screen, BLACK, (rand_x, rand_y - 100, 200, 200), 1.5 * PI, 0, 2)
    pygame.draw.polygon(screen, BLACK, [[rand_x, rand_y - 75], [rand_x + 50, rand_y - 125], [rand_x + 50, rand_y - 25]], 2)
    pygame.draw.line(screen, BLACK, (rand_x + 50, rand_y - 25), (rand_x + 50, rand_y), 2)
    pygame.display.flip()



while not close_screen:

    # -------- Main Program Loop -----------
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            close_screen = True # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            testDraw()
    # --- Game logic should go here

    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    # pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)




def drawShip(size, positionX, positionY):
    pygame.draw.rect(screen, BLACK, [20, 20, 250, 100], 2)
    pygame.display.flip()
    if size == 'small':
        print("User pressed a key.")







