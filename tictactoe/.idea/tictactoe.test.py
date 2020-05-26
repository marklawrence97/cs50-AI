import unittest
from tictactoe import player, actions, result, winner, terminal

EMPTY = None

class TestPlayerFunction(unittest.TestCase):
    def test_first_move(self):
        board = [[EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]]
        self.assertEqual(player(board), "X")

    def test_x_turn(self):
        board = [[EMPTY, EMPTY, EMPTY],
        [EMPTY, "X", EMPTY],
        [EMPTY, EMPTY, "O"]]
        self.assertEqual(player(board), "X")

    def test_o_turn(self):
        board = [[EMPTY, EMPTY, "X"],
        [EMPTY, "X", EMPTY],
        [EMPTY, EMPTY, "O"]]
        self.assertEqual(player(board), "O")

class TestActionsFunction(unittest.TestCase):
    def test_get_actions(self):
        board = [[EMPTY, EMPTY, "O"],
        [EMPTY, "X", "X"],
        ["X", "O", "O"]]
        action = set()
        action.add((0, 0))
        action.add((0, 1))
        action.add((1, 0))
        self.assertEqual(actions(board), action)

    def test_get_action(self):
        board = [[EMPTY, EMPTY, "O"],
        [EMPTY, "X", "X"],
        ["X", "O", EMPTY]]
        action = set()
        action.add((0, 0))
        action.add((0, 1))
        action.add((1, 0))
        action.add((2, 2))
        self.assertEqual(actions(board), action)

class TestResultFunction(unittest.TestCase):
    def test_play_actions(self):
        before = [[EMPTY, EMPTY, "O"],
        [EMPTY, "X", "X"],
        ["X", "O", "O"]]
        after = [[EMPTY, EMPTY, "O"],
        ["X", "X", "X"],
        ["X", "O", "O"]]
        self.assertEqual(result(before, (1, 0)), after)

    def test_play_actions(self):
        before = [[EMPTY, EMPTY, "O"],
        ["O", "X", "X"],
        ["X", "O", "X"]]
        after = [[EMPTY, "O", "O"],
        ["O", "X", "X"],
        ["X", "O", "X"]]
        self.assertEqual(result(before, (0, 1)), after)


class TestWinnerFunction(unittest.TestCase):
    def test_x_victory(self):
        board = [[EMPTY, "O", "O"],
                ["X", "X", "X"],
                ["X", "O", EMPTY]]
        self.assertEqual(winner(board), "X")

    def test_o_victory(self):
        board = [[EMPTY, "X", "O"],
                ["X", "X", "O"],
                ["X", "O", "O"]]
        self.assertEqual(winner(board), "O")

    def test_no_victory(self):
        board = [[EMPTY, "O", "O"],
                ["X", "X", "O"],
                ["X", "O", "X"]]
        self.assertEqual(winner(board), None)

    def test_diagonal(self):
        board = [[EMPTY, "O", "X"],
                ["X", "X", "O"],
                ["X", "O", "O"]]
        self.assertEqual(winner(board), "X")

class TestTerminalFunction(unittest.TestCase):
    def test_x_victory(self):
        board = [[EMPTY, "O", "O"],
                ["X", "X", "X"],
                ["X", "O", EMPTY]]
        self.assertTrue(terminal(board))

    def test_o_victory(self):
        board = [["O", "O", "O"],
                ["X", "O", "X"],
                ["X", "X", EMPTY]]
        self.assertTrue(terminal(board))

    def test_end(self):
        board = [["O", "O", "O"],
                ["X", "O", "X"],
                ["X", "X", "X"]]
        self.assertTrue(terminal(board))

    def test_still_playing(self):
        board = [[EMPTY, "O", "O"],
                ["X", "O", "X"],
                ["X", "X", EMPTY]]
        self.assertFalse(terminal(board))

if __name__ == '__main__':
    unittest.main()
