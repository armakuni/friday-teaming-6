from character import *
import pytest


def test_something():
    assert True


def test_character_starts_with_1000_hp():
    character = Character()

    assert character.get_hp() == 1000


def test_character_starts_with_alive_state():
    character = Character()

    assert character.get_state() == ALIVE


def test_character_can_take_damage():
    character = Character()

    character.take_damage(10)
