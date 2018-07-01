from model.board import Board, Location, NumberAssignmentError
from model.evaluator import Evaluator
from itertools import permutations

class Result:
    complete = False
    solution = Board()
    success = False

class Solver:

    def __init__(self):
        self._debut_board = Board()
        self._result = Result()

    def _attempt(self):

        missing_numbers = self._debut_board.get_missing_numbers()
        empty_cells = self._debut_board.get_empty_cell_locations()
        number_combinations = permutations(missing_numbers, len(missing_numbers))

        for combo in number_combinations:

            cloned_board = self._debut_board.clone()
            cell_index = 0

            for empty_cell in empty_cells:
                try:
                    cloned_board.set_cell_value(empty_cell.get_x(), empty_cell.get_y(), combo[cell_index])
                    cell_index = cell_index + 1
                except NumberAssignmentError:
                    break

            if cloned_board.has_empty_cell():
                continue

            evaluator = Evaluator()
            evaluator.evaluate(cloned_board)

            if evaluator.is_complete() and evaluator.is_valid():
                self._result.complete = True
                self._result.success = True
                self._result.solution = cloned_board
                return

    def solve(self, board: Board) -> Result:

        self._result = Result()
        self._debut_board = board

        self._attempt()

        return self._result