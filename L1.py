def add(x, y):
    return x + y


def test1():
    assert 2 == add(1, 1)


def test2():
    assert 1 != add(1, 1)
