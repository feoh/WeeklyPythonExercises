def threshold_equal(attr, threshold):
    def add_threshold_equal(klass):
        class DummyClass(klass):
            def __eq__(self, other):
                try:
                    apples = getattr(self, attr)
                    oranges = getattr(other, attr)
                except AttributeError:
                    return False

                return abs(apples - oranges) <= threshold
        return DummyClass

    return add_threshold_equal

