from entities.EntityBase import EntityBase


class BillShooter(EntityBase):
    def __init__(
        self, screen, spriteCollection, x, y, sound, dashboard, level, gravity=0
    ):
        super(BillShooter, self).__init__(x, y, gravity)
        self.screen = screen
        self.spriteCollection = spriteCollection
        self.type = "Block"
        self.triggered = False
        self.time = 0
        self.maxTime = 120
        self.sound = sound
        self.dashboard = dashboard
        self.vel = 1
        self.direction = -1
        self.x = x
        self.y = y
        self.level = level
        self.alive = True

    def update(self, cam):
        self.time += 1
        if self.time == self.maxTime:
            self.time = 0
            if self.direction == 1:
                self.level.addBulletBill(self.y + 1, self.x + 1, self.direction)
            else:
                self.level.addBulletBill(self.y + 1, self.x - 1, self.direction)
