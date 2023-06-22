from dino_runner.utils.constants import HEART, JUMP_TYPE
from dino_runner.components.powerups.power_up import PowerUp


class JumpLife(PowerUp):
    def __init__(self):
        self.image = HEART
        self.type = JUMP_TYPE
        super().__init__(self.image, self.type)