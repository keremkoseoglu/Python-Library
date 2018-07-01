from abc import ABC, abstractmethod
from ai.abstract_ai import AbstractAI
from game.board import Board, Coordinate


class AbstractPlayer(ABC):

    def __init__(self, ai: AbstractAI=None):
        self.ai = ai

    @abstractmethod
    def get_next_move(self, board: Board) -> Coordinate:
        pass