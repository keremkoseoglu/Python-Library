import test.test_boards
import model.solver

sample_board = test.test_boards.SolvedBoard_Minus_10()

board = sample_board.get_board()
solver = model.solver.Solver()
result = solver.solve(board)

if result.success:
    print("Success")
else:
    print("Failure")