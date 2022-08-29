import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    # Initialize the snake
    def __init__(self):
        self.body = [Vector2(0, 0), Vector2(0, 1), Vector2(0, 2)]
        self.direction = Vector2(1, 0)
    def draw_snake(self):
        for segment in self.body:
            block_rect = pygame.Rect(int(segment.x*cell_size), int(segment.y*cell_size), cell_size, cell_size)
            pygame.draw.rect(screen, (0, 255, 0), block_rect)
    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]
        
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

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
    def update(self):
        self.snake.move_snake()
        if self.snake.body[0] == self.fruit.pos:
            self.snake.body.append(self.snake.body[-1])
            self.fruit = FRUIT()
        if self.snake.body[0] == self.snake.body[1]:
            print("You lose")
            sys.exit()
        if self.snake.body[0].x < 0 or self.snake.body[0].x > cell_number-1 or self.snake.body[0].y < 0 or self.snake.body[0].y > cell_number-1:
            print("You lose")
            sys.exit()
        for i in range(1, len(self.snake.body)):
            if self.snake.body[0] == self.snake.body[i]:
                print("You lose")
                sys.exit()
        
    def draw(self):
        self.snake.draw_snake()
        self.fruit.draw_fruit()
        
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
clock = pygame.time.Clock()
#test_surface = pygame.Surface((100,200))
#test_surface.fill(pygame.Color('blue'))
#test_rect = test_surface.get_rect(topright=(200,250))
main_game = MAIN()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction != Vector2(0, 1):
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction != Vector2(0, -1):
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction != Vector2(1, 0):
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction != Vector2(-1, 0):
                    main_game.snake.direction = Vector2(1, 0)
            
    screen.fill(pygame.Color('gold'))
    #pygame.draw.rect(screen, pygame.Color('red'), test_rect)
    #screen.blit(test_surface, test_rect) # where to draw, where to draw from; top left corner of test_surface
    main_game.draw()
    #draw all our elements
    pygame.display.update() # update the screen
    clock.tick(120) #60 frames per second is the max speed of the game
    
