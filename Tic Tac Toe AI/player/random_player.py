from game.board import Board, Coordinate
from player.abstract_player import AbstractPlayer
import random


class RandomPlayer(AbstractPlayer):

    def get_next_move(self, board: Board) -> Coordinate:
        empty_coordinates = board.get_empty_coordinates()
        if len(empty_coordinates) == 0:
            return None
        elif len(empty_coordinates) == 1:
            return empty_coordinates[0]
        else:
            random_index = random.randint(0, len(empty_coordinates) - 1)
            return empty_coordinates[random_index]

