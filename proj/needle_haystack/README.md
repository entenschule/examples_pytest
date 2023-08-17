# flag needle and JSON haystack


The list of haystacks in defined in [haystacks.json](haystacks.json).<br>

In [conftest.py](conftest.py) the _haystack_ and _needle_ fixtures are defined.<br>
The former passes along the data from JSON.<br>
The latter passes along the argument from the `--needle` flag.

Only the needles 0 and 6 will be found in all haystacks.<br>
If the flag is not used, `needle_fixture` will return 0 as default.

```
python -m pytest proj/needle_haystack                # pass (default needle 0)
python -m pytest proj/needle_haystack --needle 3     # fail
python -m pytest proj/needle_haystack --needle 6     # pass

python -m pytest proj/needle_haystack --needle       # error (missing argument)
python -m pytest proj/needle_haystack --needle abc   # ValueError (not numeric)
```
