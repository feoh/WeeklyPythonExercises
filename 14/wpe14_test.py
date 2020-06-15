from solution import threshold_equal


def test_self():
    @threshold_equal('x', 0)
    class MyClass:
        def __init__(self, x):
            self.x = x

    m1 = MyClass(10)
    assert m1 == m1


def test_two_equal():
    @threshold_equal('x', 0)
    class MyClass:
        def __init__(self, x):
            self.x = x

    m1 = MyClass(10)
    m2 = MyClass(10)
    assert m1 == m2


def test_two_close():
    @threshold_equal('x', 2)
    class MyClass:
        def __init__(self, x):
            self.x = x

    m1 = MyClass(10)
    m2 = MyClass(12)
    assert m1 == m2
    assert m2 == m1


def test_two_unequal():
    @threshold_equal('x', 2)
    class MyClass:
        def __init__(self, x):
            self.x = x

    m1 = MyClass(10)
    m2 = MyClass(20)
    assert m1 != m2


def test_wrong_type():
    @threshold_equal('x', 2)
    class MyClass:
        def __init__(self, x):
            self.x = x

    m1 = MyClass(10)
    assert m1 != False
    assert m1 != 5
    assert m1 != 'abcd'
    assert False != m1
    assert 5 != m1
    assert 'abcd' != m1