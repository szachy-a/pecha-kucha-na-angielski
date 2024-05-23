import pygame
from pygame.locals import (
    QUIT,
    KEYDOWN
)
pygame.init()

import os
import time

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def slidesGen():
    for n in sorted(os.listdir()):
        if n[-4:] in ['.jpg', '.png']:
            surf = pygame.image.load(n)
            yield pygame.transform.scale(surf, screen.get_size()).convert()

running = True
slides = slidesGen()
slide = next(slides)
lastTime = time.time()
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            slide = next(slides)
            lastTime = time.time()
    if time.time() > lastTime + 20:
        slide = next(slides)
        lastTime = time.time()
    screen.blit(slide, (0, 0))
    pygame.display.flip()
pygame.quit()
