from classes.Animation import Animation
from classes.Maths import Vec2D
from entities.EntityBase import EntityBase
from traits.leftrightwalk import LeftRightWalkTrait
from classes.Collider import Collider
from classes.EntityCollider import EntityCollider
from classes.Sprites import Sprites

spriteCollection = Sprites().spriteCollection
throwAnimation = Animation(
    [
        spriteCollection["fireBall_1"].image,
        spriteCollection["fireBall_2"].image,
        spriteCollection["fireBall_3"].image,
        spriteCollection["fireBall_4"].image,
    ],
)
#TODO: Add Animaiton exploding
explodeAnimation = Animation(
    [
        spriteCollection["mario_big_run1"].image,
        spriteCollection["mario_big_run2"].image,
        spriteCollection["mario_big_run3"].image,
    ],
)



class FireBall(EntityBase):
    def __init__(self, screen, spriteColl, x, y, level, sound):
        super(FireBall, self).__init__(y, x - 1, 1.25)
        self.spriteCollection = spriteColl
        self.screen = screen
        self.leftrightTrait = LeftRightWalkTrait(self, level)
        self.type = "Projectile"
        self.dashboard = level.dashboard
        self.collision = Collider(self, level)
        self.EntityCollider = EntityCollider(self)
        self.levelObj = level
        self.sound = sound
        self.animation = throwAnimation

    def update(self, camera):
        if self.alive:
            self.applyGravity()
            self.drawFireBall(camera)
            self.leftrightTrait.update()
            self.checkEntityCollision()
        else:
            self.onDead(camera)

    def drawFireBall(self, camera):
        self.entity.scaleRect(0.5)
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
        self.dashboard.drawText("100", self.textPos.x + camera.x, self.textPos.y, 8)

    def checkEntityCollision(self):
        pass
