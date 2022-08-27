from tkinter import CENTER
import pygame, sys

pygame.init()
screen = pygame.display.set_mode((400,500))
clock = pygame.time.Clock()
test_surface = pygame.Surface((100,200))
test_surface.fill(pygame.Color('blue'))
test_rect = test_surface.get_rect(topright=(200,250))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(pygame.Color('gold'))
    pygame.draw.rect(screen, pygame.Color('red'), test_rect)
    screen.blit(test_surface, test_rect) # where to draw, where to draw from; top left corner of test_surface
    
    #draw all our elements
    pygame.display.update()
    clock.tick(60)
    
