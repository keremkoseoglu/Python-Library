from game.board import Board, Coordinate
from player.abstract_player import AbstractPlayer
from player.random_player import RandomPlayer


class AIPlayer(AbstractPlayer):

    def get_next_move(self, board: Board) -> Coordinate:

        # AI response

        output = self.ai.get_next_move(board)

        # Fallback: Random

        if output is None:
            output = RandomPlayer().get_next_move(board)

        # Flush

        return output

