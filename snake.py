import pygame, random, base
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        start_pos = [[Vector2(4,10), Vector2(3,10), Vector2(2,10)], 
                     [Vector2(16,10), Vector2(17,10), Vector2(18,10)], 
                     [Vector2(10,4), Vector2(10,3), Vector2(10,2)], 
                     [Vector2(10,16), Vector2(10,17), Vector2(10,18)]]
        random_pos = random.randint(0,3)
        self.body = start_pos[random_pos]
        self.direction = Vector2(0,0)
        self.new_block = False
        self.score = str((len(self.body) - 3))

        # import default snake parts
        self.head_up = pygame.transform.scale((pygame.image.load('Assets/head_up.png').convert_alpha()), (base.cell_size, base.cell_size))
        self.head_down = pygame.transform.scale((pygame.image.load('Assets/head_down.png').convert_alpha()), (base.cell_size, base.cell_size))
        self.head_right = pygame.transform.scale((pygame.image.load('Assets/head_right.png').convert_alpha()), (base.cell_size, base.cell_size))
        self.head_left = pygame.transform.scale((pygame.image.load('Assets/head_left.png').convert_alpha()), (base.cell_size, base.cell_size))

        self.tail_up = pygame.transform.scale((pygame.image.load('Assets/tail_up.png').convert_alpha()), (base.cell_size, base.cell_size))
        self.tail_down = pygame.transform.scale((pygame.image.load('Assets/tail_down.png').convert_alpha()), (base.cell_size, base.cell_size))
        self.tail_right = pygame.transform.scale((pygame.image.load('Assets/tail_right.png').convert_alpha()), (base.cell_size, base.cell_size))
        self.tail_left = pygame.transform.scale((pygame.image.load('Assets/tail_left.png').convert_alpha()), (base.cell_size, base.cell_size))

        self.body_vertical = pygame.transform.scale((pygame.image.load('Assets/body_vertical.png').convert_alpha()), (base.cell_size, base.cell_size))
        self.body_horizontal = pygame.transform.scale((pygame.image.load('Assets/body_horizontal.png').convert_alpha()), (base.cell_size, base.cell_size))

        self.body_tr = pygame.transform.scale((pygame.image.load('Assets/body_tr.png').convert_alpha()), (base.cell_size, base.cell_size))
        self.body_tl = pygame.transform.scale((pygame.image.load('Assets/body_tl.png').convert_alpha()), (base.cell_size, base.cell_size))
        self.body_br = pygame.transform.scale((pygame.image.load('Assets/body_br.png').convert_alpha()), (base.cell_size, base.cell_size))
        self.body_bl = pygame.transform.scale((pygame.image.load('Assets/body_bl.png').convert_alpha()), (base.cell_size, base.cell_size))

        self.eating_sound = pygame.mixer.Sound('Sound/crunch.wav')
        pygame.mixer.Sound.set_volume(self.eating_sound, 0.4)


    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            block_rect = pygame.Rect(block.x * base.cell_size, block.y * base.cell_size, base.cell_size, base.cell_size)
            if index == 0: # head
                base.window.blit(self.head, block_rect)
            elif index == len(self.body) - 1: # tail
                base.window.blit(self.tail, block_rect)
            else:
                prev_block_relation = self.body[index + 1] - block
                next_block_relation = self.body[index - 1] - block
                if prev_block_relation.x == next_block_relation.x: # if x coords are same, snake is vertical
                    base.window.blit(self.body_vertical, block_rect)
                elif prev_block_relation.y == next_block_relation.y: # if y coords are same, snake is horizontal
                    base.window.blit(self.body_horizontal, block_rect)
                else: # for corners
                    if prev_block_relation.y == -1 and next_block_relation.x == -1 or prev_block_relation.x == -1 and next_block_relation.y == -1:
                        base.window.blit(self.body_tl, block_rect)
                    elif prev_block_relation.y == 1 and next_block_relation.x == -1 or next_block_relation.y == 1 and prev_block_relation.x == -1:
                        base.window.blit(self.body_bl, block_rect)
                    elif prev_block_relation.y == -1 and next_block_relation.x == 1 or next_block_relation.y == -1 and prev_block_relation.x == 1:
                        base.window.blit(self.body_tr, block_rect)
                    elif prev_block_relation.y == 1 and next_block_relation.x == 1 or next_block_relation.y == 1 and prev_block_relation.x == 1:
                        base.window.blit(self.body_br, block_rect)
    
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): 
            self.head = self.head_left
        elif head_relation == Vector2(-1,0): 
            self.head = self.head_right
        elif head_relation == Vector2(0,1): 
            self.head = self.head_up
        elif head_relation == Vector2(0,-1): 
            self.head = self.head_down
    
    def update_tail_graphics(self):
        tail_relation = self.body[len(self.body)-2] - self.body[len(self.body)-1]
        if tail_relation == Vector2(1,0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): 
            self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): 
            self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): 
            self.tail = self.tail_down

    def move(self):
        if self.new_block == True:
            body_copy = self.body[:] # don't exclude last element
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1] # exclude last element
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def play_eating_sound(self):
        pygame.mixer.Channel(1).play(self.eating_sound)

    def reset(self):
        start_pos = [[Vector2(4,10), Vector2(3,10), Vector2(2,10)], 
                    [Vector2(16,10), Vector2(17,10), Vector2(18,10)], 
                    [Vector2(10,4), Vector2(10,3), Vector2(10,2)], 
                    [Vector2(10,16), Vector2(10,17), Vector2(10,18)]]
        random_pos = random.randint(0,3)
        self.body = start_pos[random_pos]
        self.direction = Vector2(0,0)
        # reset speed after a new game
    base.reset_speed() 