#!/usr/bin/python3
""" Defines unittests for models/rectangle.py """
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """ Unittests for testing the Rectangle class """

    def test_rectangle_is_a_base(self):
        self.assertIsInstance(Rectangle(8, 4), Base)

    def test_no_args_passed(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg_passed(self):
        with self.assertRaises(TypeError):
            Rectangle(2)

    def test_two_args_passed(self):
        rec1 = Rectangle(8, 4)
        rec2 = Rectangle(6, 3)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_three_args_passed(self):
        rec1 = Rectangle(8, 6, 4)
        rec2 = Rectangle(4, 8, 6)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_four_args_passed(self):
        rec1 = Rectangle(2, 4, 6, 8)
        rec2 = Rectangle(5, 6, 7, 8)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_five_args_passed(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_more_than_five_args_passed(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 4, 6, 8, 10, 11)

    def test_getter_width(self):
        rec = Rectangle(2, 4, 6, 8, 10)
        self.assertEqual(2, rec.width)

    def test_setter_width(self):
        rec = Rectangle(2, 4, 6, 8, 10)
        rec.width = 3
        self.assertEqual(3, rec.width)

    def test_getter_heigh(self):
        rec = Rectangle(2, 4, 6, 8, 10)
        self.assertEqual(4, rec.height)

    def test_setter_height(self):
        rec = Rectangle(2, 4, 6, 8, 10)
        rec.height = 5
        self.assertEqual(5, rec.height)

    def test_getter_x(self):
        rec = Rectangle(2, 4, 6, 8, 10)
        self.assertEqual(6, rec.x)

    def test_setter_x(self):
        rec = Rectangle(2, 4, 6, 8, 10)
        rec.x = 10
        self.assertEqual(10, rec.x)

    def test_getter_y(self):
        rec = Rectangle(2, 4, 6, 8, 10)
        self.assertEqual(8, rec.y)

    def test_setter_y(self):
        rec = Rectangle(2, 4, 6, 8, 10)
        rec.y = 7
        self.assertEqual(7, rec.y)

    """ Tests for width inputs """

    def test_width_is_non_integer(self):

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 5)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(6.5, 5)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("string input", 3)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([2, 4, 6], 4)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({2, 4, 6}, 4)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((2, 4, 6), 4)

    def test_width_is_non_negative(self):

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-5, 4)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 4)

    """ Tests for height inputs """

    def test_height_is_non_integer(self):

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, None)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, 6.5)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, "string input")

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, [2, 4, 6])

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, {2, 4, 6})

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, (2, 4, 6))

    def test_width_is_non_negative(self):

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(5, -4)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(5, 0)

    """ Tests for x inputs """

    def test_x_is_non_integer(self):

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, None)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, "string input", 4)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, 6.4, 4)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, [2, 4, 6], 4)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, {2, 4, 6}, 4)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, (2, 4, 6), 4)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(6, 3, -4, 2)

    """ Tests for y inputs """

    def test_y_is_non_integer(self):

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 6, None)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 6, "string input")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 6, 6.4)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 6, [2, 4, 6])

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 6, {2, 4, 6})

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 6, (2, 4, 6))

    def test_negative_y(self):

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(7, 6, 0, -6)

    """ Tests for the area of the Rectangle """

    def test_area_small(self):

        rec = Rectangle(10, 3, 0, 0, 0)
        self.assertEqual(30, rec.area())

    def test_area_large(self):
        rec = Rectangle(999999999999999, 999999999999999999, 0, 0, 0)
        self.assertEqual(999999999999998999000000000000001, rec.area())

    def test_area_changed_attributes(self):
        rec = Rectangle(2, 4, 0, 0, 1)
        rec.width = 9
        rec.height = 8
        self.assertEqual(72, rec.area())


if __name__ == "__main__":
    unittest.main()
