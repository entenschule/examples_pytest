# duckburg

In [conftest.py](conftest.py) the fixture `duckburg` is defined.<br>
It yields the elements of a list of characters:

```python
@fixture(params=list_of_duckburg_characters, ids=lambda x: f'{x.first_name} {x.last_name}')
def duckburg(request):
    yield request.param
```


It can be used by all tests within this folder,
e.g. in [nested/test_duckburg_nested.py](nested/test_duckburg_nested.py):

```python
def test_trivial(duckburg):
    x = duckburg
    assert len(x.first_name) > 1
```

The interesting tests are in [test_duckburg.py](test_duckburg.py).


```
python -m pytest proj/duckburg -v -m "not trivial"
python -m pytest proj/duckburg -v -k "test_matching_initials or test_matching_name_and_species"
```

For some characters the tests are skipped:

```
python -m pytest proj/duckburg/test_duckburg.py::test_matching_initials -v
python -m pytest proj/duckburg -k "test_matching_initials" -v
```

```
proj/duckburg/test_duckburg.py::test_matching_initials[Donald Duck] PASSED                                    [ 20%]
proj/duckburg/test_duckburg.py::test_matching_initials[Daisy Duck] PASSED                                     [ 40%]
proj/duckburg/test_duckburg.py::test_matching_initials[Scrooge McDuck] SKIPPED (exception from the rule)      [ 60%]
proj/duckburg/test_duckburg.py::test_matching_initials[Gladstone Gander] PASSED                               [ 80%]
proj/duckburg/test_duckburg.py::test_matching_initials[Gyro Gearloose] PASSED                                 [100%]

==================================== 4 passed, 1 skipped, 10 deselected in 0.01s ====================================
```
