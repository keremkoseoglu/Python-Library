import random
from music_theory.note import Note

class Chord:

    def __init__(self):
        self._chord_types = ["", "7", "∆7", "9", "#11", "13", "sus4", "-", "-7", "-9", "-b9", "-11", "-13", "-b13", "Ø"]

    def get_random_chord_type(self) -> str:
        i = random.randint(0, len(self._chord_types) - 1)
        return self._chord_types[i]

    def get_random_chords(self, count: int) -> []:

        output = []
        note_obj = Note()

        for c in range(count):
            random_note = note_obj.get_random_note()
            random_chord_type = self.get_random_chord_type()
            random_result = random_note + random_chord_type
            output.append(random_result)

        return output