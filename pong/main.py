__author__ = 'rutger'
import pygame
import time

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

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

def up():
    return velocity - speed

def release_up():
    return 0

def down():
    return velocity + speed

def release_down():
    return 0

def move():
    loc = y + velocity
    if loc < 0:
        return 0
    if loc > size[1] - paddle_length:
        return size[1] - paddle_length
    return loc

done = False
while not done:

    for event in pygame.event.get():    # User did something
        if event.type == pygame.QUIT:   # If user clicked close
            done = True                 # Flag that we are done so we exit this loop

        elif event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == "z":
                velocity = up()
            elif pygame.key.name(event.key) == "s":
                velocity = down()
            elif pygame.key.name(event.key) == "p":
                done = True
                break

        elif event.type == pygame.KEYUP:
            if pygame.key.name(event.key) == "z":
                velocity = release_up()
            elif pygame.key.name(event.key) == "s":
                velocity = release_down()

    screen.fill(WHITE)

    y = move()
    print(x, y)
    pygame.draw.rect(screen, GREEN, (x, y, paddle_width, paddle_length))


    pygame.display.flip()

    clock.tick(30)

pygame.quit()

