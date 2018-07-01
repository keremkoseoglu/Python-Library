from model import exercise, exercise_step
from music_theory import chord, mode, position
from practice import abstract_practice

class Arpeggio(abstract_practice.AbstractPractice):

    _TITLE = "Arpeggio"
    _SUBTITLE = "Do an arpeggio on the given chord / mode"

    def get_exercise(self, quantity: int) -> exercise.Exercise:

        # ---Preparation-----

        random_steps = []
        position_obj = position.Position()

        # ---Build random list-----

        random_chords = chord.Chord().get_random_chords(quantity)
        quantity_left = quantity - len(random_chords)
        if quantity_left > 0:
            random_modes = mode.Mode().get_random_modes(quantity_left)

        random_stuff = []

        for i in range(len(random_chords)):
            random_stuff.append(random_chords[i])

        try:
            for i in range(len(random_modes)):
                random_stuff.append(random_modes[i])
        except:
            pass

        # ---Build return list-----

        for random_arp in random_stuff:
            suggested_position = position_obj.get_random_position()

            random_step = exercise_step.ExerciseStep(random_arp, "Suggested position: " + str(suggested_position))
            random_steps.append(random_step)

        output = exercise.Exercise(self._TITLE, self._SUBTITLE, random_steps)
        return output