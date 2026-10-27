import pygame
import math
from planet import Planet
from Sun import Sun

pygame.init()
WIDTH = 1500
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")
clock = pygame.time.Clock()
running = True

The_Sun = Sun("Sun", "yellow", 30, (WIDTH//2), (HEIGHT//2))
Planets = [Planet("Mercury", "gray", 5, 155, 150, 72,The_Sun),
    Planet("Earth", "blue", 10, 400, 250, 300, The_Sun),
    Planet("Mars", "red", 8, 610, 600, 564, The_Sun)
           ]


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    The_Sun.draw_sun(screen)
    for planet in Planets:
        planet.update()
        planet.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()