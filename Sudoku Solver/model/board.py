class NumberAssignmentError(Exception):
    def __init__(self, number):
        self.number = number


class NumberUsedInColError(NumberAssignmentError):
    pass


class NumberUsedInRowError(NumberAssignmentError):
    pass


class NumberNotFreeError(NumberAssignmentError):
    pass


class Location:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y


class Board:

    BOARD_SIZE = 9

    def __init__(self):
        self._matrix = [[0 for x in range(self.BOARD_SIZE)] for y in range(self.BOARD_SIZE)]
        self._missing_numbers = []
        self._initialize_missing_numbers(recognize_matrix=False)

    def _initialize_missing_numbers(self, recognize_matrix=True):
        self._missing_numbers = []
        for row in range(self.BOARD_SIZE):
            for col in range(self.BOARD_SIZE):
                self._missing_numbers.append(row + 1)

        if recognize_matrix:
            for row in range(self.BOARD_SIZE):
                for col in range(self.BOARD_SIZE):
                    number_to_be_removed = self._matrix[row][col]
                    if number_to_be_removed != 0:
                        self._missing_numbers.remove(number_to_be_removed)

    def clone(self):
        output = Board()
        output.set_matrix(self._matrix)
        return output

    def get_cell_value(self, row: int, col: int) -> int:
        return self._matrix[row][col]

    def get_empty_cell_locations(self) -> []:
        output = []
        for row in range(self.BOARD_SIZE):
            for col in range(self.BOARD_SIZE):
                if self.get_cell_value(row, col) == 0:
                    location = Location(row, col)
                    output.append(location)
        return output

    def get_missing_numbers(self):
        return self._missing_numbers

    def has_empty_cell(self) -> bool:
        if len(self._missing_numbers) == 0:
            return False
        else:
            return True

    def has_value_in_col(self, col: int, val: int) -> bool:
        for row in range(self.BOARD_SIZE):
            if self.get_cell_value(row, col) == val:
                return True;
        return False;

    def has_value_in_row(self, row: int, val: int) -> bool:
        for col in range(self.BOARD_SIZE):
            if self.get_cell_value(row, col) == val:
                return True;
        return False;

    def set_cell_value(self, row: int, col: int, val: int):
        if val != 0:
            if val not in self._missing_numbers:
                raise NumberNotFreeError(val)
            if self.has_value_in_row(row, val):
                raise NumberUsedInRowError(val)
            if self.has_value_in_col(col, val):
                raise NumberUsedInColError(val)

        self._matrix[row][col] = val

        if val != 0:
            self._missing_numbers.remove(val)

    def set_matrix(self, matrix):
        for row in range(self.BOARD_SIZE):
            for col in range(self.BOARD_SIZE):
                self._matrix[row][col] = matrix[row][col]

        self._initialize_missing_numbers(recognize_matrix=True)

    def set_missing_numbers(self, numbers):
        self._missing_numbers = numbers

    def fill_matrix_from_string(self, val: str):
        for row in range(self.BOARD_SIZE):
            for col in range(self.BOARD_SIZE):
                str_pos = (row * self.BOARD_SIZE) + col
                current_char = val[str_pos:str_pos+1]
                self.set_cell_value(row, col, int(current_char))
        self._initialize_missing_numbers(recognize_matrix=True)