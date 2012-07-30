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
    pps = clock.tick(60) / 1000.

    for e in pygame.event.get():
        if e.type == QUIT:
            running = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                running = False

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        squ.move(-(pps * velocity), 0)
    elif keys[K_RIGHT]:
        squ.move(pps * velocity, 0)
    if keys[K_UP]:
        squ.move(0, -(pps * velocity))
    elif keys[K_DOWN]:
        squ.move(0, pps * velocity)

    if (squ.collide(tri)):
        squ.color = tri.color = (255, 0, 0)
    else:
        squ.color = tri.color = (0, 0, 0)

    screen.fill((255, 255, 255))
    tri.draw(screen)
    squ.draw(screen)

    pygame.display.flip()

pygame.quit()

