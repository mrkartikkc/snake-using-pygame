import pygame
import time
import random

pygame.init()
clock = pygame.time.Clock()

#colors
black = (0, 0, 0)
red = (255, 0, 0)
green = (0 ,255, 0)


#size of the window
display_width = 600
display_height = 600

#display with the help of size
dis =  pygame.display.set_mode((display_height, display_height))

#display box caption
pygame.display.set_caption('Snake Game')

#snake size
snake_block = 20
snake_speed = 10

snake_list =[]

#define snake structure and posotion
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

#main function
def snakegame():
    #for working game window while/while not loop
    game_over = False
    game_end = False
    #coordinates
    x1 = display_width/2
    y1 = display_height/2
    #when the snakes moves
    x1_change = 0
    y1_change = 0

    snake_list = []
    lenght_of_snake = 1

    #food
    foodx = round(random.randrange(0, display_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, display_height - snake_block) / 20.0) * 20.0

    while not game_over:
        while game_end == True:
            #restart
            dis.fill(black)
            font_style = pygame.font.SysFont("comicsansms", 25)
            mesg = font_style.render("You lost!   Play again?   Press P ", True, red)
            dis.blit(mesg,[display_width / 6, display_height / 3])

           #score
            score = lenght_of_snake - 1
            score_font = pygame.font.SysFont("comicsansms", 35)
            value = score_font.render("Your score: " + str(score), True, red)
            dis.blit(value, [display_width/3, display_height/5])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        snakegame()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_end = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = +snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = +snake_block
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 <0:
            game_end =True

        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, red,[foodx, foody, snake_block, snake_block])


        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        #when the lenght of snake exceeds
        if len(snake_list) > lenght_of_snake:
            del snake_list[0]

        #when snake hits itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_end = True
        snake(snake_block, snake_list)
        pygame.display.update()

        #when snake eats the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0,  display_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, display_height - snake_block) / 20.0) * 20.0
            lenght_of_snake += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()
snakegame()