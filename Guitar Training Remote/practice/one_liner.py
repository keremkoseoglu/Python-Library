from model import exercise, exercise_step
from practice.abstract_practice import AbstractPractice
import random


class OneLiner(AbstractPractice):

    _ONE_LINERS = [
        "Old licks",
        "Circle of 5ths",
        "New lick",
        "Groove loop",
        "Repertoire"
    ]

    _TITLE = "One-Liner"
    _SUBTITLE = "Go over the one-liners"

    def _clone_one_liners(self) -> []:
        output = []

        for i in range(0, len(self._ONE_LINERS)):
            output.append(self._ONE_LINERS[i])

        return output

    def get_exercise(self, quantity: int) -> exercise.Exercise:

        random_steps = []
        one_liners = []

        for i in range(0, quantity):
            if len(one_liners) == 0:
                one_liners = self._clone_one_liners()
            random_index = random.randint(0, len(one_liners) - 1)
            random_one_liner = one_liners.pop(random_index)
            random_step = exercise_step.ExerciseStep(random_one_liner, "")
            random_steps.append(random_step)

        output = exercise.Exercise(self._TITLE, self._SUBTITLE, random_steps)
        return output