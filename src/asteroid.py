import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: int):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        rand_angle = random.uniform(20, 50)
        velocities = [
            self.velocity.rotate(rand_angle),
            self.velocity.rotate(-rand_angle),
        ]
        radius = self.radius - ASTEROID_MIN_RADIUS
        for velocity in velocities:
            asteroid = Asteroid(self.position.x, self.position.y, radius)
            asteroid.velocity = velocity * 1.2
