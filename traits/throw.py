class throwFire:
    def __init__(self, entity):
        self.entity = entity
        
    def throw(self, throwing):
        if throwing:
            self.entity.levelObj.addFireBall(self.entity.getPosY() // 32, self.entity.getPosIndexAsFloat().x)