#!/usr/bin/python3
""" Defines unittests for models/square.py """
import unittest
from models.base import Base
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """ Unittests for testing the Square class """

    def test_square_is_a_base(self):
        self.assertIsInstance(Square(8), Base)

    def test_no_args_passed(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg_passed(self):
        sq1 = Square(9)
        sq2 = Square(5)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_two_args_passed(self):
        sq1 = Square(8, 4)
        sq2 = Square(6, 3)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_three_args_passed(self):
        sq1 = Square(8, 6, 4)
        sq2 = Square(4, 8, 6)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_four_args_passed(self):
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_getter_size(self):
        self.assertEqual(4, Square(4, 2, 7, 4).size)

    def test_setter_size(self):
        sq = Square(4, 1, 9, 2)
        sq.size = 7
        self.assertEqual(7, sq.size)

    def test_setter_width(self):
        sq = Square(2, 4, 6, 8)
        sq.size = 7
        self.assertEqual(7, sq.width)

    def test_setter_height(self):
        sq = Square(2, 4, 6, 8)
        sq.size = 7
        self.assertEqual(7, sq.width)

    def test_setter_x(self):
        self.assertEqual(0, Square(10).x)

    def test_setter_y(self):
        self.assertEqual(0, Square(10).y)

    """ Tests for size inputs """

    def test_size_is_non_integer(self):

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(6.5)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("string input")

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([2, 4, 6])

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({2, 4, 6})

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((2, 4, 6))

    def test_width_is_non_negative(self):

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-5, 4)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 4)

    """ Tests for x inputs """

    def test_x_is_non_integer(self):

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, None)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, "string input", 4)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, 6.4, 4)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, [2, 4, 6], 4)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, {2, 4, 6}, 4)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, (2, 4, 6), 4)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(6, -4, 2)

    """ Tests for y inputs """

    def test_y_is_non_integer(self):

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 4, None)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 4, "string input")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 4, 6.4)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 4, [2, 4, 6])

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 4, {2, 4, 6})

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 4, (2, 4, 6))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(7, 0, -6)

    """ Tests for the area of the Square """

    def test_area_small(self):
        sq = Square(9, 0, 0, 1)
        self.assertEqual(81, sq.area())

    def test_area_large(self):
        sq = Square(999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999999998000000000000000001, sq.area())

    def test_area_changed_attributes(self):
        sq = Square(5, 0, 0, 1)
        sq.size = 6
        self.assertEqual(36, sq.area())


if __name__ == "__main__":
    unittest.main()
