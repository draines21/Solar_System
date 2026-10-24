import pygame
from planet import Planets

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

Planet = Planets("Earth", "blue",(640, 360), 3.0, 10, 10)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    Planet.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()