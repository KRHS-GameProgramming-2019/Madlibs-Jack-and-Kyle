import pygame, random, sys
from pygame.locals import *
pygame.init()

res = (700,437)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(res)
pygame.display.set_caption('Gibby')

gibby = pygame.image.load("gibby.jpg")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.blit(gibby,(0,0))
    clock.tick(60)
    pygame.display.flip()
