import pygame
import math
from planet import Planets
from Sun import Sun

pygame.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")
clock = pygame.time.Clock()
running = True

The_Sun = Sun("Sun", "yellow", 30, 640, 360)
Planet = Planets("Earth", "blue", 10, 400, 250, 300, The_Sun)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    The_Sun.draw_sun(screen)
    Planet.update()
    Planet.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()