import random


class Degree:

    def __init__(self):
        self._degrees = [1, 2, 3, 4, 5, 6, 7, 9, 11, 13]

    def get_random_degree(self) -> int:
        i = random.randint(0, len(self._degrees) - 1)
        return self._degrees[i]

    def get_random_degrees(self, count: int) -> []:

        output = []

        for c in range(count):
            random_degree = self.get_random_degree()
            output.append(random_degree)

        return output