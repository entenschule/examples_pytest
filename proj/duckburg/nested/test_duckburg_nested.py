import pytest


@pytest.mark.trivial
def test_trivial(duckburg):
    x = duckburg
    assert len(x.first_name) > 1
