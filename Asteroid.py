
import random
import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event













class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
        #self.y += CircleShape.velocity.y * dt  # Example movement

    def split(self):
        # Logic to split the asteroid into smaller pieces
        self.kill()  # Remove the original asteroid
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            
            velocity1 = self.velocity.rotate(random_angle)
            velocity2 = self.velocity.rotate(-random_angle)

            velocity1 = velocity1 * 1.2
            velocity2 = velocity2 * 1.2
            
            self.radius -= ASTEROID_MIN_RADIUS

            asteroid = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid.velocity = velocity1
            asteroid = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid.velocity = velocity2
