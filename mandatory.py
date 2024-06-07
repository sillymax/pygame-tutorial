import pygame
import random

#Initialize pygame
pygame.init()

#Set FPS and Clock
FPS = 60
clock = pygame.time.Clock()

#Create window
window_width = 800
window_height = 700
window = pygame.display.set_mode((window_width, window_height))

#Set game values
enemy_velocity = 10
player_velocity = 5

#Set images
background_image = pygame.image.load("assets/background.png")
background_rect = background_image.get_rect()

player_image = pygame.image.load("assets/spaceship_horizontal.png")
player_rect = player_image.get_rect()
player_rect.left = 100
player_rect.centery = window_height//2

enemy_image = pygame.image.load("assets/enemy.png")

#Set enemies intial positions
num_enemies = 5
buffer_distance = 500
enemies = []
for _ in range(num_enemies):
    enemy_rect = enemy_image.get_rect()
    enemy_rect.left = random.randint(window_width, window_width + buffer_distance)
    enemy_rect.centery = random.randint(0, window_height - 48)
    enemies.append(enemy_rect)

#The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Continous movement
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_UP] and player_rect.top > 0:
        player_rect.y -= player_velocity
    if key_pressed[pygame.K_DOWN] and player_rect.bottom < window_height:
        player_rect.y += player_velocity
    
    #Move the enemy
    for enemy_rect in enemies:
        if enemy_rect.right < 0:
            enemy_rect.left = random.randint(window_width, window_width + buffer_distance)
            enemy_rect.centery = random.randint(0, window_height - 48)
        else:
            enemy_rect.x -= enemy_velocity

        if player_rect.colliderect(enemy_rect):
            quit()

    #Blit (copying) images
    window.blit(background_image, background_rect)
    window.blit(player_image, player_rect)

    for enemy_rect in enemies:
        window.blit(enemy_image, enemy_rect)

    #Update the display
    pygame.display.update()
    clock.tick(FPS)
