from collections import Counter, defaultdict

visits = defaultdict(Counter)

def collect_places():
    visits.clear()
    while True:
        city_country = input("Tell me where you went: ")
        if not city_country:
            break
        try:
            (city, country) = city_country.split(', ')
        except ValueError:
            print("That's not a legal city, country combination")
            continue
        visits[country][city] += 1

def display_places():
    print("You visited:")
    for country in sorted(visits.keys()):
        print(f"{country}:")
        for city in sorted(visits[country]):
            print(f"\t{city} ({visits[country][city]})")


if __name__ == "__main__":
    collect_places()
    display_places()
