import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    # Initialize the snake
    def __init__(self):
        self.body = [Vector2(0, 0), Vector2(0, 1), Vector2(0, 2)]
        self.direction = Vector2(1, 0)
        
        self.head_up = pygame.image.load("Graphics/head_up.png")
        self.head_down = pygame.image.load("Graphics/head_down.png")
        self.head_right = pygame.image.load("Graphics/head_right.png")
        self.head_left = pygame.image.load("Graphics/head_left.png")
        
        self.tail_up = pygame.image.load("Graphics/tail_up.png")
        self.tail_down = pygame.image.load("Graphics/tail_down.png")
        self.tail_right = pygame.image.load("Graphics/tail_right.png")
        self.tail_left = pygame.image.load("Graphics/tail_left.png")
        
        self.body_verical = pygame.image.load("Graphics/body_vertical.png")
        self.body_horizontal = pygame.image.load("Graphics/body_horizontal.png")
        
        self.body_tr = pygame.image.load("Graphics/body_tr.png") # top right
        self.body_tl = pygame.image.load("Graphics/body_tl.png")
        self.body_br = pygame.image.load("Graphics/body_br.png") # bottom right
        self.body_bl = pygame.image.load("Graphics/body_bl.png")
    def reset(self):
        self.body = [Vector2(4,10),Vector2(3,10),Vector2(2,10)]
        self.direction = Vector2(0,0) 
    def draw_snake(self):
        for index, segment in enumerate(self.body):
            block_rect = pygame.Rect(int(segment.x*cell_size), int(segment.y*cell_size), cell_size, cell_size)
            if index == 0:
                if self.direction.y > 0:
                    screen.blit(self.head_down, block_rect)
                elif self.direction.y < 0:
                    screen.blit(self.head_up, block_rect)
                elif self.direction.x > 0:
                    screen.blit(self.head_right, block_rect)
                elif self.direction.x < 0:
                    screen.blit(self.head_left, block_rect)
            elif index == len(self.body) - 1:
                if self.body[index - 1] - self.body[index] == Vector2(1, 0):
                    screen.blit(self.tail_left, block_rect)
                elif self.body[index - 1] - self.body[index] == Vector2(-1, 0):
                    screen.blit(self.tail_right, block_rect)
                elif self.body[index - 1] - self.body[index] == Vector2(0, 1):
                    screen.blit(self.tail_up, block_rect)
                elif self.body[index - 1] - self.body[index] == Vector2(0, -1):
                    screen.blit(self.tail_down, block_rect)
                #screen.blit(self.tail_up if self.direction.y > 0 else self.tail_down if self.direction.y < 0 else self.tail_right if self.direction.x > 0 else self.tail_left, block_rect)
            else:
                previous_segment = self.body[index + 1] - segment
                next_segment = self.body[index - 1] - segment
                if previous_segment.x == next_segment.x:
                    screen.blit(self.body_verical, block_rect)
                elif previous_segment.y == next_segment.y:
                    screen.blit(self.body_horizontal, block_rect)
                elif previous_segment.x == -1 and next_segment.y == -1 or previous_segment.y == -1 and next_segment.x == -1:
                    screen.blit(self.body_tl,block_rect)
                elif previous_segment.x == -1 and next_segment.y == 1 or previous_segment.y == 1 and next_segment.x == -1:
                    screen.blit(self.body_bl,block_rect)
                elif previous_segment.x == 1 and next_segment.y == -1 or previous_segment.y == -1 and next_segment.x == 1:
                    screen.blit(self.body_tr,block_rect)
                elif previous_segment.x == 1 and next_segment.y == 1 or previous_segment.y == 1 and next_segment.x == 1:
                    screen.blit(self.body_br,block_rect)
                
                    
                    #screen.blit(self.body_tr, block_rect)
                #screen.blit(self.body_tr if self.direction.x > 0 and self.direction.y > 0 else self.body_tl if self.direction.x < 0 and self.direction.y > 0 else self.body_br if self.direction.x > 0 and self.direction.y < 0 else self.body_bl if self.direction.x < 0 and self.direction.y < 0 else self.body_verical if self.direction.x == 0 else self.body_horizontal, block_rect)
            # else:
            #     pygame.draw.rect(screen, (0, 255, 0), block_rect)
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
        screen.blit(apple, fruit_rect)
        #pygame.draw.rect(screen,pygame.Color('red'),fruit_rect)

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
            self.game_over()
        if self.snake.body[0].x < 0 or self.snake.body[0].x > cell_number-1 or self.snake.body[0].y < 0 or self.snake.body[0].y > cell_number-1:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
    def game_over(self):
        self.snake.reset()
    def draw_grass(self):
        grass_color = (167,209,61)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text,True,(56,74,12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left,score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width + 6,apple_rect.height)

        pygame.draw.rect(screen,(167,209,61),bg_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(apple,apple_rect)
        pygame.draw.rect(screen,(56,74,12),bg_rect,2)
  
    def draw(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
        
        
        
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load('Graphics/apple.png').convert_alpha() # Load the apple image
game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)

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
    
            
    screen.fill(pygame.Color('yellow'))
    main_game.draw()
    #pygame.draw.rect(screen, pygame.Color('red'), test_rect)
    #screen.blit(test_surface, test_rect) # where to draw, where to draw from; top left corner of test_surface
    
    #draw all our elements
    pygame.display.update() # update the screen
    clock.tick(120) #60 frames per second is the max speed of the game
    
