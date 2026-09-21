import unittest

from maze import Maze


class MazeTests(unittest.TestCase):
    """Tests for maze construction, boundaries, and DFS solving."""

    def test_maze_create_cells(self) -> None:
        """The requested number of columns and rows should be created."""
        dimensions = ((12, 10), (5, 2))

        for num_cols, num_rows in dimensions:
            with self.subTest(num_cols=num_cols, num_rows=num_rows):
                maze = Maze(0, 0, num_cols, num_rows, 10, 10)

                self.assertEqual(len(maze._cells), num_cols)
                self.assertTrue(
                    all(len(column) == num_rows for column in maze._cells)
                )

    def test_break_entrance_and_exit(self) -> None:
        """The maze should open its entrance and exit walls."""
        maze = Maze(0, 0, 10, 10, 10, 10)

        maze._break_entrance_and_exit()

        self.assertFalse(maze._cells[0][0].has_top_wall)
        self.assertFalse(maze._cells[-1][-1].has_bottom_wall)

    def test_seeded_maze_can_be_solved(self) -> None:
        """A deterministically generated maze should have a DFS solution."""
        maze = Maze(0, 0, 8, 6, 10, 10, seed=42)

        maze._break_entrance_and_exit()
        maze._break_walls_r(0, 0)
        maze._reset_cells_visited()

        self.assertTrue(maze.solve())


if __name__ == "__main__":
    unittest.main()
