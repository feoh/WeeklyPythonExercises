#!/usr/bin/env python3

import wpe06_solution
import pytest
from collections import Counter

all_people = [{'name':'Reuven', 'age':48, 'hobbies':['Python', 'cooking', 'reading']},
              {'name':'Atara', 'age':17, 'hobbies':['horses', 'cooking', 'art', 'reading']},
              {'name':'Shikma', 'age':15, 'hobbies':['Python', 'piano', 'cooking', 'reading']},
              {'name':'Amotz', 'age':13, 'hobbies':['biking', 'cooking']}]

@pytest.mark.parametrize('people, maxage, output', [
    ({}, 120, 0),
    (all_people, 120, 23.25),
    (all_people, 25, 15),
    (all_people, -1, 0)
])
def test_average_age_under(people, maxage, output):
    assert wpe06_solution.average_age_under(people, maxage) == output

@pytest.mark.parametrize('people, output', [
    ({}, set()),
    (all_people, {'Python', 'cooking', 'reading', 'horses', 'art', 'piano', 'cooking', 'biking'})
])
def test_all_hobbies(people, output):
    assert wpe06_solution.all_hobbies(people) == output

@pytest.mark.parametrize('people, output', [
    ({}, Counter()),
    (all_people, Counter({'Python':2, 'biking':1, 'cooking':4, 'art': 1, 'horses': 1, 'piano': 1, 'reading': 3}))
])
def test_hobby_counter(people, output):
    assert wpe06_solution.hobby_counter(people) == output

@pytest.mark.parametrize('people, n, output', [
    ({}, 3, []),
    (all_people, 3, ['Python', 'reading', 'cooking'])
])
def test_n_most_common(people, n, output):
    assert sorted(wpe06_solution.n_most_common(people, 3)) == sorted(output)