from pytest import mark


@mark.parametrize('tv', [
    ('Samsung', '123'),
    ('Sony', 'ASDF'),
    ('LG', 'OMG-2000')
], ids=lambda x: x[0])
def test_television_turns_on(tv):
    brand, model = tv
    print(f'######################## {brand} {model} turns on.')
