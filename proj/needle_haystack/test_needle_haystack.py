def test_needle_haystack(needle_fixture, haystack_fixture):
    needle = needle_fixture
    haystack = haystack_fixture
    assert needle in haystack
