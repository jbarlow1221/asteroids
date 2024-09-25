import pygame
from constants import *
from player import *
from asteroids import *
from asteroidfield import *
def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	black = (0, 0, 0)
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	shootables = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (shootables, updatable, drawable)
	AsteroidField.containers = (updatable)
	player = Player(x, y)
	asteroid_field = AsteroidField()
	while True:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return
		dt = clock.tick(60) / 1000
		for sprite in updatable:
			sprite.update(dt)
		screen.fill(black)
		for thing in drawable:
			thing.draw(screen)
		pygame.display.flip()
		











if __name__ == "__main__":
    main()

