import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS, SHOT_SPEED


class Shot(CircleShape):
    def __init__(self, x: int, y: int, velocity: pygame.Vector2):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity.normalize() * SHOT_SPEED
        self.age = 0

    def update(self, dt):
        self.position += self.velocity * dt
        self.age += dt

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)
