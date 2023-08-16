from pytest import fixture

from proj.duckburg.character_examples import donald, daisy, scrooge, gladstone, gyro


list_of_duckburg_characters = [donald, daisy, scrooge, gladstone, gyro]


@fixture(params=list_of_duckburg_characters, ids=lambda x: x.first_name)
def duckburg(request):
    yield request.param
