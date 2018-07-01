class Coordinate:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def convert_to_pos(self) -> int:
        return (self.x * 3) + self.y

    def equals(self, x: int, y: int) -> bool:
        return self.x == x and self.y == y

    def set_from_pos(self, pos: int):
        if pos < 3:
            self.x = 0
            self.y = pos
        elif pos < 6:
            self.x = 1
            self.y = pos - 3
        else:
            self.x = 2
            self.y = pos - 6


class Cell:

    def __init__(self, coordinate: Coordinate, player: str):
        self.coordinate = coordinate
        self.player = player


class MoveRecord:

    def __init__(self, board_before: str, coordinate: Coordinate, player: str, board_after: str):
        self.board_before = board_before
        self.coordinate = coordinate
        self.player = player
        self.board_after = board_after


class InvalidBoardMatrixError(Exception):
    pass


class SpaceOccupiedError(Exception):
    pass


class Board:

    '''
    012
    345
    678
    '''

    COMPUTER = "c"
    EMPTY = "e"
    HUMAN = "h"
    SIZE = 3

    def __init__(self):
        self._matrix = ""
        self._last_player = ""
        self._move_history = []

        self._clear_matrix()

    def get_board(self) -> str:
        return self._matrix

    def get_empty_coordinates(self) -> []:

        output = []

        for i in range(9):
            if self._matrix[i:i+1] == self.EMPTY:
                coordinate = Coordinate()
                coordinate.set_from_pos(i)
                output.append(coordinate)

        return output

    def get_move_history(self) -> []:
        return self._move_history

    def get_negative_board(self) -> str:
        output = self.get_board()
        output = output.replace(self.COMPUTER, "T")
        output = output.replace(self.HUMAN, self.COMPUTER)
        output = output.replace("T", self.HUMAN)
        return output

    def get_next_player(self) -> str:
        if self._last_player == self.COMPUTER:
            return self.HUMAN
        else:
            return self.COMPUTER

    def get_player_at_coordinate(self, coordinate:Coordinate):
        pos_in_matrix = coordinate.convert_to_pos()
        return self._matrix[pos_in_matrix: pos_in_matrix + 1]

    def get_winner(self) -> str:

        # This method could have been written better, but the focus is AI so I don't care

        # --- 3 in a row -----

        if self._three_cells_eq(0, 1, 2):
            return self._matrix[2:3]
        elif self._three_cells_eq(3, 4, 5):
            return self._matrix[5:6]
        elif self._three_cells_eq(6, 7, 8):
            return self._matrix[8:9]

        # --- 3 in a col -----

        elif self._three_cells_eq(0, 3, 6):
            return self._matrix[6:7]
        elif self._three_cells_eq(1, 4, 7):
            return self._matrix[7:8]
        elif self._three_cells_eq(2, 5, 8):
            return self._matrix[8:9]

        # --- Diagonal -----

        elif self._three_cells_eq(0, 4, 8):
            return self._matrix[8:9]
        elif self._three_cells_eq(2, 4, 6):
            return self._matrix[6:7]

        # --- No winner -----

        else:
            return self.EMPTY

    def has_empty_cell(self):
        return self._matrix.find(self.EMPTY) >= 0

    def is_game_complete(self):
        return (not self.has_empty_cell()) or self.get_winner() != self.EMPTY

    def play(self, player: str, coordinate: Coordinate):

        # Checks
        if self.get_player_at_coordinate(coordinate) != self.EMPTY:
            raise SpaceOccupiedError()
        board_before = self.get_board()

        # Play
        pos_in_matrix = coordinate.convert_to_pos()
        self._matrix = self._matrix[:pos_in_matrix] + player + self._matrix[pos_in_matrix+1:]

        # Flags
        self._last_player = player
        self._move_history.append(MoveRecord(board_before, coordinate, player, self.get_board()))

    def set_board(self, matrix: str):
        self._matrix = matrix

    def _clear_matrix(self):
        for i in range(9):
            self._matrix += self.EMPTY

    def _three_cells_eq(self, a: int, b: int, c: int) -> bool:
        a_next = a + 1
        b_next = b + 1
        c_next = c + 1

        if self._matrix[a:a_next] != self._matrix[b:b_next]:
            return False

        if self._matrix[b:b_next] != self._matrix[c:c_next]:
            return False

        if self._matrix[c:c_next] == self.EMPTY:
            return False

        return True
