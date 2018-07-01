from ai.abstract_ai import AbstractAI
from game.board import Board, Coordinate
from player.random_player import RandomPlayer
import random

class _PossibleMove:

    def __init__(self, coordinate: Coordinate, value: int):
        self.coordinate = coordinate
        self.value = value


class QLearning(AbstractAI):

    _CRLF = "\r\n"
    _FILE_NAME = "qlearning_memory.txt"
    _FILE_SEP = ";"
    _TRAIN_GAME_COUNT = 1000000

    def __init__(self):
        self._matrix = {}

    def learn_from_human_game(self, board: Board):
        self._learn_from_board(board)
        self._save_to_file()

    def train_and_save(self):

        # --- Play random games -----

        for tgi in range(self._TRAIN_GAME_COUNT):  # TGI = Train Game Index

            # Play
            dojo = Board()
            random_pupil = RandomPlayer(self)
            game_is_active = True
            while game_is_active:
                next_player = dojo.get_next_player()
                next_move = random_pupil.get_next_move(dojo)
                dojo.play(next_player, next_move)
                game_is_active = not dojo.is_game_complete()

            # Evaluate
            self._learn_from_board(dojo)

        # --- Save -----
        self._save_to_file()

    def load(self):
        self._matrix = {}

        text_file = open(self._FILE_NAME, "r")
        text_lines = text_file.readlines()
        text_file.close()

        for line in text_lines:
            split_line = line.split(self._FILE_SEP)
            possible_moves = []
            for i in range(len(split_line)):
                if i == 1 or (i - 1) % 3 == 0:
                    coord = Coordinate(int(split_line[i]), int(split_line[i+1]))
                    possible_move = _PossibleMove(coord, int(split_line[i+2]))
                    possible_moves.append(possible_move)
            self._matrix[split_line[0]] = possible_moves

        x = 1

    def get_next_move(self, board: Board) -> Coordinate:

        # Get previously experienced board position

        try:
            current_state = board.get_board()
            possible_moves = self._matrix[current_state]
        except:
            try:
                current_state = board.get_negative_board()
                possible_moves = self._matrix[current_state]
            except:
                return

        # Get best moves

        best_value = 1
        best_coordinates = []

        for i in range(len(possible_moves)):
            if possible_moves[i].value > best_value:
                best_value = possible_moves[i].value
                best_coordinates.clear()
                best_coordinates.append(possible_moves[i].coordinate)
            elif possible_moves[i].value == best_value:
                best_coordinates.append(possible_moves[i].coordinate)

        # Return random best move
        if len(best_coordinates) == 0:
            return None
        elif len(best_coordinates) == 1:
            return best_coordinates[0]
        else:
            ret_index = random.randint(0, len(best_coordinates) - 1)
            return best_coordinates[ret_index]

    def _add_evaluation(self, board_state:str, possible_move:_PossibleMove):
        # Ensure board state exists in matrix
        if board_state not in self._matrix.keys():
            self._matrix[board_state] = []

        # Add to existing evaluation
        for i in range(len(self._matrix[board_state]) - 1):
            if self._matrix[board_state][i].coordinate.equals(possible_move.coordinate.x, possible_move.coordinate.y):
                self._matrix[board_state][i].value += possible_move.value
                return

        # If doesn't exist, enter new one
        self._matrix[board_state].append(possible_move)

    def _learn_from_board(self, dojo: Board):
        winner = dojo.get_winner()
        if winner == "" or winner == Board.EMPTY:
            return
        history = dojo.get_move_history()
        move_count = len(history)
        for move_index in reversed(range(move_count)):
            move = history[move_index]
            move_value = move_index + 1
            if winner != move.player:
                move_value *= -1
            self._add_evaluation(move.board_before, _PossibleMove(move.coordinate, move_value))

    def _save_to_file(self):
        text_output = ""
        for state in self._matrix:
            text_output += state
            moves = self._matrix[state]
            for i in range(len(moves)):
                text_output += self._FILE_SEP + str(moves[i].coordinate.x) \
                               + self._FILE_SEP + str(moves[i].coordinate.y) \
                               + self._FILE_SEP + str(moves[i].value)
            text_output += self._CRLF

        text_file = open(self._FILE_NAME, "w")
        text_file.write(text_output)
        text_file.close()