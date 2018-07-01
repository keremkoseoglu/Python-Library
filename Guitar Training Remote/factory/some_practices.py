from factory import abstract_factory, all_practices
import random
from model import workout

class SomePractices(abstract_factory.AbstractFactory):

    _LOW_PERCENT = 50
    _HIGH_PERCENT = 80

    def get_workout(self) -> workout.WorkOut:
        output = all_practices.AllPractices().get_workout()
        remove_percent = random.randint(self._LOW_PERCENT, self._HIGH_PERCENT)
        output.remove_random_exercies(remove_percent)
        return output