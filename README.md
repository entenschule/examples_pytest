# examples PyTest


``` 
python -m pytest
python -m pytest -v

python -m pytest proj/parametrize -v -m "not bad"

python -m pytest proj/duckburg -v -m "not trivial"
python -m pytest proj/duckburg -v -k "test_matching_initials"
```

(The plain `pytest` command would require more `__init__.py` files, e.g. in [proj](proj) and [proj/duckburg](proj/duckburg).)
