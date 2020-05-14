from collections import namedtuple, defaultdict

Person = namedtuple('Person', 'first last')


class GuestList:
    max_at_table = 10

    def __init__(self):
        self.tables = defaultdict(list)

    def assign(self, person: Person, table_number):
        if len(self.tables[table_number]) >= self.max_at_table:
            raise TableFull("Max per table exceeded!")

        for _, guests in self.tables.items():
            if person in guests:
                guests.remove(person)
                break

        self.tables[table_number].append(person)

    def unassigned(self):
        if len(self.tables):
            return self.tables[None]

    def table(self, table: int):
        if len(self.tables):
            return self.tables[table]

    def __len__(self):
        return sum([len(table) for table in self.tables.values()])

    def free_space(self):
        # return {table: 10 - len(self.table(table)) for table in self.tables.keys()}
        free_space_dict = {}
        for table in self.tables.keys():
            space = 10 - len(self.table(table))
            print(f"table: {table} space: {space}")
            free_space_dict[table] = space

        return free_space_dict

    def guests(self):
        guests = []
        for table in self.tables.keys():
            guests.extend(self.table(table))
        return guests

    def __repr__(self):
        out = ""
        for table in self.tables.keys():
            out = f"{table}\n"
            for person in self.table(table):
                out = out + f"\t{person.last}, {person.first}\n"
        return out


class TableFull(Exception):
    def __init__(self, message):
        pass
