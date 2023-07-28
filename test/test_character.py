from character import Character


def test_something():
    assert True


def test_character_starts_with_1000_hp():
    character = Character()

    assert character.get_hp() == 1000
