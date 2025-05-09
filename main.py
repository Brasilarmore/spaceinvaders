import pygame
from constants import *
from player import Player
from asteroidfield import *

def main():
    pygame.init()
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    AsteroidField.containers = (updatable_group,)
    Asteroid.containers = (updatable_group, drawable_group, asteroid_group)
    Player.containers = (updatable_group, drawable_group)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots_group)
    asteroidfield = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = (clock.tick(60) / 1000)
        updatable_group.update(dt)
        shots_group.update(dt)
        #check for collisions between asteroid and player
        for asteroid in asteroid_group:
            if asteroid.collision(player):
                print("Game over!")
                import sys
                sys.exit()
 
        screen.fill("black")
        for thing in drawable_group:
            thing.draw(screen)
        for shot in shots_group:
            shot.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
