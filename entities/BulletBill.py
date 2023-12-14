from classes.Animation import Animation
from entities.EntityBase import EntityBase
from traits.leftrightwalk import LeftRightWalkTrait
from classes.Collider import Collider
from classes.EntityCollider import EntityCollider

import pygame

# TODO: Add Animaiton exploding


class BulletBill(EntityBase):
    def __init__(self, screen, spriteColl, x, y, level, sound, dir):
        super(BulletBill, self).__init__(y, x - 1, 0)  # last num is gravity
        self.spriteCollection = spriteColl
        self.screen = screen
        self.leftrightTrait = LeftRightWalkTrait(self, level)
        self.leftrightTrait.direction = dir
        self.leftrightTrait.speed = 3.5
        self.type = "Mob"
        self.dashboard = level.dashboard
        self.collision = Collider(self, level)
        self.EntityCollider = EntityCollider(self)
        self.levelObj = level
        self.sound = sound
        self.animation = Animation(
            [
                self.spriteCollection.get("bill").image,
            ]
        )
        self.lives = 1
        self.direction = dir

    def update(self, camera):
        if self.alive:
            # self.applyGravity()
            self.drawBulletBill(camera)
            self.leftrightTrait.update()
            if self.lives <= 0:
                self.alive = 0
            self.checkEntityCollision(camera)
        else:
            self.alive = None

    def drawBulletBill(self, camera):
        if self.direction == -1:
            self.screen.blit(
                self.animation.image, (self.rect.x + camera.x, self.rect.y)
            )
        else:
            self.screen.blit(
                pygame.transform.flip(self.animation.image, True, False),
                (self.rect.x + camera.x, self.rect.y),
            )
        self.animation.update()

    def checkEntityCollision(self, camera):
        pass
