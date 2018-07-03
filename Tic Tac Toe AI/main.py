from ai.qlearning import QLearning
from gui.tk_gui import TicTacToeGUI
from player.ai_player import AIPlayer
from player.random_player import RandomPlayer

# ______________________________
# Program functions


def play_with_trained_qlearning():
    q = QLearning()
    q.load()
    player = AIPlayer(q)
    TicTacToeGUI(player)


def play_with_randomizer():
    TicTacToeGUI(RandomPlayer())


def train_qlearning():
    q = QLearning()
    q.train_and_save()

# ______________________________
# Call desired function here

# step 1:
# train_qlearning()

# step 2:
play_with_trained_qlearning()
