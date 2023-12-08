class throwFire:
    def __init__(self, entity, x, y):
        self.entity = entity
        self.x = x
        self.y = y

    def throw(self, throwing):
        if throwing:
            self.entity.levelObj.addFireFlower(self.x, self.y)
