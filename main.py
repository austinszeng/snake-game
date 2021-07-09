import pygame, sys, base
from pygame.math import Vector2
from snake import SNAKE
from food import FOOD

class PLAYER:
    def __init__(self):
        self.coins = 0
        self.score = 0

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FOOD(0)
    
    # Updates every time base.SCREEN_UPDATE event is triggered
    def update(self):
        self.snake.move()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        base.draw_grass((167,209,61))
        self.fruit.draw_food()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize() # reposition fruit
            self.snake.add_block() # add another block to snake
            self.snake.play_eating_sound()
        
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize() # randomize fruit again if it lands on body

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < base.cell_number or not 0 <= self.snake.body[0].y < base.cell_number:
            self.game_over() 

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        player.coins += self.get_score()
        player.score = self.get_score()
        self.snake.reset() 
        pygame.mixer.Channel(3).play(base.hit_wall)
        pygame.mixer.Channel(2).play(base.game_over_mus)
        base.bg_mus_1.stop()
        game_over_screen()
    
    def draw_score(self):
        score_surface = base.font.render(str(len(self.snake.body) - 3), True, (255,255,255))
        score_rect = score_surface.get_rect(center = (base.cell_size * base.cell_number - base.cell_size, base.cell_size))
        egg_rect = base.egg.get_rect(midright = (score_rect.left, score_rect.centery))

        base.window.blit(score_surface, score_rect)
        base.window.blit(base.egg, egg_rect)

    def get_score(self):
        return len(self.snake.body) - 3

# variables for menus that have clickable buttons
click = False 
click1 = False
click2 = False
click3 = False
click4 = False
click5 = False
click6 = False
click7 = False
click8 = False

def main_menu():
    while True:
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        base.window.fill((200,220,60))
        base.draw_grass((167,209,61))
        pygame.draw.circle(base.window, (200,200,200), (base.cell_size * base.cell_number/2, base.cell_size * base.cell_number/2), base.cell_size * 5)

        # Display amount of coins
        currency_surface = base.font.render(str(player.coins), True, (255,255,255))
        currency_rect = currency_surface.get_rect(center = (base.cell_size * base.cell_number - base.cell_size, base.cell_size))
        coin_rect = base.coin.get_rect(midright = (currency_rect.left, currency_rect.centery))
        base.window.blit(currency_surface, currency_rect)
        base.window.blit(base.coin, coin_rect)

        mx, my = pygame.mouse.get_pos()

        button_play = pygame.Rect(base.cell_size * base.cell_number/2 - base.cell_size/2*3, base.cell_size * base.cell_number/2 - base.cell_size * 2, base.cell_size * 3, base.cell_size)
        button_store = pygame.Rect(base.cell_size * base.cell_number/2 - base.cell_size/2*3, base.cell_size * base.cell_number/2, base.cell_size * 3, base.cell_size)
        button_options = pygame.Rect(base.cell_size * base.cell_number/2 - base.cell_size/2*3, base.cell_size * base.cell_number/2 + base.cell_size * 2, base.cell_size * 3, base.cell_size)

        if button_play.collidepoint((mx,my)):
            if click:
                game()
        if button_store.collidepoint((mx,my)):
            if click:
                store()
        if button_options.collidepoint((mx,my)):
            if click:
                options()

        pygame.draw.rect(base.window, (255,255,255), button_play)
        pygame.draw.rect(base.window, (255,255,255), button_store)
        pygame.draw.rect(base.window, (255,255,255), button_options)
        base.draw_text_topleft("PLAY", (0,0,0), button_play.x + 25, button_play.y + 4, base.font2)
        base.draw_text_topleft("STORE", (0,0,0), button_store.x + 17, button_store.y + 3, base.font2)
        base.draw_text_topleft("OPTIONS", (0,0,0), button_options.x + 3, button_options.y + 3, base.font2)

        pygame.display.update()
        base.clock.tick(60)

def store():
    while True:
        click1 = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click1 = True

        base.window.fill((200,220,60))
        base.draw_text_center('STORE', (255,255,255), (base.cell_size * base.cell_number)/2, (base.cell_size * base.cell_number)/5, base.font)

        # Display amount of coins
        currency_surface = base.font.render(str(player.coins), True, (255,255,255))
        currency_rect = currency_surface.get_rect(center = (base.cell_size * base.cell_number - base.cell_size, base.cell_size))
        coin_rect = base.coin.get_rect(midright = (currency_rect.left, currency_rect.centery))
        base.window.blit(currency_surface, currency_rect)
        base.window.blit(base.coin, coin_rect)

        mx, my = pygame.mouse.get_pos()

        button_snakes = pygame.Rect(base.cell_size * base.cell_number/2 - base.cell_size/2*5, base.cell_size * base.cell_number/2 - base.cell_size * 2, base.cell_size * 5, base.cell_size)
        button_food = pygame.Rect(base.cell_size * base.cell_number/2 - base.cell_size/2*5, base.cell_size * base.cell_number/2, base.cell_size * 5, base.cell_size)
        button_backgrounds = pygame.Rect(base.cell_size * base.cell_number/2 - base.cell_size/2*5, base.cell_size * base.cell_number/2 + base.cell_size * 2, base.cell_size * 5, base.cell_size)
        button_main_menu = pygame.Rect(base.cell_size, base.cell_size * base.cell_number - base.cell_size * 2, base.cell_size * 2, base.cell_size)

        if button_snakes.collidepoint((mx,my)):
            if click1:
                snake_options()
        if button_food.collidepoint((mx,my)):
            if click1:
                food_options()
        if button_backgrounds.collidepoint((mx,my)):
            if click1:
                background_options()
        if button_main_menu.collidepoint((mx,my)):
            if click1:
                main_menu()

        pygame.draw.rect(base.window, (255,255,255), button_snakes)
        pygame.draw.rect(base.window, (255,255,255), button_food)
        pygame.draw.rect(base.window, (255,255,255), button_backgrounds)
        pygame.draw.rect(base.window, (255,255,255), button_main_menu)
        base.draw_text_topleft("SNAKES", (0,0,0), button_snakes.x + 30, button_snakes.y + 4, base.font2)
        base.draw_text_topleft("FOOD", (0,0,0), button_food.x + 22, button_food.y + 4, base.font2)
        base.draw_text_topleft("BACKGROUNDS", (0,0,0), button_backgrounds.x + 8, button_backgrounds.y + 4, base.font2)
        base.draw_text_topleft("BACK", (0,0,0), button_main_menu.x + 10, button_main_menu.y + 4, base.font2)

        pygame.display.update()
        base.clock.tick(60)

def snake_options():
    while True:
        click2 = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click2 = True

        base.window.fill((200,220,60))
        base.draw_text_center('Choose your snake!', (255,255,255), (base.cell_size * base.cell_number)/2, (base.cell_size * base.cell_number)/5, base.font)

        # Display amount of coins
        currency_surface = base.font.render(str(player.coins), True, (255,255,255))
        currency_rect = currency_surface.get_rect(center = (base.cell_size * base.cell_number - base.cell_size, base.cell_size))
        coin_rect = base.coin.get_rect(midright = (currency_rect.left, currency_rect.centery))
        base.window.blit(currency_surface, currency_rect)
        base.window.blit(base.coin, coin_rect)

        mx, my = pygame.mouse.get_pos()

        button_store = pygame.Rect(base.cell_size, base.cell_size * base.cell_number - base.cell_size * 2, base.cell_size * 2, base.cell_size)

        if button_store.collidepoint((mx,my)):
            if click2:
                store()

        pygame.draw.rect(base.window, (255,255,255), button_store)
        base.draw_text_topleft("BACK", (0,0,0), button_store.x + 10, button_store.y + 4, base.font2)

        pygame.display.update()
        base.clock.tick(60)

def food_options():
    while True:
        click3 = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click3 = True

        base.window.fill((200,220,60))
        base.draw_text_center('What would your snake like to eat?', (255,255,255), (base.cell_size * base.cell_number)/2, (base.cell_size * base.cell_number)/5, base.font)

        # Display amount of coins
        currency_surface = base.font.render(str(player.coins), True, (255,255,255))
        currency_rect = currency_surface.get_rect(center = (base.cell_size * base.cell_number - base.cell_size, base.cell_size))
        coin_rect = base.coin.get_rect(midright = (currency_rect.left, currency_rect.centery))
        base.window.blit(currency_surface, currency_rect)
        base.window.blit(base.coin, coin_rect)

        mx, my = pygame.mouse.get_pos()

        button_store = pygame.Rect(base.cell_size, base.cell_size * base.cell_number - base.cell_size * 2, base.cell_size * 2, base.cell_size)

        if button_store.collidepoint((mx,my)):
            if click3:
                store()

        pygame.draw.rect(base.window, (255,255,255), button_store)
        base.draw_text_topleft("BACK", (0,0,0), button_store.x + 10, button_store.y + 4, base.font2)

        pygame.display.update()
        base.clock.tick(60)

def background_options():
    while True:
        click4 = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click4 = True

        base.window.fill((200,220,60))
        base.draw_text_center('Choose a habitat for your snake to play in!', (255,255,255), (base.cell_size * base.cell_number)/2, (base.cell_size * base.cell_number)/5, base.font)

        # Display amount of coins
        currency_surface = base.font.render(str(player.coins), True, (255,255,255))
        currency_rect = currency_surface.get_rect(center = (base.cell_size * base.cell_number - base.cell_size, base.cell_size))
        coin_rect = base.coin.get_rect(midright = (currency_rect.left, currency_rect.centery))
        base.window.blit(currency_surface, currency_rect)
        base.window.blit(base.coin, coin_rect)

        mx, my = pygame.mouse.get_pos()
        
        button_store = pygame.Rect(base.cell_size, base.cell_size * base.cell_number - base.cell_size * 2, base.cell_size * 2, base.cell_size)

        if button_store.collidepoint((mx,my)):
            if click4:
                store()

        pygame.draw.rect(base.window, (255,255,255), button_store)
        base.draw_text_topleft("BACK", (0,0,0), button_store.x + 10, button_store.y + 4, base.font2)

        pygame.display.update()
        base.clock.tick(60)

def options():
    running = True
    click5 = False
    while running:
        # base.cell_size = int(base.slider_res.getValue() * 40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_ESCAPE:
                #     # change refresh speed after exiting options to apply changes
                #     ms_speed = int(220 - base.slider_spd.getValue() * 100)
                #     pygame.time.set_timer(base.SCREEN_UPDATE, ms_speed) 
                #     running = False 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click5 = True

            # if event.type == pygame.VIDEORESIZE:
            #     scrsize = event.size
            #     width = event.w
            #     height = event.h
            #     base.window = pygame.display.set_mode(scrsize, pygame.RESIZABLE)


        base.window.fill((200,220,60))
        base.draw_text_center('OPTIONS', (255,255,255), (base.cell_size * base.cell_number)/2, (base.cell_size * base.cell_number)/5, base.font)

        base.slider_res.render(base.window, 'RESOLUTION')
        base.slider_res.changeValue()

        base.slider_spd.render(base.window, 'SPEED')
        base.slider_spd.changeValue()

        # Main menu and play buttons
        mx, my = pygame.mouse.get_pos()

        button_main_menu = pygame.Rect(base.cell_size, base.cell_size * base.cell_number - base.cell_size * 2, base.cell_size * 2, base.cell_size)

        if button_main_menu.collidepoint((mx,my)):
            if click5:
                # change refresh speed after exiting options to apply changes
                base.reset_speed()
                main_menu()

        pygame.draw.rect(base.window, (255,255,255), button_main_menu)
        base.draw_text_topleft("BACK", (0,0,0), button_main_menu.x + 6, button_main_menu.y + 3, base.font2)

        pygame.display.update()
        base.clock.tick(60)

# copy of options() menu but with a resume button
def options_resume():
    running = True
    click6 = False
    init_spd = base.slider_spd.getValue()
    while running:
        # base.cell_size = int(base.slider_res.getValue() * 40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_ESCAPE:
            #         # change refresh speed after exiting options to apply changes
            #         ms_speed = int(220 - base.slider_spd.getValue() * 100)
            #         pygame.time.set_timer(base.SCREEN_UPDATE, ms_speed) 
            #         running = False 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click6 = True

            # if event.type == pygame.VIDEORESIZE:
            #     scrsize = event.size
            #     width = event.w
            #     height = event.h
            #     base.window = pygame.display.set_mode(scrsize, pygame.RESIZABLE)


        base.window.fill((200,220,60))
        base.draw_text_center('OPTIONS', (255,255,255), (base.cell_size * base.cell_number)/2, (base.cell_size * base.cell_number)/5, base.font)

        base.slider_res.render(base.window, 'RESOLUTION')
        base.slider_res.changeValue()

        base.slider_spd.render(base.window, 'SPEED')
        base.slider_spd.changeValue()

        if init_spd != base.slider_spd.getValue():
            base.draw_text_center('Your changes will be applied next game.', (255,255,255), (base.cell_size * base.cell_number)/2, (base.cell_size * base.cell_number)/2 + base.cell_size * 2, base.font2)

        # Main menu and play buttons
        mx, my = pygame.mouse.get_pos()

        button_main_menu = pygame.Rect(base.cell_size, base.cell_size * base.cell_number - base.cell_size * 2, base.cell_size * 4, base.cell_size)
        button_play = pygame.Rect(base.cell_size * base.cell_number - base.cell_size * 3, base.cell_size * base.cell_number - base.cell_size * 2, base.cell_size * 2, base.cell_size)

        if button_main_menu.collidepoint((mx,my)):
            if click6:
                base.reset_speed() # change refresh speed after exiting options to apply changes
                main_game.snake.reset() # restart game
                main_menu()

        if button_play.collidepoint((mx,my)):
            if click6:
                game()

        pygame.draw.rect(base.window, (255,255,255), button_play)
        pygame.draw.rect(base.window, (255,255,255), button_main_menu)
        base.draw_text_topleft("PLAY", (0,0,0), button_play.x + 12, button_play.y + 4, base.font2)
        base.draw_text_topleft("MAIN MENU", (0,0,0), button_main_menu.x + 10, button_main_menu.y + 4, base.font2)

        pygame.display.update()
        base.clock.tick(60)

first_key_press = False
main_game = MAIN()
player = PLAYER()
def game():
    running = True
    first_key_press = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == base.SCREEN_UPDATE:
                if first_key_press:
                    main_game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # esc gets out of game
                    running = False
                    base.bg_mus_1.stop()
                    pause_screen()
                if first_key_press == False:
                    base.bg_mus_1.play()
                    first_key_press = True
                # prevent snake from going into itself by going opposite direction
                # WASD
                if event.key == pygame.K_w:
                    if main_game.snake.direction.y != 1: 
                        main_game.snake.direction = Vector2(0,-1)
                if event.key == pygame.K_a:
                    if main_game.snake.direction.x != 1:
                        main_game.snake.direction = Vector2(-1,0)
                if event.key == pygame.K_s:
                    if main_game.snake.direction.y != -1:
                        main_game.snake.direction = Vector2(0,1)
                if event.key == pygame.K_d:
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(1,0)

                # ARROW KEYS
                if event.key == pygame.K_UP:
                    if main_game.snake.direction.y != 1:
                        main_game.snake.direction = Vector2(0,-1)
                if event.key == pygame.K_LEFT:
                    if main_game.snake.direction.x != 1:
                        main_game.snake.direction = Vector2(-1,0)
                if event.key == pygame.K_DOWN:
                    if main_game.snake.direction.y != -1:
                        main_game.snake.direction = Vector2(0,1)
                if event.key == pygame.K_RIGHT:
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(1,0)

        base.window.fill((200,220,60))
        main_game.draw_elements()

        pygame.display.update()
        base.clock.tick(60)

def pause_screen():
    while True:
        click7 = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click7 = True

        # base.window.fill((200,220,60))
        # base.draw_grass()
        pygame.draw.circle(base.window, (200,200,200), ((base.cell_size * base.cell_number)/2, (base.cell_size * base.cell_number)/2), base.cell_size * 5)
        base.draw_text_center('PAUSED', (255,255,255), (base.cell_size * base.cell_number)/2, (base.cell_size * base.cell_number)/2 - base.cell_size, base.font)

        mx, my = pygame.mouse.get_pos()

        button_play = pygame.Rect(base.cell_size * base.cell_number/2 - base.cell_size * 4, base.cell_size * base.cell_number/2, base.cell_size * 3, base.cell_size)
        button_options = pygame.Rect(base.cell_size * base.cell_number/2 + base.cell_size, base.cell_size * base.cell_number/2, base.cell_size * 3, base.cell_size)
        button_main_menu = pygame.Rect(base.cell_size * base.cell_number/2 - base.cell_size * 2, base.cell_size * base.cell_number/2 + base.cell_size*2, base.cell_size * 4, base.cell_size)

        if button_play.collidepoint((mx,my)):
            if click7:
                game()
        if button_options.collidepoint((mx,my)):
            if click7:
                options_resume()
        if button_main_menu.collidepoint((mx,my)):
            if click7:
                # restart game
                main_game.snake.reset()
                main_menu()

        pygame.draw.rect(base.window, (255,255,255), button_play)
        pygame.draw.rect(base.window, (255,255,255), button_options)
        pygame.draw.rect(base.window, (255,255,255), button_main_menu)
        base.draw_text_topleft("RESUME", (0,0,0), button_play.x + 8, button_play.y + 3, base.font2)
        base.draw_text_topleft("OPTIONS", (0,0,0), button_options.x + 2, button_options.y + 3, base.font2)
        base.draw_text_topleft("MAIN MENU", (0,0,0), button_main_menu.x + 5, button_main_menu.y + 3, base.font2)

        pygame.display.update()
        base.clock.tick(60)

def game_over_screen():
    while True:
        click8 = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click8 = True

        base.window.fill((200,220,60))
        base.draw_grass((167,209,61))
        pygame.draw.circle(base.window, (200,200,200), ((base.cell_size * base.cell_number)/2, (base.cell_size * base.cell_number)/2), base.cell_size * 5)
        base.draw_text_center('GAME OVER', (255,255,255), (base.cell_size * base.cell_number)/2, (base.cell_size * base.cell_number)/2 - base.cell_size, base.font)
        base.draw_text_center(f'SCORE: {player.score}', (255,255,255), (base.cell_size * base.cell_number)/2, (base.cell_size * base.cell_number)/2 + base.cell_size/8, base.font)

        mx, my = pygame.mouse.get_pos()

        button_play = pygame.Rect(base.cell_size * base.cell_number/2 - base.cell_size * 4, base.cell_size * base.cell_number/2 + base.cell_size, base.cell_size * 4, base.cell_size)
        button_main_menu = pygame.Rect(base.cell_size * base.cell_number/2 + base.cell_size, base.cell_size * base.cell_number/2 + base.cell_size, base.cell_size * 4, base.cell_size)

        if button_play.collidepoint((mx,my)):
            if click8:
                base.reset_speed() 
                base.game_over_mus.fadeout(500)
                game()
 
        if button_main_menu.collidepoint((mx,my)):
            if click8:
                base.game_over_mus.fadeout(500)
                main_menu()

        pygame.draw.rect(base.window, (255,255,255), button_play)
        pygame.draw.rect(base.window, (255,255,255), button_main_menu)
        base.draw_text_topleft("PLAY AGAIN", (0,0,0), button_play.x + 15, button_play.y + 4, base.font2)
        base.draw_text_topleft("MAIN MENU", (0,0,0), button_main_menu.x + 10, button_main_menu.y + 4, base.font2)

        pygame.display.update()
        base.clock.tick(60)

main_menu() # game starts at main menu