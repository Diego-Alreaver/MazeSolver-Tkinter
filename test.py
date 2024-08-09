import unittest
from maze import Maze
from tkinter import Tk, BOTH, Canvas
from window import Window, Point, Line, Cell
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        screen_x = 800
        screen_y = 600
        win = Window(screen_x, screen_y)
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

if __name__ == "__main__":
    unittest.main() 