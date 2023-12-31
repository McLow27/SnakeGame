import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
black = (0, 0, 0)

screen_width = 500
screen_height = 400
screenDisplay = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game by MChokr')

clock = pygame.time.Clock()

snakeSize = 10
snakeSpeed = 20

font_style = pygame.font.SysFont("calibri", 20)
score_font = pygame.font.SysFont("arial", 20)


def track_score(score):
    value = score_font.render("Score: " + str(score), True, white)
    screenDisplay.blit(value, [0, 0])


def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screenDisplay, green, [x[0], x[1], snakeSize, snakeSize])


def message(message1, color):
    message1 = font_style.render(message1, True, color)
    screenDisplay.blit(message1, [screen_width / 6, screen_height / 3])


def gameLoop():
    gameOver = False
    gameExit = False

    x1 = screen_width / 2
    y1 = screen_height / 2

    x1_change = 0
    y1_change = 0

    snakeList = []
    snakeLength = 1

    foodx = round(random.randrange(0, screen_width - snakeSize) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - snakeSize) / 10.0) * 10.0

    while not gameOver:

        while gameExit == True:
            screenDisplay.fill(black)
            message("Game Over! Play Again = R or Q-Quit", red)
            track_score(snakeLength - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameExit = False
                    if event.key == pygame.K_r:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snakeSize
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snakeSize
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snakeSize
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snakeSize
                    x1_change = 0

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            gameExit = True
        x1 += x1_change
        y1 += y1_change
        screenDisplay.fill(black)
        pygame.draw.rect(screenDisplay, red, [foodx, foody, snakeSize, snakeSize])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snakeList.append(snake_Head)
        if len(snakeList) > snakeLength:
            del snakeList[0]

        for x in snakeList[:-1]:
            if x == snake_Head:
                gameExit = True

        snake(snakeSize, snakeList)
        track_score(snakeLength - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snakeSize) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - snakeSize) / 10.0) * 10.0
            snakeLength += 1

        clock.tick(snakeSpeed)

    pygame.quit()
    quit()


gameLoop()