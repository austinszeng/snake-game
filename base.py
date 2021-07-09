import pygame
from slider import Slider

# Set up
pygame.mixer.init()
pygame.init()
pygame.mixer.pre_init(44100,-16,2,512)
cell_size = 40
cell_number = 20
prison = cell_number * cell_size
window = pygame.display.set_mode((prison, prison))
pygame.display.set_caption('Snake! om nom nom')
clock = pygame.time.Clock()
SCREEN_UPDATE = pygame.USEREVENT + 1 # event trigger for update() speed
font = pygame.font.Font('Font/LEMONMILK-Medium.otf', 25)
font2 = pygame.font.Font('Font/Cabin-Bold.ttf', 22)

# add more foods (images) that user can buy/ choose from
egg = pygame.transform.scale((pygame.image.load('Assets/egg.png').convert_alpha()), (cell_size, cell_size))
coin = pygame.transform.scale((pygame.image.load('Assets/coin.png').convert_alpha()), (cell_size, cell_size))

# sound
bg_mus_1 = pygame.mixer.Sound('Music/sparks.wav')
pygame.mixer.Sound.set_volume(bg_mus_1, 0.3)
game_over_mus = pygame.mixer.Sound('Music/walking_with_you.wav')
pygame.mixer.Sound.set_volume(game_over_mus, 0.2)
hit_wall = pygame.mixer.Sound('Sound/bone.wav')
pygame.mixer.Sound.set_volume(hit_wall, 0.2)

# Make sliders for options/ settings page
slider_res = Slider((cell_size * cell_number / 2 - 150, cell_size * 6), 1, 300)
slider_spd = Slider((cell_size * cell_number / 2 - 150, cell_size * 8), 2, 150)

cell_size = int(slider_res.getValue() * 40)
# initialize speed value
ms_speed = int(220 - slider_spd.getValue() * 100)
pygame.time.set_timer(SCREEN_UPDATE, ms_speed) 


def draw_text_center(text, color, x, y, font):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center = (x, y))
    window.blit(text_surface, text_rect)

def draw_text_topleft(text, color, x, y, font):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(topleft = (x, y))
    window.blit(text_surface, text_rect)

def draw_grass(grass_color):
    for row in range(cell_number):
        if row % 2 == 0:
            for col in range(cell_number):
                if col % 2 == 0:
                    grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                    pygame.draw.rect(window, grass_color, grass_rect)
        else:
            for col in range(cell_number):
                if col % 2 != 0:
                    grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                    pygame.draw.rect(window, grass_color, grass_rect)

def reset_speed(): 
    ms_speed = int(220 - slider_spd.getValue() * 100)
    pygame.time.set_timer(SCREEN_UPDATE, ms_speed) 