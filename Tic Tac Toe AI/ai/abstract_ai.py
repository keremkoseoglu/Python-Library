from abc import ABC, abstractmethod
from game.board import Board, Coordinate


class AbstractAI(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def learn_from_human_game(self, board: Board):
        pass

    @abstractmethod
    def train_and_save(self):
        pass

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def get_next_move(self, board: Board) -> Coordinate:
        pass
