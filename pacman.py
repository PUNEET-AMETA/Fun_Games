# -*- coding: utf-8 -*-
"""


@author: ameta
"""

import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man (Simplified)")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

player_size = 20
player_pos = [WIDTH // 2, HEIGHT // 2]
player_speed = 5

enemy_size = 20
enemy_pos = [random.randint(0, WIDTH - enemy_size), random.randint(0, HEIGHT - enemy_size)]
enemy_speed = 3

food_size = 10
food_pos = [random.randint(0, WIDTH - food_size), random.randint(0, HEIGHT - food_size)]

score = 0

def draw_text(text, x, y, color):
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN] and player_pos[1] < HEIGHT - player_size:
        player_pos[1] += player_speed

    if enemy_pos[0] < player_pos[0]:
        enemy_pos[0] += enemy_speed
    if enemy_pos[0] > player_pos[0]:
        enemy_pos[0] -= enemy_speed
    if enemy_pos[1] < player_pos[1]:
        enemy_pos[1] += enemy_speed
    if enemy_pos[1] > player_pos[1]:
        enemy_pos[1] -= enemy_speed

    if abs(player_pos[0] - food_pos[0]) < food_size and abs(player_pos[1] - food_pos[1]) < food_size:
        score += 1
        food_pos = [random.randint(0, WIDTH - food_size), random.randint(0, HEIGHT - food_size)]

    if abs(player_pos[0] - enemy_pos[0]) < enemy_size and abs(player_pos[1] - enemy_pos[1]) < enemy_size:
        draw_text("Game Over!", WIDTH // 2 - 80, HEIGHT // 2 - 20, RED)
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    pygame.draw.rect(screen, YELLOW, (*player_pos, player_size, player_size))
    pygame.draw.rect(screen, RED, (*enemy_pos, enemy_size, enemy_size))
    pygame.draw.rect(screen, WHITE, (*food_pos, food_size, food_size))

    draw_text(f"Score: {score}", 10, 10, WHITE)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
