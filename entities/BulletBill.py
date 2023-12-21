from classes.Animation import Animation
from entities.EntityBase import EntityBase
from traits.leftrightwalk import LeftRightWalkTrait
from classes.Collider import Collider
from classes.EntityCollider import EntityCollider
from classes.Maths import Vec2D
from copy import copy
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

    def update(self, camera):
        if self.alive:
            self.drawBulletBill(camera)
            self.leftrightTrait.update()
            if self.lives <= 0:
                self.alive = 0
            self.checkEntityCollision(camera)
        else:
            self.onDead(camera)

    def onDead(self, camera):
        if self.timer == 0:
            self.animation = copy(self.spriteCollection.get("explosion_big").animation)
            self.dashboard.points += 200
            self.setPointsTextStartPosition(self.rect.x + 3, self.rect.y)
        if self.timer < self.timeAfterDeath:
            self.animation.update()
            self.movePointsTextUpAndDraw(camera)
            self.screen.blit(
                self.animation.image,
                (self.rect.x + camera.x, self.rect.y),
            )
        else:
            self.alive = None
        self.timer += 0.1

    def drawBulletBill(self, camera):
        if self.leftrightTrait.direction == -1:
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

    def setPointsTextStartPosition(self, x, y):
        self.textPos = Vec2D(x, y)

    def movePointsTextUpAndDraw(self, camera):
        self.textPos.y += -0.5
        self.dashboard.drawText("200", self.textPos.x + camera.x, self.textPos.y, 8)
