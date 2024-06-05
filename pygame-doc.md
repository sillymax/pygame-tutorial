### Table of content
- [Initialization](#initialization)
	- [Initialize window, etc.](#initialize-the-game)
	- [Event loop](#event-loop)

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

### Initialize window, etc.
- Set the game loop
- Set the tick rate
```py
def main():
	pygame.init()
	WIN = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Simple Game with Enemies!")
	clock = pygame.time.Clock()

	running = True
	while running:
		clock.tick(FPS)
		# Event loop
```

### Event loop
- Check for events
```py
for event in pygame.event.get():
	if event.type == pygame.QUIT:
		running = False
```
