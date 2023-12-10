from entities.EntityBase import EntityBase
from entities.FireBall import FireBall


class BillShooter(EntityBase):
    def __init__(self, screen, spriteCollection, x, y, sound, dashboard, gravity=0):
        super(BillShooter, self).__init__(x, y, gravity)
        self.screen = screen
        self.spriteCollection = spriteCollection
        self.type = "Block"
        self.triggered = False
        self.time = 0
        self.maxTime = 10
        self.sound = sound
        self.dashboard = dashboard
        self.vel = 1
        self.direction = 1
        self.fireBall = FireBall(spriteCollection, screen, x-1, y)
        self.x = x
        self.y = y
        

    def update(self):
        
        pass
