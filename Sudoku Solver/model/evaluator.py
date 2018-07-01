from model.board import Board

class Evaluator:

    def __init__(self):
        self._is_complete = False
        self._is_valid = False

        self._board = Board()

    def _evaluate_col(self, col: int):
        hit_count = {}

        for row in range(Board.BOARD_SIZE):
            number_in_cell = str(self._board.get_cell_value(row, col))

            try:
                current_count = int(hit_count[number_in_cell])
            except KeyError:
                hit_count[number_in_cell] = 0
                current_count = 0

            current_count = current_count + 1
            hit_count[number_in_cell] = current_count

        self._evaluate_hit_count(hit_count)

    def _evaluate_hit_count(self, hit_count):
        for number in range(10):
            number_as_str = str(number)
            try:
                hit_of_number = int(hit_count[number_as_str])
            except KeyError:
                hit_of_number = 0

            if number == 0:
                if hit_of_number > 0:
                    self.is_complete = False
            else:
                if hit_of_number == 0:
                    self._is_complete = False
                elif hit_of_number > 1:
                    self._is_valid = False

    def _evaluate_row(self, row: int):
        hit_count = {}

        for col in range(Board.BOARD_SIZE):
            number_in_cell = str(self._board.get_cell_value(row, col))

            try:
                current_count = int(hit_count[number_in_cell])
            except KeyError:
                hit_count[number_in_cell] = 0
                current_count = 0

            current_count = current_count + 1
            hit_count[number_in_cell] = current_count

        self._evaluate_hit_count(hit_count)

    def evaluate(self, board: Board):
        self._is_complete = True
        self._is_valid = True
        self._board = board

        for row in range(Board.BOARD_SIZE):
            self._evaluate_row(row)

        for col in range(Board.BOARD_SIZE):
            self._evaluate_col(col)

    def is_complete(self) -> bool:
        return self._is_complete

    def is_valid(self) -> bool:
        return self._is_valid
