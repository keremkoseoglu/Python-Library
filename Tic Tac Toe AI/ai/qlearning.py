from ai.abstract_ai import AbstractAI
from game.board import Board, Coordinate
from game.rotator import Rotator
from player.random_player import RandomPlayer
from player.ai_player import AIPlayer
import random

class _PossibleMove:

    def __init__(self, coordinate: Coordinate, value: int):
        self.coordinate = coordinate
        self.value = value


class QLearning(AbstractAI):

    _CRLF = "\r\n"
    _FILE_NAME = "qlearning_memory.txt"
    _FILE_SEP = ";"
    _TRAIN_GAME_COUNT = 10000

    def __init__(self):
        self._matrix = {}

    def learn_from_human_game(self, board: Board):
        self._learn_from_board(board)
        self._save_to_file()

    def train_and_save(self):

        # ______________________________
        # Play random games

        for tgi in range(self._TRAIN_GAME_COUNT):  # TGI = Train Game Index

            # Play
            dojo = Board()
            random_pupil = RandomPlayer(self)
            ai_pupil = AIPlayer(self)
            game_is_active = True
            while game_is_active:
                next_player = dojo.get_next_player()

                if (random.randint(1, 10)) < 8:
                    next_move = random_pupil.get_next_move(dojo)
                else:
                    next_move = ai_pupil.get_next_move(dojo)

                dojo.play(next_player, next_move)
                game_is_active = not dojo.is_game_complete()

            # Evaluate
            self._learn_from_board(dojo)

        # ______________________________
        # Save

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


    '''
    This is where the AI "thinks". It returns the best possible move it can think of
    '''

    def get_next_move(self, board: Board) -> Coordinate:

        # ______________________________
        # Get previously experienced board position

        possible_moves = []

        try:
            current_state = board.get_board()
            possible_moves = self._matrix[current_state]
        except:
            try:
                current_state = board.get_negative_board()
                possible_moves = self._matrix[current_state]
            except:
                pass

        # ______________________________
        # Get previously experienced board positions by rotating

        must_rotate = False

        if len(possible_moves) == 0:
            must_rotate = True
        else:
            for i in range(len(possible_moves)):
                if possible_moves[i].value > 0:
                    must_rotate = False
                    break

        if must_rotate:
            possible_moves.extend(self._get_rotated_possible_moves(board.get_board()))
            possible_moves.extend(self._get_rotated_possible_moves(board.get_negative_board()))

        # ______________________________
        # Get best moves

        if len(possible_moves) == 0:
            return None

        best_value = 1
        best_coordinates = []

        for i in range(len(possible_moves)):
            if possible_moves[i].value > best_value:
                best_value = possible_moves[i].value
                best_coordinates.clear()
                best_coordinates.append(possible_moves[i].coordinate)
            elif possible_moves[i].value == best_value:
                best_coordinates.append(possible_moves[i].coordinate)

        # ______________________________
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

    def _get_rotated_possible_moves(self, current_state:str) -> []:
        output = []
        rotator = Rotator(current_state)

        for a in range(2):
            for b in range(2):
                for c in range(3):
                    rotator.rotate_clockwise()
                    try:
                        for possible_move in self._matrix[rotator.get_rotated_matrix()]:
                            new_possible_coor = rotator.get_original_coordinate(possible_move.coordinate)
                            new_possible_move = _PossibleMove(new_possible_coor, possible_move.value)
                            output.append(new_possible_move)
                    except:
                        pass
                rotator.reset()
                rotator.flip_horizontal()
            rotator.reset()
            rotator.flip_vertical()

        return output

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