'''
This is the file responsible of data access.
We would normally access a database here.
However, we will use simple Text files for the sake of simplicity.
'''

from data.person import Person

class DataManager:

    _DATA_FILE_PATH = "/Users/kerem/Dropbox/Software/Kerem/Development/Python Library/snippets/Flask Tutor/data/data_file.csv"
    _FILE_DELIMINATOR = ";"
    _USERNAME = "me"
    _PASSWORD = "me"

    def __init__(self):
        pass

    def add_person(self, person: Person):
        file = open(self._DATA_FILE_PATH, "a")
        file.write("\r\n" + person.get_name() + self._FILE_DELIMINATOR + person.get_surname() + self._FILE_DELIMINATOR + str(person.get_year()))
        file.close()

    def get_people(self) -> []:
        output = []

        file = open(self._DATA_FILE_PATH, "r")
        line = file.readline()
        while line:
            line_values = line.split(self._FILE_DELIMINATOR)
            if len(line_values) != 4:
                continue
            person = Person()
            person.set_id(line_values[0])
            person.set_name(line_values[1])
            person.set_surname(line_values[2])
            person.set_year(line_values[3])
            output.append(person)
            line = file.readline()
        file.close()

        return output

    def get_people_as_dict(self) -> {}:
        people = self.get_people()

        output = {}
        for person in people:
            key = person.get_id()
            val = {"name":person.get_name(), "surname":person.get_surname(), "year": str(person.get_year()).replace("\n", "")}
            output[key] = val
        return output

    def get_person(self, person_id: int) -> Person:
        people = self.get_people()
        for i in range(len(people)):
            if people[i].get_id() == person_id:
                return people[i]

    def login(self, username: str, password: str):
        if not (username == self._USERNAME and password == self._PASSWORD):
            raise ValueError("Invalid user or password")
