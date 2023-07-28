ALIVE = 1
DEAD = 2


class Character:
    def __init__(self) -> None:
        self.hp = 1000

    def get_hp(self):
        return self.hp

    def get_state(self):
        if self.hp <= 0:
            return DEAD

        return ALIVE

    def take_damage(self, damage_amount):
        self.hp -= damage_amount
