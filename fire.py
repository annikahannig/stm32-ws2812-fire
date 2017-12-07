#!/usr/bin/env python3

import sys
import time
import math
import random

import pygame

import palette

# Preview buffer
P_WIDTH = 400
P_HEIGHT = 400

# Render framebuffer
FB_WIDTH  = 8
FB_HEIGHT = 8

# Firebuffer
F_WIDTH = 8
F_HEIGHT = 8 + 2

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


def fb_set_pixel(fb, x, y, c):
    i = x + y * FB_WIDTH
    fb[i] = c

    return fb


def fire_set_value(fire, x, y, v):
    i = x + (y * F_WIDTH)
    fire[i] = v

    return fire


def fire_get_value(fire, x, y):
    if x < 0:
        x = 0
    if y >= F_HEIGHT:
        y = F_HEIGHT - 1

    i = x + (y * F_WIDTH)

    return fire[i]


def fire_fill_base(fire, hotspots):
    y = F_HEIGHT - 3
    for x in range(F_WIDTH):
        fire = fire_set_value(fire, x, y, 0)
        fire = fire_set_value(fire, x, y + 1, 0)

    for _ in range(hotspots):
        x = random.randint(0, F_WIDTH - 1)
        fire = fire_set_value(fire, x,  y, 255)
        fire = fire_set_value(fire, x,  y + 1, 255)

    return fire


def fire_fill_framebuffer(fb, fire):
    for y in range(FB_HEIGHT):
        for x in range(FB_WIDTH):
            v = fire_get_value(fire, x, y)
            c = palette.fire[round(v)]
            fb = fb_set_pixel(fb, x, y, c)

    return fb


def fire_update(fire):
    for y in range(F_HEIGHT - 2):
        for x in range(F_WIDTH):
            samples = [fire_get_value(fire, x - 1, y + 1) / 3.0,
                       fire_get_value(fire, x,     y + 1) / 3.0,
                       fire_get_value(fire, x + 1, y + 1) / 3.0]
            fire = fire_set_value(fire, x, y, sum(samples))

    return fire


def main():
    pygame.init()

    display = pygame.display.set_mode((P_WIDTH, P_HEIGHT), 0, 32)

    framebuffer = [(random.randint(1, 127),
                   random.randint(1, 127),
                   random.randint(1, 127)) for i in range(FB_WIDTH * FB_HEIGHT)]


    # Initialize firebuffer
    firebuffer = [0 for _ in range(F_WIDTH * F_HEIGHT)]

    i = 0
    while 42:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit();

        render(display, framebuffer)
        pygame.display.update()

        # Periodically set hotspots
        if i % 10 == 0:
            fire_buffer = fire_fill_base(firebuffer, 5)

        framebuffer = fire_fill_framebuffer(framebuffer, firebuffer)

        if i % 2 == 0:
            firebuffer = fire_update(firebuffer)

        i += 1

if __name__ == "__main__":
    main()
