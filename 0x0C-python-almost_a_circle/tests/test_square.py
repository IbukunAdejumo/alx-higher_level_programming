#!/usr/bin/python3
"""Unittests for Square class
"""
import unittest
import json
import inspect
import pep8
import io
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Test cases for Square class
    Args:
        unittest (TestCase): inherited class
    """

    def test_documentation(self):
        """test class Rectangle documentation in methods and functions
        """
        self.assertTrue(len(Square.__doc__) > 0)
        func = inspect.getmembers(Square, predicate=inspect.ismethod)
        for name, method in func:
            self.assertTrue(len(method.__doc__) > 0)
        func2 = inspect.getmembers(Square, predicate=inspect.isfunction)
        for name, method in func2:
            self.assertTrue(len(method.__doc__) > 0)

    def test_pep8_Rectangle_class(self):
        """Test that we conform to PEP8 for square class"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors")

    def test_pep8_test_rectangle(self):
        """Test that we conform to PEP8 in test for square class"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(result.total_errors, 0)

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_A_entry_normal_values(self):
        """test to check entry values for a Square
        """
        s0 = Square(5)
        s1 = Square(21, 8)
        s2 = Square(12, 6, 4)
        s3 = Square(3, 7, 12, 5)
        self.assertListEqual([s0.size], [5])
        self.assertListEqual([s1.size, s1.x], [21, 8])
        self.assertListEqual([s2.size, s2.x, s2.y], [12, 6, 4])
        self.assertListEqual([s3.size, s3.x, s3.y, s3.id], [3, 7, 12, 5])

    def test_A_entry_wrong_values(self):
        """test to check entry values for a Square
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(0, 6)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square("hello", 16)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s = Square(5, -8, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(16, 1.8)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s = Square(5, 10, -1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(16, 7, (6, 9))

    def test_B_wrong_number_arguments(self):
        """test to check entry values for a Square
        """
        with self.assertRaises(TypeError):
            s = Square(2, 5, 9, 2, 18, 5, 7)
        with self.assertRaises(TypeError):
            s = Square()

    def test_C_area(self):
        """test the area method of a square
        """
        s = Square(8)
        self.assertEqual(s.area(), 64)
        s = Square(3667)
        self.assertEqual(s.area(), 13446889)

    def test_D_str(self):
        """test string representation of an object
        """
        s = Square(70, 17)
        self.assertEqual(str(s), '[Square] (1) 17/0 - 70')
        s = Square(39, 23, 42, 65)
        self.assertEqual(str(s), '[Square] (65) 23/42 - 39')

    def test_E_display(self):
        """test the display representation of a square
        """
        s = Square(6)
        f = io.StringIO()
        with redirect_stdout(f):
            s.display()
        out = f.getvalue()
        self.assertEqual(out, ('#' * 6 + '\n') * 6)

        s = Square(76, 3, 9, 900)
        f = io.StringIO()
        with redirect_stdout(f):
            s.display()
        out = f.getvalue()
        self.assertEqual(out, "\n" * 9 + (" " * 3 + '#' * 76 + '\n') * 76)

    def test_F_update_args(self):
        """test to update square object with arbitrary arguments
        """
        s = Square(7, 32, 6, 18)
        s.update(46)
        self.assertEqual(s.id, 46)
        s.update(24, 11)
        self.assertEqual(s.size, 11)
        s.update(67, 31, 41, 23)
        self.assertEqual(s.y, 23)
        self.assertEqual(s.x, 41)

    def test_G_update_kwargs(self):
        """
        Test for update method: kwargs
        """
        s = Square(19, 48, 5, 1)
        s.update(2, size=3)
        self.assertEqual([s.id, s.size, s.x, s.y], [2, 19, 48, 5])
        s.update(id=42, size=36)
        self.assertEqual([s.id, s.size, s.x, s.y], [42, 36, 48, 5])
        s.update(x=6, y=7, size=56)
        self.assertEqual([s.id, s.size, s.x, s.y], [42, 56, 6, 7])
        s.update(x=0, size=2, y=569, id=8)
        self.assertEqual([s.id, s.size, s.x, s.y], [8, 2, 0, 569])

    def test_H_to_dictionary(self):
        """
        Test for dictionary of object Square
        """
        s = Square(3, 52, 0, 159)
        dic = {'y': 0, 'id': 159, 'size': 3, 'x': 52}
        self.assertEqual(s.to_dictionary(), dic)

        s = Square(18, 6, 12, 69)
        dic = {'y': 12, 'id': 69, 'size': 18, 'x': 6}
        self.assertEqual(s.to_dictionary(), dic)

        s = Square(63, 51)
        s2 = Square(88, 452)
        dic = s.to_dictionary()
        self.assertFalse(s2.update(**dic), dic)

if __name__ == '__main__':
    unittest.main()
