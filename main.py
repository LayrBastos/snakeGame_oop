import pygame

black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
grass_green = (76, 153, 0)

pygame.init()
pygame.display.set_caption("Snake Game")
screen_width, screen_height = 1200, 800
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

