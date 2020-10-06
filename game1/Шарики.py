#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 2
screen = pygame.display.set_mode((1200, 900))

points = 0

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    global m
    m = randint(1, 3)
    if m == 1:
        global x, y, r
        x = randint(100, 1100)
        y = randint(100, 900)
        r = randint(10, 100)
        color = COLORS[randint(0, 5)]
        circle(screen, color, (x, y), r)
    else:
        global x1, y1, r1
        x1 = randint(100, 1100)
        y1 = randint(100, 900)
        r1 = randint(10, 100)
        color1 = COLORS[randint(0, 5)]
        circle(screen, color1, (x1, y1), r1)
        global x2, y2, r2
        x2 = randint(100, 1100)
        y2 = randint(100, 900)
        r2 = randint(10, 100)
        color2 = COLORS[randint(0, 5)]
        circle(screen, color2, (x2, y2), r2)
        
       
def count(pos):
    p = 1
    if m == 1:
        if (pos[0] - x)**2 + (pos[1] - y)**2 <= r**2:
            return p
        else:
            return 0
    else:
        if (pos[0] - x1)**2 + (pos[1] - y1)**2 <= r1**2:
            return p
        else:
            return 0
        if (pos[0] - x2)**2 + (pos[1] - y2)**2 <= r2**2:
            return p
        else:
            return 0
           
    
    
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            if count(event.pos) == 1:
                print('Ты попал! Молодец!')
                points += 1
            else:
                points -= 0.5
                print('Промах!')
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)
print('Вы набрали', points, 'балла')
pygame.quit()


# In[ ]:




