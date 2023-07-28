ALIVE = 1
DEAD = 2

MAX_HP = 1000


class DeadCharacterCannotBeHealedException(Exception):
    pass


class Character:
    def __init__(self) -> None:
        self.hp = MAX_HP
        self.lifetime_damage_amount = 0

    def get_hp(self):
        return self.hp

    def get_state(self):
        return DEAD if self.hp <= 0 else ALIVE

    def take_damage(self, damage_amount):
        self.lifetime_damage_amount += damage_amount
        self.hp -= damage_amount

    def heal(self, heal_amount):
        if self.get_state() == DEAD:
            raise DeadCharacterCannotBeHealedException()

        self.hp += heal_amount
        self.hp = min(self.hp, 1000)

    def get_level(self):
        return int(self.lifetime_damage_amount / 1000) + 1
        if self.lifetime_damage_amount >= 2000:
            return 3
        if self.lifetime_damage_amount >= 1000:
            return 2

        return 1
