import tkinter
from model.board import Board
from model.solver import Solver
from test import test_boards

class SudokuGUI:

    _ENTRY_SIZE = 50
    _BUTTON_WIDTH = 200
    _BUTTON_HEIGHT = 50

    def __init__(self):

        self._window = tkinter.Tk()

        self._inputs = [[0 for x in range(Board.BOARD_SIZE)] for y in range(Board.BOARD_SIZE)]
        self._input_texts = [[0 for x in range(Board.BOARD_SIZE)] for y in range(Board.BOARD_SIZE)]

        for row in range(Board.BOARD_SIZE):
            for col in range(Board.BOARD_SIZE):
                self._input_texts[row][col] = tkinter.StringVar()
                self._inputs[row][col] = tkinter.Entry(master=self._window, textvariable=self._input_texts[row][col])
                self._inputs[row][col].place(x=row*self._ENTRY_SIZE, y=col*self._ENTRY_SIZE, width=self._ENTRY_SIZE, height=self._ENTRY_SIZE)

        self._button = tkinter.Button(master=self._window, text="Solve", command=self._button_click)
        self._button.place(x=0, y=Board.BOARD_SIZE*self._ENTRY_SIZE, width=self._BUTTON_WIDTH, height=self._BUTTON_HEIGHT)

        self._label = tkinter.Label(master=self._window, text="Idle")
        self._label.place(x=self._BUTTON_WIDTH, y=Board.BOARD_SIZE*self._ENTRY_SIZE, width=100, height=self._BUTTON_HEIGHT)

        self._paint_board(test_boards.SolvedBoard_Minus_5().get_board())

        self._window.geometry("450x500")
        self._window.mainloop()

    def _button_click(self):
        self._solve_puzzle()

    def _paint_board(self, board: Board):
        for row in range(Board.BOARD_SIZE):
            for col in range(Board.BOARD_SIZE):
                int_val = board.get_cell_value(row, col)
                if int_val == 0:
                    str_val = ""
                else:
                    str_val = str(int_val)
                self._input_texts[row][col].set(str_val)

    def _solve_puzzle(self):

        self._label["text"] = "Working"
        self._window.update()

        try:

            board = Board()

            for row in range(Board.BOARD_SIZE):
                for col in range(Board.BOARD_SIZE):
                    str_val = self._inputs[row][col].get()
                    if str_val == "":
                        int_val = 0
                    else:
                        int_val = int(str_val)
                    board.set_cell_value(row, col, int_val)

            result = Solver().solve(board)

            if not result.success:
                self._label["text"] = "Failed"
                return

            self._label["text"] = "Success"
            self._paint_board(result.solution)

        except:
            self._label["text"] = "Error"