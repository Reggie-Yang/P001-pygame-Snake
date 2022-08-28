import pygame, sys, random
from pygame.math import Vector2

class FRUIT:
    """
    This is a function that will randomly generate a fruit position
    """
    # Class for the fruit object 
    def __init__(self):
        # create an x and y position for the fruit
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x, self.y)
    
    def draw_fruit(self):
        # draw the fruit on the screen
        fruit_rect = pygame.Rect(int(self.pos.x*cell_size), int(self.pos.y*cell_size), cell_size, cell_size)
        pygame.draw.rect(screen,pygame.Color('red'),fruit_rect)

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
clock = pygame.time.Clock()
#test_surface = pygame.Surface((100,200))
#test_surface.fill(pygame.Color('blue'))
#test_rect = test_surface.get_rect(topright=(200,250))
fruit = FRUIT()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(pygame.Color('gold'))
    #pygame.draw.rect(screen, pygame.Color('red'), test_rect)
    #screen.blit(test_surface, test_rect) # where to draw, where to draw from; top left corner of test_surface
    fruit.draw_fruit()
    #draw all our elements
    pygame.display.update() # update the screen
    clock.tick(60) #60 frames per second is the max speed of the game
    
