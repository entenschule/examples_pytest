from pytest import fixture

from proj.duckburg.character_examples import donald_duck, daisy_duck, scrooge_mcduck, gladstone_gander, gyro_gearloose


list_of_duckburg_characters = [donald_duck, daisy_duck, scrooge_mcduck, gladstone_gander, gyro_gearloose]


@fixture(params=list_of_duckburg_characters, ids=lambda x: x.first_name)
def duckburg(request):
    yield request.param
