from proj.duckburg.character_examples import scrooge_mcduck, gladstone_gander, gyro_gearloose


def test_matching_initials(duckburg):
    x = duckburg
    if x != scrooge_mcduck:
        assert x.first_name[0] == x.last_name[0]


def test_matching_name_and_species(duckburg):
    x = duckburg
    if x not in [scrooge_mcduck, gladstone_gander, gyro_gearloose]:
        assert x.last_name == x.species
