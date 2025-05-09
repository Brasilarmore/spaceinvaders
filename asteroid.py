import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
 
    def draw(self, screen):
        pygame.draw.circle(screen, "purple", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
         self.position += self.velocity * dt

class Shot(CircleShape):
    def __init__(self, position, velocity):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = velocity
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius)
