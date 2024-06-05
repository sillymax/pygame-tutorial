### Table of content
- [Initialization](#initialization)
	- [Initialize window, etc.](#initialize-the-game)

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
		# event loop
```
