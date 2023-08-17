from pytest import mark


@mark.foo
def test_foo():
    pass


@mark.foo
@mark.bar
def test_foobar():
    pass


@mark.bar
def test_bar():
    pass


def test_other():
    pass
