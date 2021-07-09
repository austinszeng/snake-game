import pygame, random, base
from pygame.math import Vector2

class FOOD:
    def __init__(self, price):
        self.x = random.randint(0,base.cell_number - 1)
        self.y = random.randint(0,base.cell_number - 1)
        self.pos = Vector2(self.x, self.y)
        self.price = price
    
    def draw_food(self):
        food_rect = pygame.Rect(self.pos.x * base.cell_size, self.pos.y * base.cell_size, base.cell_size, base.cell_size)
        base.window.blit(base.egg, food_rect)

    def randomize(self):
        self.x = random.randint(0,base.cell_number - 1)
        self.y = random.randint(0,base.cell_number - 1)
        self.pos = Vector2(self.x, self.y)