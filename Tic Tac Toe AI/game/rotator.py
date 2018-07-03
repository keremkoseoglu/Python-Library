''' Board Rotator
Purpose of this class is the ability to rotate the board,
and match patterns on the rotated board.
'''

from game.board import Board, Coordinate


class Rotator:

    _ROTATE_CW = "a"     # Clockwise
    _ROTATE_CCW = "b"    # Counter clockwise
    _FLIP_HOR = "c"      # Horizontal
    _FLIP_VER = "d"      # Vertical

    def __init__(self, matrix: str):
        self._original_matrix = matrix
        self._rotated_matrix = matrix
        self._history = []

    '''
    123    789
    456 -> 456
    789    123
    '''
    def flip_horizontal(self):
        new_matrix = \
            self._rotated_matrix[6:7] + \
            self._rotated_matrix[7:8] + \
            self._rotated_matrix[8:9] + \
            self._rotated_matrix[3:4] + \
            self._rotated_matrix[4:5] + \
            self._rotated_matrix[5:6] + \
            self._rotated_matrix[0:1] + \
            self._rotated_matrix[1:2] + \
            self._rotated_matrix[2:3]
        self._rotated_matrix = new_matrix
        self._history.append(self._FLIP_HOR)

    '''
    123    321
    456 -> 654
    789    987
    '''
    def flip_vertical(self):
        new_matrix = \
            self._rotated_matrix[2:3] + \
            self._rotated_matrix[1:2] + \
            self._rotated_matrix[0:1] + \
            self._rotated_matrix[5:6] + \
            self._rotated_matrix[4:5] + \
            self._rotated_matrix[3:4] + \
            self._rotated_matrix[8:9] + \
            self._rotated_matrix[7:8] + \
            self._rotated_matrix[6:7]
        self._rotated_matrix = new_matrix
        self._history.append(self._FLIP_VER)

    def get_original_coordinate(self, rotated_coordinate:Coordinate) -> Coordinate:
        if len(self._history) == 0:
            return rotated_coordinate

        undo_board = Board()
        undo_board.play(Board.COMPUTER, rotated_coordinate)
        undo_rotator = Rotator(undo_board.get_matrix())

        for i in reversed(range(len(self._history))):
            move_to_undo = self._history[i]
            if move_to_undo == self._FLIP_VER:
                undo_rotator.flip_vertical()
            elif move_to_undo == self._FLIP_HOR:
                undo_rotator.flip_horizontal()
            elif move_to_undo == self._ROTATE_CW:
                undo_rotator.rotate_counter_clockwise()
            elif move_to_undo == self._ROTATE_CCW:
                undo_rotator.rotate_clockwise()

        output = Coordinate()
        output.set_from_pos(undo_rotator.get_rotated_matrix().find(Board.COMPUTER))
        return output

    def get_rotated_matrix(self) -> str:
        return self._rotated_matrix

    def reset(self):
        self._rotated_matrix = self._original_matrix
        self._history.clear()

    '''
    123    741
    456 -> 852
    789    963
    '''
    def rotate_clockwise(self):
        new_matrix = \
            self._rotated_matrix[6:7] + \
            self._rotated_matrix[3:4] + \
            self._rotated_matrix[0:1] + \
            self._rotated_matrix[7:8] + \
            self._rotated_matrix[4:5] + \
            self._rotated_matrix[1:2] + \
            self._rotated_matrix[8:9] + \
            self._rotated_matrix[5:6] + \
            self._rotated_matrix[2:3]
        self._rotated_matrix = new_matrix
        self._history.append(self._ROTATE_CW)

    '''
    123    369
    456 -> 258
    789    147
    '''
    def rotate_counter_clockwise(self):
        new_matrix = \
            self._rotated_matrix[2:3] + \
            self._rotated_matrix[5:6] + \
            self._rotated_matrix[8:9] + \
            self._rotated_matrix[1:2] + \
            self._rotated_matrix[4:5] + \
            self._rotated_matrix[7:8] + \
            self._rotated_matrix[0:1] + \
            self._rotated_matrix[3:4] + \
            self._rotated_matrix[6:7]
        self._rotated_matrix = new_matrix
        self._history.append(self._ROTATE_CCW)
