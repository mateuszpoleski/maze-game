"""Tests for level class."""
import unittest
import level

class TestLevel(unittest.TestCase):
    """Level class tests."""
    def setUp(self):
        """Tests setup"""
        self.level1 = level.Level(5)
        self.level2 = level.Level(7)

    def test_initialization(self):
        """Test level initialization."""
        self.assertEqual(self.level1.maze_size, 5)
        self.assertEqual(self.level1.maze, [['X', 'X', 'X', 'X', 'X'],
                                            ['X', 'X', 'X', 'X', 'X'],
                                            ['X', 'X', 'X', 'X', 'X'],
                                            ['X', 'X', 'X', 'X', 'X'],
                                            ['X', 'X', 'X', 'X', 'X']])

        self.assertEqual(self.level2.maze_size, 7)
        self.assertEqual(self.level2.maze, [['X', 'X', 'X', 'X', 'X', 'X', 'X'],
                                            ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
                                            ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
                                            ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
                                            ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
                                            ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
                                            ['X', 'X', 'X', 'X', 'X', 'X', 'X']])

    def test_in_maze(self):
        """Test level in_maze method."""
        self.assertTrue(self.level1.in_maze(0, 0))
        self.assertTrue(self.level1.in_maze(2, 1))
        self.assertTrue(self.level1.in_maze(4, 4))
        self.assertFalse(self.level1.in_maze(-1, 2))
        self.assertFalse(self.level1.in_maze(1, 5))

    def test_create_guide_cells(self):
        """Test level create_guide_cells method."""
        self.level1.create_guide_cells()
        self.level2.create_guide_cells()
        self.assertEqual(self.level1.maze, [['X', 'X', 'X', 'X', 'X'],
                                            ['X', ' ', 'X', ' ', 'X'],
                                            ['X', 'X', 'X', 'X', 'X'],
                                            ['X', ' ', 'X', ' ', 'X'],
                                            ['X', 'X', 'X', 'X', 'X']])

        self.assertEqual(self.level2.maze, [['X', 'X', 'X', 'X', 'X', 'X', 'X'],
                                            ['X', ' ', 'X', ' ', 'X', ' ', 'X'],
                                            ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
                                            ['X', ' ', 'X', ' ', 'X', ' ', 'X'],
                                            ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
                                            ['X', ' ', 'X', ' ', 'X', ' ', 'X'],
                                            ['X', 'X', 'X', 'X', 'X', 'X', 'X']])
    def test_add_start(self):
        """Test level add_start method."""
        self.level1.maze[1][1] = ' '
        self.level1.add_start()
        self.assertEqual(self.level1.maze[1][0], 'P')

        self.level2.maze[1][1] = ' '
        self.level2.add_start()
        self.assertEqual(self.level2.maze[1][0], 'P')

    def test_add_end(self):
        """Test level add_end method."""
        self.level1.maze[3][3] = ' '
        self.level1.add_end()
        self.assertEqual(self.level1.maze[3][4], 'E')

        self.level2.maze[5][5] = ' '
        self.level2.add_end()
        self.assertEqual(self.level2.maze[5][6], 'E')

if __name__ == '__main__':
    unittest.main()
