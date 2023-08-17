# examples PyTest


``` 
python -m pytest
python -m pytest -v

python -m pytest proj/parametrize -v -m "not bad"

python -m pytest proj/duckburg -v -m "not trivial"
python -m pytest proj/duckburg -v -k "test_matching_initials"
```

(The plain `pytest` command would require more `__init__.py` files, e.g. in [proj](proj) and [proj/duckburg](proj/duckburg).)


Running all tests, rather than those in a folder, will raise warnings for markers defined only in folders.<br>E.g. in [duckburg/pytest.ini](proj/duckburg/pytest.ini) and [marks/pytest.ini](proj/marks/pytest.ini).
