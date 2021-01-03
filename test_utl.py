"""Tests for utilities."""
import unittest
import utl

class TestUtl(unittest.TestCase):
    """Test utilities."""
    def test_in_range(self):
        """Test in_range function."""
        self.assertTrue(utl.in_range(0, 0, 5))
        self.assertTrue(utl.in_range(1, 1, 5))
        self.assertTrue(utl.in_range(4, 4, 5))
        self.assertTrue(utl.in_range(2, 3, 5))
        self.assertFalse(utl.in_range(0, -1, 5))
        self.assertFalse(utl.in_range(0, 5, 5))
        self.assertFalse(utl.in_range(7, 7, 5))

    def test_pixel_coords_to_pos(self):
        """Test pixel coords to position convertion."""
        self.assertEqual(utl.pixel_coords_to_pos(-288, 288, 25), (0, 0))
        self.assertEqual(utl.pixel_coords_to_pos(-288, -288, 25), (0, 24))
        self.assertEqual(utl.pixel_coords_to_pos(288, 288, 25), (24, 0))
        self.assertEqual(utl.pixel_coords_to_pos(288, -288, 25), (24, 24))
        self.assertEqual(utl.pixel_coords_to_pos(0, 0, 25), (12, 12))

if __name__ == '__main__':
    unittest.main()
