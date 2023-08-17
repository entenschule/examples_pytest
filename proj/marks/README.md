# marks


```
python -m pytest proj/marks -m foo -v
python -m pytest proj/marks -m bar -v

python -m pytest proj/marks -m "foo and bar" -v
python -m pytest proj/marks -m "foo or bar" -v

python -m pytest proj/marks -m "foo and not bar" -v
python -m pytest proj/marks -m "not bar" -v
python -m pytest proj/marks -m "not (foo or bar)" -v
```