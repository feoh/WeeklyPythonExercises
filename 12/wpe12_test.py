#!/usr/bin/env python3

from solution import RandMemory

def test_empty():
    r = RandMemory(1, 100)
    assert r.lowest == 1
    assert r.highest == 100
    assert r._history == []
    assert r.history() == []

def test_types():
    r = RandMemory(1, 100)
    assert type(r.get) == int

def test_three():
    r = RandMemory(1, 100)
    old_numbers = [ ]
    for i in range(3):
        old_numbers.append(r.get)
    assert r.history() == old_numbers