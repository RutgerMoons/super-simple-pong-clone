__author__ = 'rutger'

import pygame
from Board_Objects import *

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

# Set the width and height of the screen [width, height]
size = (1200, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong Clone")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

x, y = 40, 20
paddle_width, paddle_length = 15, 30

velocity = 0
speed = 15

left_paddle = Paddle(x, y, paddle_width, paddle_length, speed, size[1])
right_paddle = Paddle(size[0] - x - paddle_width, y, paddle_width, paddle_length, speed, size[1])

ball = Ball(size[0]//2, size[1]//2, 8, 15, 15, size[0], size[1])

done = False
while not done:

    for event in pygame.event.get():    # User did something
        if event.type == pygame.QUIT:   # If user clicked close
            done = True                 # Flag that we are done so we exit this loop

        elif event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == "z":
                left_paddle.up()
            elif pygame.key.name(event.key) == "s":
                left_paddle.down()
            elif pygame.key.name(event.key) == "o":
                right_paddle.up()
            elif pygame.key.name(event.key) == "l":
                right_paddle.down()
            elif pygame.key.name(event.key) == "h":
                done = True
                break

        elif event.type == pygame.KEYUP:
            if pygame.key.name(event.key) == "z" or pygame.key.name(event.key) == "s":
                left_paddle.stop_moving()
            elif pygame.key.name(event.key) == "o" or pygame.key.name(event.key) == "l":
                right_paddle.stop_moving()

    screen.fill(WHITE)

    left_paddle.move()
    right_paddle.move()
    ball.move()

    if ball.x - ball.radius <= 0:
        print("player 2 wins")
        done = True

    if ball.x + ball.radius >= size[0]:
        print("player 1 wins")
        done = True

    pygame.draw.rect(screen, GREEN, (left_paddle.x, left_paddle.y, left_paddle.width, left_paddle.height))
    pygame.draw.rect(screen, GREEN, (right_paddle.x, right_paddle.y, right_paddle.width, right_paddle.height))
    pygame.draw.circle(screen, BLUE, (ball.x, ball.y), ball.radius)

    pygame.display.flip()

    clock.tick(30)

pygame.quit()