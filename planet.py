import pygame
import math
from Sun import Sun



class Planets:
    def __init__(self, name, color, radius, major_axis, minor_axis, period, Sun):
        self.name = name
        self.radius = radius
        self.major_axis = major_axis
        self.minor_axis = minor_axis
        self.period = period
        self.angle = 0
        self.color = color
        self.sun = Sun


    def update(self):
        self.angle += (2* math.pi) / self.period
        self.x = self.sun.center_x + self.major_axis * math.cos(self.angle)
        self.y = self.sun.center_y + self.minor_axis *math.sin(self.angle)


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    