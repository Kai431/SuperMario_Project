import random

from classes.Collider import Collider


class StandTrait:
    def __init__(self, entity, level):
        self.direction = random.choice([-1, 1])
        self.entity = entity
        self.collDetection = Collider(self.entity, level)
        self.speed = 0
        self.entity.vel.x = self.speed * self.direction

    def update(self):
        self.entity.rect.y += self.entity.vel.y
        self.collDetection.checkY()
        self.entity.rect.x += self.entity.vel.x
        self.collDetection.checkX()
