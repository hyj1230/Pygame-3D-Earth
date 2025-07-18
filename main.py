import pygame
import sys
from render import Render
from control import Control
from stats import Stats
import time

pygame.init()
w, h = 800, 600
screen = pygame.display.set_mode((w, h), pygame.RESIZABLE)
pygame.display.set_caption('pygame 3D地球仪')

clock = pygame.time.Clock()

render = Render()
control = Control()
stats = Stats(clock)

while 1:
    pygame_events = pygame.event.get()
    for event in pygame_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            w, h = screen.get_size()

    control.handle_event(pygame_events, w)
    control.update()

    screen.fill((255,)*3)
    render.render(screen, w, h)
    stats.render(screen)
    control.render(screen, w)

    pygame.display.flip()
    clock.tick(114514)
