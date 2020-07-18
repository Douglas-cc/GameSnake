import pygame, random
from pygame.locals import *

def grid():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return(x//10 * 10, y//10 *10)

def comer(c1,c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1]) 

pygame.init()
screen = pygame.display.set_mode((600,600)) # plano cartesiano X e Y
pygame.display.set_caption('Snake')

snake = [(200,200),(210,210),(220,220)]
snake_skin = pygame.Surface((10,10)) # plotando a snake
snake_skin.fill((225,225,255)) #cor da snake

apple_pos = grid()
apple = pygame.Surface((10,10)) # plotando  a maçã
apple.fill((255,0,0)) # cor da maçã

# direções 
UP = 0
RIGHT = 1 
DOWN = 2
LEFT = 3

my_direction = LEFT # direção atual
font = pygame.font.Font('freesansbold.ttf', 18) # Fonte da mensagem GAME OVER
clock = pygame.time.Clock() # metodo par cotrolar o time da nossa snayke
score = 0

game_over = False
while not game_over:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN:
               my_direction = UP     

            if event.key == K_DOWN and my_direction != UP:
               my_direction = DOWN     

            if event.key == K_LEFT and my_direction != RIGHT:
               my_direction = LEFT

            if event.key == K_RIGHT and my_direction != LEFT:
               my_direction = RIGHT

            
    if comer(snake[0], apple_pos):
        apple_pos = grid()
        snake.append((0,0))
        score = score + 1
    
    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = False
        break

    if game_over:
        break

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])              
           
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10) # quando estou indo pra cima meu Y esta diminuindo

    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10) # quando estou indo pra cima meu Y esta aumentando

    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1]) # quando estou indo pra cima meu X esta aumentando

    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1]) # quando estou indo pra cima meu X esta diminuindo

    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)

    score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 120, 10)
    screen.blit(score_font, score_rect)

    for pos in snake:
        screen.blit(snake_skin,pos)

    pygame.display.update()                     