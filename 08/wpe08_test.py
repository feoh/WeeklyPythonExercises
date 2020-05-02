from solution import multiziperator


def test_returns_iterator():
    m = multiziperator('abc', 'def')
    assert m == iter(m)


def test_simple():
    m = multiziperator('abc', 'def')
    assert list(m) == list('adbecf')


def test_not_same_length():
    m = multiziperator('abc', 'de')
    assert list(m) == list('adbe')
