import random
import pygame

# Initialize Pygame
pygame.init()

# Player's health, score
# __BONUS__
# health = 3
score = 0

# Screen dimensions
WIDTH, HEIGHT = 800, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Game with Enemies!")
running = True

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Game constants
FPS = 30  # frame rate
PLAYER_VEL = 5  # player velocity, pixel per frame
BULLET_VEL = 10  # bullet velocity
ENEMY_VEL = 20  # enemy velocity
MAX_ENEMY_ON_MAP = 15
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 75, 78
BULLET_COOLDOWN = 200  # milliseconds

# Fonts
FONT = pygame.font.SysFont('comicsans', 40)

# spaceship image
PLAYER_IMAGE = pygame.image.load("assets/spaceship_horizontal.png")

# enemy image
ENEMY_IMAGE = pygame.image.load('assets/enemy.png')

# BACKGROUND place holder, replace with image later
SPACE_IMAGE = pygame.image.load('assets/background.png')
SPACE_IMAGE = pygame.transform.scale(SPACE_IMAGE, (WIDTH, HEIGHT))

# rectangle to store yellow spaceship's location data
player = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

# Bullets and enemies
# __BONUS__
# last_bullet_time = 0
# yellow_bullets = []
enemies_list = []


# draw everything, including player, enemy, bullets, background
def draw():
    WIN.blit(SPACE_IMAGE, (0, 0))

    # put the yellow spaceship picture on the screen at
    # the position (yellow.x, yellow.y) which is the top left corner of
    # the yellow rectangle (spaceship)
    WIN.blit(PLAYER_IMAGE, (player.x, player.y))

    # __BONUS__
    # draw every bullet in the yellow_bullets list using
    # pygame.draw.rect to draw a rectangle
    # for bullet in yellow_bullets:
    #     pygame.draw.rect(WIN, YELLOW, bullet)

    # draw every enemy in the enemies list
    for enemy in enemies_list:
        WIN.blit(ENEMY_IMAGE, (enemy.x, enemy.y))

    # __BONUS__
    # show the health and score on the screen.
    # we use blit which stands for "block transfer", which is a
    # function that draws one surface onto another.
    # health_text = FONT.render("Health: " + str(health), 1, WHITE)
    # WIN.blit(health_text, (10, 10))

    # score is placed below health, with a gap of 10.
    # we do this by getting the health text's height and adding
    # it to the score text's height (from above)
    score_text = FONT.render("Score: " + str(score), 1, WHITE)
    # put score below health, do this by adding the height of the
    # health text to the score text's height (from above)
    WIN.blit(score_text, (10, 10))
    # __BONUS__
    # WIN.blit(score_text, (10, health_text.get_height() + 10))

    # updates the displaed screen
    pygame.display.update()

# __BONUS__
# shoot bullets by adding bullets to yellow_bullets list
# red shoot can be defined the same way but with diff buttons
# def player_shoot():
#     global last_bullet_time
#
#     # get pressed keys
#     keys_pressed = pygame.key.get_pressed()
#     if keys_pressed[pygame.K_SPACE]:  # shoot if space is pressed
#         current_time = pygame.time.get_ticks()
#         # get_ticks returns the number of milliseconds since pygame.init()
#         # check if the bullet cooldown is passed
#         # current_time - last_bullet_time = "time passed since last shot"
#         # check if the time passed is greater than the bullet cooldown (in milliseconds)
#         if current_time - last_bullet_time > BULLET_COOLDOWN:
#             # spawn the bullet at the right of the yellow spaceship
#             # and update the last_bullet_time to the current time
#             # we get the corrdinate by:
#             #     right of yellow spaceship = yellow.x + yellow.width
#             #     middle height of yellow spaceship = yellow.y + yellow.height // 2
#             bullet = pygame.Rect(player.x + player.width, player.y + player.height // 2 - 2, 10, 5)
#             yellow_bullets.append(bullet)
#             last_bullet_time = current_time


# randomly spawn red enemies (can change to another player)
# at the right of the screen
def spawn_enemies():
    # use random.randint to get a random number between 0 and 100
    # then, check if the number is less than 2, which has a
    # proability of 2%
    # we also want to check if the number of enemies is less than the max
    # number of enemies on the map to pervent too many enemies from spawning
    if random.randint(0, 100) < 2 and len(enemies_list) < MAX_ENEMY_ON_MAP:
        # spawn the enemy at the right of the screen
        # which is at y-coordinate equal to the width of the screen minus 100
        x_location = WIDTH - 100
        y_location = random.randint(0, HEIGHT - SPACESHIP_HEIGHT)
        enemy = pygame.Rect(x_location, y_location, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
        # add enemy to the list of enemies to be drawn
        enemies_list.append(enemy)


# move player accordint to input
def move_player():
    global player
    keys_pressed = pygame.key.get_pressed()

    # since left is 0, right is WIDTH
    # minus VEL to go left and add VEL to go right
    # make sure player is not going out of bounds

    # if A is pressed and player is not touching left wall
    # ensure by checking if yellow rectangle top left corner
    # is not touching left wall (0)
    if keys_pressed[pygame.K_a] and player.x > 0:  # LEFT
        player.x -= PLAYER_VEL
    # if D is pressed and player is not touching right wall
    # ensure by checking if yellow rectangle top right corner (yellow.x + yellow.width)
    # is not touching right wall (WIDTH)
    if keys_pressed[pygame.K_d] and player.x + player.width < WIDTH:  # RIGHT
        player.x += PLAYER_VEL
    # since top is 0, bottom is HEIGHT
    # minus VEL to move up and add VEL to move down

    # if W is pressed and player is not touching top wall
    if keys_pressed[pygame.K_w] and player.y - PLAYER_VEL > 0:  # UP
        player.y -= PLAYER_VEL
    # if S is pressed and player is not touching bottom wall
    if keys_pressed[pygame.K_s] and player.y + PLAYER_VEL + player.height < HEIGHT:  # DOWN
        player.y += PLAYER_VEL


# move everything, not including player
def move_everything():
    global yellow_bullets, enemies_list

    # __BONUS__
    # for bullet in yellow_bullets:  # go through all bullets
    #     bullet.x += BULLET_VEL  # move them to the right
    #
    #     # remove the bullet if it goes out of bounds
    #     # we do this by comparing the bullet's x position to the right wall (WIDTH)
    #     if bullet.x > WIDTH:
    #         yellow_bullets.remove(bullet)

    for enemy in enemies_list:  # go through all enemies
        enemy.x -= ENEMY_VEL  # move them to the left
        # want to remove the enemy if it goes out of bounds
        # we do this by comparing the enemy's x position to the left wall (0)
        if enemy.x + enemy.width < 0:
            enemies_list.remove(enemy)


# collision detection, including removal of enemies and detecting bullet hit
def check_collisions():
    # global health, yellow_bullets, enemies_list, score
    global enemies_list

    # go through all enemies and bullets
    # if enemy hits the player, remove the enemy and subtract 1 from health
    # for each enemy in the enemy list
    for enemy in enemies_list:
        if player.colliderect(enemy): # if player collides with the enemy
            # __BONUS__
            # health -= 1
            # enemies_list.remove(enemy)
            exit()

    # __BONUS__
    # if bullet hits the enemy, remove the enemy and bullet, and increase score
    # for bullet in yellow_bullets:
    #     for enemy in enemies_list:
    #         if bullet.colliderect(enemy):
    #             #yellow_bullets.remove(bullet)
    #             enemies_list.remove(enemy)
    #             score += 1
    #             break

# __BONUS__
# ending screen that shows up after the game ends
# def ending_screen():
#     global running
#
#     # display ending message
#     ending_text = FONT.render("YOU DIED!", 1, WHITE)
#     WIN.blit(ending_text, (WIDTH // 2 - ending_text.get_width() // 2, HEIGHT // 2 - ending_text.get_height() // 2))
#     # score is displayed below the ending message
#     score_text = FONT.render("Score: " + str(score), 1, WHITE)
#     WIN.blit(score_text, (
#     WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - score_text.get_height() // 2 + ending_text.get_height()))
#
#     # here, display is updated to show the ending text
#     # after that we no longer need to update so its outside of the main loop
#     pygame.display.update()
#
#     # main loop for ending screen
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#                 pygame.quit()
#
#         pygame.time.delay(100)
#
#     pygame.quit()


def main():
    global player, yellow_bullets, enemies_list, health, running

    # pygame clock that helps to control the frame rate
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(FPS) # limits frames per second

        # if cross is detected, we end the game by setting running as False
        # this way, we know that the game is quitted manually
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        # __BONUS__
        # player_shoot()  # BONUS
        spawn_enemies()  # 3rd
        check_collisions()  # 5th
        move_everything()  # 4th
        move_player()  # 2nd
        draw()  # first thing to add

        # __BONUS__
        # if health is 0, we end the game
        # if health <= 0:
        #     break

    # __BONUS__
    # ending_screen()  # last thing to add
    pygame.quit()


if __name__ == "__main__":
    print(PLAYER_IMAGE.get_rect().width, PLAYER_IMAGE.get_rect().height)
    main()
