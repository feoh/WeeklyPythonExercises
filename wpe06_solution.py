#!/usr/bin/env python

from collections import Counter

all_people = [{'name': 'Chris', 'age': 51, 'hobbies': ['Python', 'Freemasonry', 'reading']},
              {'name': 'Michelle', 'age': 49, 'hobbies': ['TV', 'Puppies']},
              {'name': 'Jack', 'age': 45, 'hobbies': ['Python', 'Bowling', 'Snark', 'reading']}]


def all_hobbies(people):
    hobbies = set()
    for person in people:
        hobbies.update(person['hobbies'])
    return hobbies


def average_age_under(people, maxage):
    people_below_max_age = [person for person in people if person['age'] < maxage]
    if not people_below_max_age:
        return 0
    total_age_of_people = sum([person['age'] for person in people_below_max_age])
    return total_age_of_people / len(people_below_max_age)


def hobby_counter(people):
    hobbies_count = Counter()
    [hobbies_count.update(person['hobbies']) for person in people]
    return hobbies_count


def n_most_common(people, n):
    hc = hobby_counter(people)
    mc = hc.most_common(n)
    most_common_hobbies = [hobby for hobby, count in mc]
    return most_common_hobbies
