from classes.Animation import Animation
from classes.Maths import Vec2D
from entities.EntityBase import EntityBase
from traits.leftrightwalk import LeftRightWalkTrait
from classes.Collider import Collider
from classes.EntityCollider import EntityCollider
from classes.Sprites import Sprites
from traits.bounce import bounceTrait

spriteCollection = Sprites().spriteCollection
throwAnimation = Animation(
    [
        spriteCollection["fireBall_1"].image,
        spriteCollection["fireBall_2"].image,
        spriteCollection["fireBall_3"].image,
        spriteCollection["fireBall_4"].image,
    ],
)
# TODO: Add Animaiton exploding

class FireBall(EntityBase):
    def __init__(self, screen, spriteColl, x, y, level, sound, dir):
        super(FireBall, self).__init__(y, x - 1, 0.5)  # last num is gravity
        self.rect.width = 16
        self.rect.height = 16
        self.spriteCollection = spriteColl
        self.screen = screen
        self.leftrightTrait = LeftRightWalkTrait(self, level)
        self.leftrightTrait.direction = dir
        self.leftrightTrait.speed = 5
        self.bounceTrait = bounceTrait(self, 6)
        self.type = "Projectile"
        self.dashboard = level.dashboard
        self.collision = Collider(self, level)
        self.EntityCollider = EntityCollider(self)
        self.levelObj = level
        self.sound = sound
        self.animation = throwAnimation
        self.lives = 5
        self.direction = dir

    def update(self, camera):
        if self.alive:
            self.applyGravity()
            self.drawFireBall(camera)
            self.leftrightTrait.update()
            if self.onGround:
                self.bounceTrait.jump = 1
                self.lives -= 1
            if(self.lives <= 0):
                self.alive = 0
            if self.direction != self.leftrightTrait.direction:
                self.lives -= 1
            self.direction = self.leftrightTrait.direction
            self.bounceTrait.update()
            self.checkEntityCollision()
        else:
            self.onDead(camera)

    def drawFireBall(self, camera):
        self.screen.blit(self.animation.image, (self.rect.x + camera.x, self.rect.y))
        self.animation.update()

    def onDead(self, camera):
        if self.timer == 0:
            self.setPointsTextStartPosition(self.rect.x + 3, self.rect.y)
        if self.timer < self.timeAfterDeath:
            self.movePointsTextUpAndDraw(camera)
        else:
            self.alive = None
        self.timer += 0.1

    def setPointsTextStartPosition(self, x, y):
        self.textPos = Vec2D(x, y)

    def movePointsTextUpAndDraw(self, camera):
        self.textPos.y += -0.5
        self.dashboard.drawText("", self.textPos.x + camera.x, self.textPos.y, 8)

    def checkEntityCollision(self):
        for ent in self.levelObj.entityList:
            collisionState = self.EntityCollider.check(ent)
            if collisionState.isColliding:
                if ent.__class__.__name__ == "Goomba":
                    ent.alive = False
                    self.alive = False
                if ent.__class__.__name__ == "Koopa":
                    if not ent.active:
                        ent.alive = None
                    else:
                        ent.timer = 0
                        ent.leftrightTrait.speed = 1
                        ent.alive = True
                        ent.active = False
                    self.alive = 0
        pass
