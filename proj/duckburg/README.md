# duckburg

In [conftest.py](conftest.py) the fixture `duckburg` is defined.<br>
It yields the elements of a list of characters:

```python
@fixture(params=list_of_duckburg_characters, ids=lambda x: x.first_name)
def duckburg(request):
    yield request.param
```


It can be used by all tests within this folder.<br>
E.g. [test_duckburg.py](test_duckburg.py),
but also in [nested/test_duckburg_nested.py](nested/test_duckburg_nested.py):

```python
def test_trivial(duckburg):
    x = duckburg
    assert len(x.first_name) > 1
```
