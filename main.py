#Simple Snake Game by ET64 or reversal_lava63

import pygame
import random

#initializing pygame module
pygame.init()

#creating game window
screen_width = 800
screen_height = 600
game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Adventure by ET64")

#colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#game variables
player_size = 50
player_x = screen_width // 2 - player_size // 2
player_y = screen_height - player_size - 10
player_speed = 2.5

enemy_size = 50
enemy_x = random.randint(0, screen_width - enemy_size)
enemy_y = -50
enemy_speed = 1.5

score = 0
font = pygame.font.SysFont(None, 30)

#functions
def draw_player(x, y):
    pygame.draw.rect(game_window, white, [x, y, player_size, player_size])

def draw_enemy(x, y):
    pygame.draw.rect(game_window, red, [x, y, enemy_size, enemy_size])

def display_score(score):
    score_text = font.render("Score: " + str(score), True, white)
    game_window.blit(score_text, [10, 10])

def game_over():
    game_over_text = font.render("Game Over! Your score: " + str(score), True, white)
    game_window.blit(game_over_text, [screen_width//2 - 150, screen_height//2 - 30])
    pygame.display.update()
    pygame.time.delay(3000)
    pygame.quit()
    quit()

#game loop
game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    #player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_size:
        player_x += player_speed

    #enemy movement
    enemy_y += enemy_speed
    if enemy_y > screen_height:
        enemy_x = random.randint(0, screen_width - enemy_size)
        enemy_y = -50
        score += 1
        enemy_speed += 0.01

    #collision detection
    if player_x < enemy_x + enemy_size and player_x + player_size > enemy_x and player_y < enemy_y + enemy_size and player_y + player_size > enemy_y:
        game_over()

    #drawing on screen
    game_window.fill(black)
    draw_player(player_x, player_y)
    draw_enemy(enemy_x, enemy_y)
    display_score(score)
    pygame.display.update()

#quitting pygame
pygame.quit()
quit()
