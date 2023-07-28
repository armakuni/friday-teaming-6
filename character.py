ALIVE = 1
DEAD = 2


class DeadCharacterCannotBeHealedException(Exception):
    pass


class Character:
    def __init__(self) -> None:
        self.hp = 1000

    def get_hp(self):
        return self.hp

    def get_state(self):
        return DEAD if self.hp <= 0 else ALIVE

    def take_damage(self, damage_amount):
        self.hp -= damage_amount

    def heal(self, heal_amount):
        if self.get_state() == DEAD:
            raise DeadCharacterCannotBeHealedException()
        self.hp += heal_amount
