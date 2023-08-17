import pytest
import inspect


def gsl(expr):
    sl = inspect.getsourcelines(expr)
    sl00 = sl[0][0]
    return sl00.strip()


expressions = [
    lambda: 1 / 0,
    lambda: 0 / 0
]


@pytest.mark.parametrize('expr', expressions, ids=gsl)
def test_zero_division(expr):
    with pytest.raises(ZeroDivisionError):
        expr()


expressions = [
    lambda: 0 / 1,
    lambda: 1 / 1,
]


@pytest.mark.bad
@pytest.mark.parametrize('expr', expressions, ids=gsl)
def test_zero_division_bad(expr):
    with pytest.raises(ZeroDivisionError):
        expr()
