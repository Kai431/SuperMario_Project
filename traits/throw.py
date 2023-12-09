class throwFire:
    def __init__(self, entity):
        self.entity = entity

    def throw(self, throwing):
        if throwing and self.entity.powerUpState == 2:
            heading = self.entity.traits["goTrait"].heading
            self.entity.inThrow = True
            if heading == 1:
                addX = 32
            else:
                addX = 0

            self.entity.levelObj.addFireBall(
                (self.entity.getPosY() + 64) // 32,
                self.entity.getPosIndexAsFloat().x + addX // 32,
                heading,
            )
