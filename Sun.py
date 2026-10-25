import pygame
class Sun:
    def __init__(self, name, color, radius, center_x, center_y):
        self.name = name
        self.color = color
        self.radius = radius
        self.center_x = center_x
        self.center_y =  center_y

    def draw_sun(self, screen):
        pygame.draw.circle(screen, self.color, (self.center_x, self.center_y), self.radius)
