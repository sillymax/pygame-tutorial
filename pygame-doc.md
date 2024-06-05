### Table of content
- [Initialization](#initialization)
	- [Initialize window, etc.](#initialize-the-game)
	- [Event loop](#event-loop)
- [Drawing](#drawing)
	- [Draw background](#draw-background)
- [Spawn enemies](#spawn-enemies)

## Initialization
- Import the pygame module
- Structure the main function

```py
import pygame


def main():
	pass
	# Initialize window, etc.


if __name__ == "__main__":
	main()
```

---

### Initialize window, etc.
- Set the game loop
- Set the tick rate
```py
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Game with Enemies!")

def main():
	clock = pygame.time.Clock()

	running = True
	while running:
		clock.tick(FPS)
		# Event loop
```

---

### Event loop
- Check for events
```py
for event in pygame.event.get():
	if event.type == pygame.QUIT:
		running = False
```

## Drawing
- Drawing the window, spaceship, enemies, etc.
```py
def draw():
	# Draw components
	pygame.display.update()
```
- Loading images
```py
# Spaceship image
PLAYER_IMAGE = pygame.image.load("assets/spaceship_horizontal.png")

# Enemy image
ENEMY_IMAGE = pygame.image.load('assets/enemy.png')

# Background image
SPACE_IMAGE = pygame.image.load('assets/background.png')
SPACE_IMAGE = pygame.transform.scale(SPACE_IMAGE, (WIDTH, HEIGHT))
```

---

### Draw background
```py
def draw():
	WIN.blit(SPACE_IMAGE, (0, 0))
```

## Spawn enemies
- Randomly spawn enemies
- Check if the number of enemies on the map is less than the maximum number of enemies allowed
- Use `random.randint` to randomly spawn enemies
- Use `pygame.Rect` to create a rectangle for the enemy
```py
def spawn_enemies():
	if random.randint(0, 100) < 2 and len(enemies_list) < MAX_ENEMY_ON_MAP:
		x_location = WIDTH - 100
		y_location = random.randint(0, HEIGHT - SPACESHIP_HEIGHT)
		enemy = pygame.Rect(x_location, y_location, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
		enemies_list.append(enemy)
```
