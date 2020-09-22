#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

circle(screen, (255, 255, 0), (200, 175), 150)
circle(screen, (0, 0, 0), (130,130), 32)
circle(screen, (255, 0, 0), (130,130), 30)
circle(screen, (0, 0, 0), (130,130), 15)

circle(screen, (0, 0, 0), (275,130), 32)
circle(screen, (255, 0, 0), (275,130), 30)
circle(screen, (0, 0, 0), (275,130), 15)

line(screen, (0, 0, 0), [130,250], [275,250], 20)
line(screen, (0, 0, 0), [100,75], [170,120], 10)
line(screen, (0, 0, 0), [230,100], [320,100], 10)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()


# In[ ]:




