class Person:

    def __init__(self):
        self._id = 0
        self._name = ""
        self._surname = ""
        self._year = 0

    def get_id(self) -> int:
        return self._id

    def get_year(self) -> int:
        return self._year

    def get_name(self) -> str:
        return self._name

    def get_surname(self) -> str:
        return self._surname

    def set_id(self, id: int):
        self._id = int(id)

    def set_year(self, year: int):
        self._year = year

    def set_name(self, name: str):
        self._name = name

    def set_surname(self, surname: str):
        self._surname = surname

