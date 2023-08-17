import os
import json
from pytest import fixture
import _pytest


this_folder = os.path.dirname(__file__)
data_path = os.path.join(this_folder, 'haystacks.json')


def load_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data


@fixture(params=load_data(data_path))
def haystack_fixture(request):
    yield request.param


###################################################################################


def pytest_addoption(parser):
    """
    This function is called, when `pytest` is run with an unknown option,
    e.g. `-j` or `--asdf`, but not `-x` (stop after first failure) or `--maxfail`.
    """
    parser.addoption(
        '--needle',
        action='store',
        help='needle to be searched in haystack'
    )


@fixture()
def needle_fixture(request):
    config = request.config
    assert isinstance(config, _pytest.config.Config)
    needle_string = config.getoption('--needle')

    if needle_string is not None:
        return int(needle_string)
    else:
        return 0
