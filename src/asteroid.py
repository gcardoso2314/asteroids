import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: int):
        super().__init__(x, y, radius)
        self.point_vectors = [
            pygame.Vector2(0, self.radius * random.uniform(0.7, 1)).rotate(i)
            for i in range(0, 360, 45)
        ]

    def draw(self, screen):
        pygame.draw.polygon(
            screen,
            (255, 255, 255),
            [self.position + v for v in self.point_vectors],
            2,
        )

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
