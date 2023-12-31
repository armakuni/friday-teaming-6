import pytest

from character import *


@pytest.fixture
def alice():
    return Character()


def test_something():
    assert True


def test_character_starts_with_1000_hp(alice):
    assert alice.get_hp() == MAX_HP


def test_character_starts_with_alive_state(alice):
    assert alice.get_state() == ALIVE


def test_character_can_take_damage(alice):
    alice.take_damage(10)

    assert alice.get_hp() == 990


def test_character_dies_when_hp_is_0(alice):
    alice.take_damage(1000)

    assert alice.get_state() == DEAD


def test_character_can_heal(alice):
    alice.take_damage(100)
    alice.heal(10)

    assert alice.get_hp() == 910


def test_character_cannot_heal_after_dying(alice):
    alice.take_damage(1000)

    with pytest.raises(DeadCharacterCannotBeHealedException):
        alice.heal(10)


def test_characters_start_at_level_1(alice):
    assert alice.get_level() == 1


def test_characters_at_level_1_cannot_heal_above_1000(alice):
    alice.heal(100)
    assert alice.get_hp() == MAX_HP

    # cannot overheal
    alice.take_damage(100)
    alice.heal(200)

    assert alice.get_hp() == MAX_HP


def test_level_is_2_after_1000_damage(alice):
    def take_1000_damage_and_heal_fully():
        alice.take_damage(900)
        alice.heal(900)
        alice.take_damage(100)
        alice.heal(10000)

    for i in range(2, 3):
        take_1000_damage_and_heal_fully()
        assert alice.get_level() == i
