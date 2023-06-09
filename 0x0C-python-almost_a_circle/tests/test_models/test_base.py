#!/usr/bin/python3
""" Defines unittests for base.py """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ Unittests for testing of the Base class """

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(13, Base(13).id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(13)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(13).__nb_instances)

    def test_str_id(self):
        self.assertEqual("string", Base("string").id)

    def test_float_id(self):
        self.assertEqual(6.4, Base(6.4).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3, 4], Base([1, 2, 3, 4]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2, 3), Base((1, 2, 3)).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


if __name__ == "__main__":
    unittest.main()
