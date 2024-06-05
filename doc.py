import pygame
import random

WIDTH, HEIGHT = 800, 700
FPS = 30

MAX_ENEMY_ON_MAP = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 75, 78

ENEMY_VEL = 20

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Game with Enemies!")

# Spaceship image
PLAYER_IMAGE = pygame.image.load("assets/spaceship_horizontal.png")

# Enemy image
ENEMY_IMAGE = pygame.image.load('assets/enemy.png')

# Background image
SPACE_IMAGE = pygame.image.load('assets/background.png')
SPACE_IMAGE = pygame.transform.scale(SPACE_IMAGE, (WIDTH, HEIGHT))

# Player's rectangle
player = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

# Enemies list
enemies_list = []


def main():
	clock = pygame.time.Clock()

	running = True
	while running:
		clock.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		spawn_enemies()
		move_everything()
		draw()


def draw():
	# Draw the background and player
	WIN.blit(SPACE_IMAGE, (0, 0))
	WIN.blit(PLAYER_IMAGE, (player.x, player.y))

	# Draw enemies
	for enemy in enemies_list:
		WIN.blit(ENEMY_IMAGE, (enemy.x, enemy.y))
	pygame.display.update()


def spawn_enemies():
	if random.randint(0, 100) < 2 and len(enemies_list) < MAX_ENEMY_ON_MAP:
		x_location = WIDTH - 100
		y_location = random.randint(0, HEIGHT - SPACESHIP_HEIGHT)
		enemy = pygame.Rect(x_location, y_location, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
		enemies_list.append(enemy)


def move_everything():
	for enemy in enemies_list:
		enemy.x -= ENEMY_VEL
		if enemy.x + enemy.width < 0:
			enemies_list.remove(enemy)


if __name__ == "__main__":
	main()
