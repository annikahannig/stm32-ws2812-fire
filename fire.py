#!/usr/bin/env python3

import sys
import time
import math
import random

import pygame

# Preview buffer
P_WIDTH = 400
P_HEIGHT = 400

# Render framebuffer
FB_WIDTH  = 8
FB_HEIGHT = 8

# Firebuffer
F_WIDTH = 8
F_HEIGHT = FB_HEIGHT + 4

# Pixel constants
PX_GUTTER = 3
PX_WIDTH  = P_WIDTH / FB_WIDTH
PX_HEIGHT = P_HEIGHT / FB_HEIGHT



def draw_pixel(ctx, fb, i):
    """Draw a pixel in the framebuffer"""
    # Framebuffer coords
    x = i % FB_WIDTH
    y = math.floor(i / FB_WIDTH)

    # Pixel coords
    px = (x * (P_WIDTH / FB_WIDTH)) + 10
    py = (y * (P_HEIGHT / FB_HEIGHT)) + 10

    color = fb[i]

    # pygame.draw.rect(ctx, color, rect)
    size = 15
    pygame.draw.circle(ctx, color, (round(px) + size, round(py) + size), size)



def render(ctx, fb):

    for i in range(0, FB_WIDTH * FB_HEIGHT):
        draw_pixel(ctx, fb, i)



def main():
    pygame.init()

    display = pygame.display.set_mode((P_WIDTH, P_HEIGHT), 0, 32)

    fb = [(random.randint(1, 127),
           random.randint(1, 127),
           random.randint(1, 127)) for i in range(FB_WIDTH * FB_HEIGHT)]


    while 42:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit();

        render(display, fb)
        pygame.display.update()


if __name__ == "__main__":
    main()
