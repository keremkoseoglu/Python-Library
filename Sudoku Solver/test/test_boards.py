from model.board import Board

class TestBoard():

    def __init__(self):
        pass

    def get_board(self) -> Board:
        pass


class SimpleBoard(TestBoard):

    def get_board(self) -> Board:
        output = Board()
        output.fill_matrix_from_string("000260701680070090190004500820100040004602900050003028009300074040050036703018000")
        return output

class SolvedBoard(TestBoard):

    def get_board(self) -> Board:
        output = Board()
        output.fill_matrix_from_string("534678912672195348198342567859761423426853791713924856961537284287419635345286179")
        return output

class SolvedBoard_Minus_1(TestBoard):

    def get_board(self) -> Board:
        output = Board()
        output.fill_matrix_from_string("034678912672195348198342567859761423426853791713924856961537284287419635345286179")
        return output

class SolvedBoard_Minus_2(TestBoard):

    def get_board(self) -> Board:
        output = Board()
        output.fill_matrix_from_string("004678912672195348198342567859761423426853791713924856961537284287419635345286179")
        return output

class SolvedBoard_Minus_5(TestBoard):

    def get_board(self) -> Board:
        output = Board()
        output.fill_matrix_from_string("000008912672195348198342567859761423426853791713924856961537284287419635345286179")
        return output

class SolvedBoard_Minus_10(TestBoard):

    def get_board(self) -> Board:
        output = Board()
        output.fill_matrix_from_string("000000000072195348198342567859761423426853791713924856961537284287419635345286179")
        return output

class EmptyBoard(TestBoard):

    def get_board(self) -> Board:
        output = Board()
        output.fill_matrix_from_string("000000000000000000000000000000000000000000000000000000000000000000000000000000000")
        return output