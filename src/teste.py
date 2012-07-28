#! /usr/bin/env python

import pygame
from pygame.locals import *
from shape import *

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, DOUBLEBUF)

clock = pygame.time.Clock()
tri = Triangle()
squ = Square()
tri.move(150, 150)
velocity = 200.

running = True
while running:
    pps = clock.tick(30) / 1000.
    x, y = 0, 0

    for e in pygame.event.get():
        if e.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        x -= pps * velocity
    elif keys[K_RIGHT]:
        x += pps * velocity
    if keys[K_UP]:
        y -= pps * velocity
    elif keys[K_DOWN]:
        y += pps * velocity

    squ.move(x, y)

    if (squ.collide(tri)):
        squ.color = tri.color = (255, 0, 0)
    else:
        squ.color = tri.color = (0, 0, 0)

    screen.fill((255, 255, 255))
    tri.draw(screen)
    squ.draw(screen)

    pygame.display.flip()

pygame.quit()
