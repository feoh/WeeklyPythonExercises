from solution import ThresholdEqual

def test_same():
    te = ThresholdEqual(10)
    assert te == te
    assert te.threshold == 2

def test_different_far():
    te1 = ThresholdEqual(10)
    te2 = ThresholdEqual(13)
    assert te1 != te2
    assert not(te1 == te2)

def test_different_close():
    te1 = ThresholdEqual(10)
    te2 = ThresholdEqual(11)
    assert te1 == te2

def test_different_change_threshold():
    te1 = ThresholdEqual(10)
    te2 = ThresholdEqual(15)
    assert te1 != te2

    te1.threshold = 100
    assert te1 == te2
    assert te2 != te1

    te2.threshold = 100
    assert te1 == te2
    assert te2 == te1

def test_simple_int_stuff():
    te = ThresholdEqual(10)

    assert te + te == 20
    assert te - te == 0
    assert te * te == 100
    assert te / te == 1
    assert te % te == 0
    assert te ** te == 10000000000