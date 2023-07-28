import pytest

from character import *


@pytest.fixture
def alice():
    return Character()


def test_something():
    assert True


def test_character_starts_with_1000_hp(alice):
    assert alice.get_hp() == 1000


def test_character_starts_with_alive_state(alice):
    assert alice.get_state() == ALIVE


def test_character_can_take_damage(alice):
    alice.take_damage(10)

    assert alice.get_hp() == 990


def test_character_dies_when_hp_is_0(alice):
    alice.take_damage(1000)
