import tkinter
from game.board import Board, Coordinate, SpaceOccupiedError
from player.abstract_player import AbstractPlayer


class TicTacToeGUI:

    _BUTTON_WIDTH = 50
    _BUTTON_HEIGHT = 50
    _WINDOW_WIDTH = 150
    _WINDOW_HEIGHT = 250

    def __init__(self, player: AbstractPlayer):

        # --- Common objects -----

        self._player = player
        self._board = Board()
        self._window = tkinter.Tk()

        # --- Game buttons -----

        self._buttons = [[0 for x in range(Board.SIZE)] for y in range(Board.SIZE)]
        self._button_texts = [[0 for x in range(Board.SIZE)] for y in range(Board.SIZE)]

        for row in range(Board.SIZE):
            for col in range(Board.SIZE):
                self._button_texts[row][col] = tkinter.StringVar()
                self._buttons[row][col] = tkinter.Button(master=self._window, textvariable=self._button_texts[row][col], command=lambda x=row, y=col: self._button_click(x, y))
                self._buttons[row][col].place(x=row*self._BUTTON_WIDTH, y=col*self._BUTTON_HEIGHT, width=self._BUTTON_WIDTH, height=self._BUTTON_HEIGHT)

        # --- Info label -----

        self._info_label_text = tkinter.StringVar()
        self._info_label = tkinter.Label(master=self._window, textvariable=self._info_label_text)
        self._info_label.place(x=0, y=self._BUTTON_HEIGHT*3, width=self._BUTTON_WIDTH*3, height=self._BUTTON_HEIGHT)
        self._info_label_text.set("Ready")

        # --- Restart -----

        self._restart_button = tkinter.Button(master=self._window, text="Restart", command=self._restart_game)
        self._restart_button.place(x=0, y=self._BUTTON_HEIGHT*4, width=self._BUTTON_WIDTH*3, height=self._BUTTON_HEIGHT)

        # --- Flush -----

        self._window.geometry(str(self._WINDOW_WIDTH) + "x" + str(self._WINDOW_HEIGHT))
        self._window.mainloop()

    def _button_click(self, row: int, col: int):

        # --- Human move -----

        try:
            self._board.play(Board.HUMAN, Coordinate(row, col))
        except SpaceOccupiedError:
            return

        winner = self._board.get_winner()
        if winner != Board.EMPTY:
            self._player.ai.learn_from_human_game(self._board)
            self._info_label_text.set("winner: " + winner)
            self._paint_board()
            return

        # --- AI move -----

        ai_move = self._player.get_next_move(self._board)
        if ai_move is None:
            self._info_label_text.set("AI didn't respond")
            self._paint_board()
            return
        self._board.play(Board.COMPUTER, ai_move)

        winner = self._board.get_winner()
        if winner != Board.EMPTY:
            self._info_label_text.set("winner: " + winner)
            self._player.ai.learn_from_human_game(self._board)

        self._paint_board()

    def _paint_board(self):
        for row in range(Board.SIZE):
            for col in range(Board.SIZE):
                player = self._board.get_player_at_coordinate(Coordinate(row, col))
                if player == Board.EMPTY:
                    str_val = ""
                else:
                    str_val = player
                self._button_texts[row][col].set(str_val)

    def _restart_game(self):
        self._board = Board()
        self._paint_board()
        self._info_label_text.set("Ready")