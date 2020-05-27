from random import randint



class RandMemory(object):

    def __init__(self, min_random_number, max_random_number):
        self._history = []
        self.lowest = min_random_number
        self.highest = max_random_number

    @property
    def get(self):
        rint=randint(self.lowest, self.highest)
        self._history.append(rint)
        return rint

    def history(self):
        return self._history

