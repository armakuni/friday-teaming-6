ALIVE = 1
DEAD = 2


class Character:
    def __init__(self) -> None:
        self.hp = 1000
        self.state = ALIVE

    def get_hp(self):
        return self.hp

    def get_state(self):
        return self.state

    def take_damage(self, damage_amount):
        self.hp -= damage_amount

        if self.hp <= 0:
            self.state = DEAD
