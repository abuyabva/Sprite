# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
import random

# color = [0x1D2B53, 0x7E2553, 0x008751, 0xAB5236, 0x5F574F, 0xC2C3C7, 0xFFF1E8, 0xFF004D, 0xFFA300, 0xFFEC27,
#          0x00E436, 0x29ADFF, 0x83769C, 0xFF77A8, 0xFFCCAA]
color = matplotlib.colors.LinearSegmentedColormap.from_list("", [(0.11, 0.17, 0.33), (0.49, 0.15, 0.33),
                                                                 (0, 0.53, 0.32), (0.67, 0.32, 0.21),
                                                                 (0.37, 0.34, 0.31), (0.76, 0.76, 0.78),
                                                                 (1, 0.95, 0.91), (1, 0, 0.30),
                                                                 (1, 0.64, 0), (1, 0.93, 0.15),
                                                                 (0, 0.89, 0.21), (0.16, 0.68, 1),
                                                                 (0.51, 0.46, 0.61), (1, 0.47, 0.66),
                                                                 (1, 0.80, 0.67), (0, 0, 0)])


def gen():
    sprite = np.arange(100).reshape((10, 10))
    sprite = np.full((10, 10), 0)
    for i in range(1, 9):
        for j in range(5):
            if j == 0:
                continue
            col = random.choice("BW")
            if col == "B":
                sprite[i][j] = 0
                sprite[i][9 - j] = 0
            else:
                sprite[i][j] = 1
                sprite[i][9 - j] = 1
    return sprite


def gen_sprite_par(height, width):
    sprite = np.arange(height*width).reshape(height, width)
    sprite = np.full((height, width), 15)
    for i in range(2, height - 2):
        for j in range((width // 2) + 1):
            if j == 0 or j == 1:
                continue
            col = random.randint(0, 16)
            sprite[i][j] = col
            sprite[i][width - j - 1] = col
    return sprite


def generate_card():
    sprite_card = np.arange(20000).reshape(200, 10, 10)
    for i in range(200):
        sprite_card[i] = gen()
    sprite_map = np.arange(20000).reshape(100, 200)
    for i in range(10):
        for j in range(20):
            new_sprite = sprite_card[i + 10 * j]
            for x in range(10*i, 10*(i+1)):
                for y in range(10*j, 10*(j+1)):
                    sprite_map[x][y] = new_sprite[x % 10][y % 10]
    return sprite_map


def generate_colored_card():
    sprite_card = np.arange(20000).reshape(200, 10, 10)
    for i in range(200):
        sprite_card[i] = gen_sprite_par(10, 10)
    sprite_map = np.arange(20000).reshape(100, 200)
    for i in range(10):
        for j in range(20):
            new_sprite = sprite_card[i + 10 * j]
            for x in range(10*i, 10*(i+1)):
                for y in range(10*j, 10*(j+1)):
                    sprite_map[x][y] = new_sprite[x % 10][y % 10]
    return sprite_map


def generate_colored_card_par(map_width, map_height, width, height):
    square = map_height * map_width
    sprite_square = height * width
    num_of_sprites = square // sprite_square
    vertical_sprites = map_height // height
    horizontal_sprites = map_width // width
    sprite_card = np.arange(square).reshape(num_of_sprites, height, width)
    for i in range(num_of_sprites):
        sprite_card[i] = gen_sprite_par(height, width)
    sprite_map = np.arange(square).reshape(map_height, map_width)
    for i in range(vertical_sprites):
        for j in range(horizontal_sprites):
            new_sprite = sprite_card[i + vertical_sprites * j]
            for x in range(height * i, height * (i+1)):
                for y in range(width * j, width * (j+1)):
                    sprite_map[x][y] = new_sprite[x % height][y % width]
    return sprite_map


fig, ax = plt.subplots()
# ax.imshow(gen_sprite_par(12, 12), cmap=color, vmin=0, vmax=15)
ax.imshow(generate_colored_card_par(200, 100, 10, 10), cmap=color, vmin=0, vmax=15)
# ax.imshow(gen(), cmap="gray")

fig.set_figwidth(8)
fig.set_figheight(8)

plt.show()
