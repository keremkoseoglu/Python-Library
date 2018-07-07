from model import exercise, exercise_step
from music_theory import chord, mode, position
from practice import abstract_practice
import random

class TritoneSub(abstract_practice.AbstractPractice):

    _TITLE = "Tritone Substitution"
    _SUBTITLE = "Do chords, walking bass and improv"

    def get_exercise(self, quantity: int) -> exercise.Exercise:
        random_steps = []

        for i in range(quantity):

            # Get chords
            number_of_chords = random.randint(1, 3)
            chords = chord.Chord().get_random_chords(number_of_chords)

            # Build chord text
            chord_txt = ""
            sub_txt = ""
            for ch in chords:
                if chord_txt == "":
                    chord_txt = ch
                else:
                    if sub_txt == "":
                        sub_txt = "followed by: "
                    else:
                        sub_txt += " | "
                    sub_txt += ch

            # Add to steps
            random_step = exercise_step.ExerciseStep(chord_txt, sub_txt)
            random_steps.append(random_step)

        output = exercise.Exercise(self._TITLE, self._SUBTITLE, random_steps)
        return output
