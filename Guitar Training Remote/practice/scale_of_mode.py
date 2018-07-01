from model import exercise, exercise_step
from music_theory import mode
from practice import abstract_practice


class ScaleOfMode(abstract_practice.AbstractPractice):

    _TITLE = "Scale of mode"
    _SUBTITLE = "Play a scale of mode"

    def get_exercise(self, quantity: int) -> exercise.Exercise:
        random_steps = []

        random_modes = mode.Mode().get_random_modes(quantity)

        for random_mode in random_modes:
            random_step = exercise_step.ExerciseStep(random_mode,
                                                     super(ScaleOfMode, self).get_random_position_suggestion_text())
            random_steps.append(random_step)

        output = exercise.Exercise(self._TITLE, self._SUBTITLE, random_steps)
        return output
