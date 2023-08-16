from proj.duckburg.character_examples import scrooge, gladstone, gyro


def test_matching_initials(duckburg):
    x = duckburg
    if x != scrooge:
        assert x.first_name[0] == x.last_name[0]


def test_matching_name_and_species(duckburg):
    x = duckburg
    if x not in [scrooge, gladstone, gyro]:
        assert x.last_name == x.species
