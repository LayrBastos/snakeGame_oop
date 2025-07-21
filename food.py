import pygame
import random

class Food:
    def __init__(self, size, color):
        self.size = size
        self.color = color
       
    def generate(self, screen_width, screen_height):
        x = round(random.randrange(0, screen_width - self.size) / float(self.size)) * float(self.size)
        y = round(random.randrange(0, screen_height - self.size) / float(self.size)) * float(self.size)
        return x, y
    
    def draw(self, screen, x, y):
        pygame.draw.rect(screen, self.color, [x, y, self.size, self.size])
        