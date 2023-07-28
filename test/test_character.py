from character import *


def test_something():
    assert True


def test_character_starts_with_1000_hp():
    character = Character()

    assert character.get_hp() == 1000


def test_character_starts_with_alive_state():
    character = Character()

    assert character.get_state() == ALIVE
