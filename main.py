import pygame
import math
from planet import Planets

pygame.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")
clock = pygame.time.Clock()
running = True

Planet = Planets("Earth", "blue", 10, 200, 200, 300)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    Planet.update()
    Planet.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()