import random
from music_theory.note import Note


class Mode:

    def __init__(self):
        self._modes = ["Ionian", "Dorian", "Phrygian", "Lydian", "Mixolydian", "Aeolian", "Locrian"]

    def get_random_mode_type(self) -> str:
        i = random.randint(0, len(self._modes) - 1)
        return self._modes[i]

    def get_random_modes(self, count: int) -> []:

        output = []
        note_obj = Note()

        for c in range(count):
            random_note = note_obj.get_random_note()
            random_mode = self.get_random_mode_type()
            random_result = random_note + " " + random_mode
            output.append(random_result)

        return output
