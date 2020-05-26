import unittest
from tictactoe import player, actions

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
        [EMPTY, EMPTY, "0"]]
        self.assertEqual(player(board), "X")

    def test_o_turn(self):
        board = [[EMPTY, EMPTY, "X"],
        [EMPTY, "X", EMPTY],
        [EMPTY, EMPTY, "0"]]
        self.assertEqual(player(board), "X")

class TestActionsFunction(unittest.TestCase):
    def test_get_actions(self):
        board = [[EMPTY, EMPTY, "0"],
        [EMPTY, "X", "X"],
        ["X", "0", "0"]]
        action = set()
        action.add((0, 0))
        action.add((0, 1))
        action.add((1, 0))
        self.assertEqual(actions(board), action)


if __name__ == '__main__':
    unittest.main()
