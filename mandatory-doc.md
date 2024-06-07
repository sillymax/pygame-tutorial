# Mandatory
[Click here for complete code](./mandatory.py)

### Table of content
- [Setup](#setup)
	- [Initialize Pygame](#initialize-pygame)
	- [Create Window](#create-window)
	- [Event Handling](#event-handling)
   		- [Close Button Event](#close-button-event)
- [Drawing](#drawing)
	- [Draw background](#draw-background)
	- [Draw player](#draw-player)
- [Spawn enemies](#spawn-enemies)
	- [Draw enemies](#draw-enemies)
- [Movement](#movement)
	- [Move enemies](#move-enemies)
	- [Move player](#move-player)
- [Collision](#collision)

## Setup
### Initialize Pygame
```py
import pygame

pygame.init()
# You must call init() at the start of every project,
# to activate pygame library.
```

---

### Create Window
```py
WIDTH = 500
HEIGHT = 700
window = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_mode() is used to create a window of WIDTH wide and HEIGHT tail.
# We store it in 'window', so that we can refer to it later in our code.

pygame.display.set_caption("Simple Game with Enemies")
# Set the window title on the top-left
```
Try running the game now. You might notice that the window only appears for a second.
This is because we need to create a "game loop" to keep the window open.

---

### Create Game Loop
```py
running = True
# 'running' is like a switch that keeps the game running.
# We start with the switch set to 'on' (True), so the game starts.
while running:
# This loop keeps the game running
	pass
	# We'll add more code here later to make the game do things!
```
Now, try running the game again. It's running, but when you try to close it by clicking the close button on the window, nothing happens.
We'll fix this by adding something special called "event handling" to make the game respond when you want to close it.

---

### Event Handling
```py
running = True
while running:
	for event in pygame.event.get():
	# Event handling allows our game to respond to things that happen, like clicking the close button.
		print(event)
		# Print the event and see what's happening. We'll remove this later!
```
Try running the game and see what events are printed!

---

### Close Button Event
```py
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
		# This part checks if we clicked the close button on the window.
			running = False
			# If we did click the close button, we turn the switch 'off' (set running to False).
```
Try running the game again. This time, when you click the close button, the game should close!

---

## Drawing On The Window
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

---

### Draw player
- Create a rectangle for the player
- Draw the player based on the rectangle (x, y)
```py
player = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

def draw():
	# Components drawn before
	WIN.blit(PLAYER_IMAGE, (player.x, player.y))
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

---

### Draw enemies
- Up until now, the enemies will not "move" because we are not updating their position
```py
def draw():
	# Components drawn before
	for enemy in enemies_list:
		WIN.blit(ENEMY_IMAGE, (enemy.x, enemy.y))
```

## Movement
- Now we handle all the movement of the player and the enemies

### Move enemies
- Move the enemies to the left on a constant velocity
- If the enemy is off the screen, remove it from the list

```py
def move_everything():
	for enemy in enemies_list:
		enemy.x -= ENEMY_VEL
		if enemy.x + enemy.width < 0:
			enemies_list.remove(enemy)
```

---

### Move player
- Move the player based on the key pressed
- Check if the player is within the screen boundaries
- Update the player's position
```py
def move_player():
	global player
	keys_pressed = pygame.key.get_pressed()

	if keys_pressed[pygame.K_a] and player.x > 0:
		player.x -= PLAYER_VEL

	if keys_pressed[pygame.K_d] and player.x + player.width < WIDTH:
		player.x += PLAYER_VEL

	if keys_pressed[pygame.K_w] and player.y - PLAYER_VEL > 0:
		player.y -= PLAYER_VEL

	if keys_pressed[pygame.K_s] and player.y + PLAYER_VEL + player.height < HEIGHT:
		player.y += PLAYER_VEL
```

## Collision
- Check if the player collides with an enemy
- Using `colliderect`
- If the player collides with an enemy, exit the game
```py
def check_collision():
	for enemy in enemies_list:
		if player.colliderect(enemy):
			exit()
```
