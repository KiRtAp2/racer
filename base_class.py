import pygame

import colors
import settings

class Base(object):

    x = y = 0
    dx = dy = 0
    sx = sy = 0

    def __init__(self):
        pass

    def __init__(self, pos, size):
        self.x, self.y = pos
        self.sx, self.sy = size

    def show(self, window):
        pygame.draw.rect(window, colors.red, (self.x, self.y, self.sx, self.sy))

