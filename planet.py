import pygame

class Planets:
    def __init__(self, name, color,position, velocity, mass, radius):
        self.name = name
        self.color = color
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)

    