import math
import pygame

import base_class
from pygame.transform import rotate

import settings
import texture


class Player(base_class.Base):

    orientation = 0 # degrees
    rotation_speed = 5
    rotating_direction = 0
    # rotating_direction:
    # 0 - no rotation
    # 1 - right
    # -1 - left
    velocity = 2
    
    def __init__(self, pos, size, image):
        self.image = image
        super(Player, self).__init__(pos, size)
    
    def show(self, window):
        window.blit(rotate(self.image, self.orientation), (self.x, self.y))

    def rotate(self, dire):
        self.rotating_direction = dire

    def stop_rotating(self):
        self.rotating_direction = 0

    def move(self):
        self.dx = math.sin(math.radians(self.orientation))*self.velocity
        self.dy = math.cos(math.radians(self.orientation))*self.velocity

        self.x += self.dx
        self.y += self.dy


    def tick(self, window):
        if self.rotating_direction == 1:
            self.orientation -= self.rotation_speed
        elif self.rotating_direction == -1:
            self.orientation += self.rotation_speed

        if self.orientation > 180:
            self.orientation = -180+(180-self.orientation)
        elif self.orientation < -180:
            self.orientation = 180+(self.orientation+180)

        self.move()
        self.show(window)