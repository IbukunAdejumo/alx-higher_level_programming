#!/usr/bin/python3
"""Unittests for Rectangle class
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
    """Test cases for Rectangle class
    Args:
        unittest (TestCase): inherited class
    """

    def test_documentation(self):
        """test class Rectangle documentation in methods and functions
        """
        self.assertTrue(len(Rectangle.__doc__) > 0)
        func = inspect.getmembers(Rectangle, predicate=inspect.ismethod)
        for name, method in func:
            self.assertTrue(len(method.__doc__) > 0)
        func2 = inspect.getmembers(Rectangle, predicate=inspect.isfunction)
        for name, method in func2:
            self.assertTrue(len(method.__doc__) > 0)

    def test_pep8_Rectangle_class(self):
        """Test that we conform to PEP8 for rectangle class"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors")

    def test_pep8_test_rectangle(self):
        """Test that we conform to PEP8 in test for rectangle class"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0)

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_A_entry_normal_values(self):
        """test to check entry values for a Rectangle
        """
        r1 = Rectangle(3, 6)
        r2 = Rectangle(5, 2, 9)
        r3 = Rectangle(10, 7, 12, 5)
        r4 = Rectangle(17, 11, 1, 8, 98)
        r4_list = [r4.width, r4.height, r4.x, r4.y, r4.id]
        self.assertListEqual([r1.width, r1.height], [3, 6])
        self.assertListEqual([r2.width, r2.height, r2.x], [5, 2, 9])
        self.assertListEqual([r3.width, r3.height, r3.x, r3.y], [10, 7, 12, 5])
        self.assertListEqual(r4_list, [17, 11, 1, 8, 98])

    def test_A_entry_wrong_values(self):
        """test to check entry values for a Rectangle
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-43, 6)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 82)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("holi", 16)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(67.9, 32, 9)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle([6, 9, 0], 45)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(5, -73, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(5, 0)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(16, 3.8)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(16, (6, 3, 9))
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(5, 12, -28)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(5, 7, (4, 6))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(16, 31, 'x')
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(5, 10, 8, -1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(16, 7, 4, [6])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(16, 7, 4, 'y')
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(16, 7, 4, 5.2)

    def test_B_wrong_number_arguments(self):
        """test to check entry values for a Rectangle
        """
        with self.assertRaises(TypeError):
            r = Rectangle(2)
        with self.assertRaises(TypeError):
            r = Rectangle(2, 5, 9, 2, 18, 5, 7)
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_C_area(self):
        """test the area method of a rectangle
        """
        r = Rectangle(4, 8)
        self.assertEqual(r.area(), 32)
        r = Rectangle(7521, 8621475)
        self.assertEqual(r.area(), 64842113475)

    def test_D_str(self):
        """test string representation of an object
        """
        r = Rectangle(5, 7, 5)
        self.assertEqual(str(r), '[Rectangle] (1) 5/0 - 5/7')
        r = Rectangle(34, 9, 4, 26, 8)
        self.assertEqual(str(r), '[Rectangle] (8) 4/26 - 34/9')

    def test_E_display(self):
        """test the display representation of a rectangle
        """
        r = Rectangle(2, 2)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        out = f.getvalue()
        self.assertEqual(out, ('#' * 2 + '\n') * 2)

        r = Rectangle(5, 8, 4, 1)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        out = f.getvalue()
        self.assertEqual(out, "\n" * 1 + (" " * 4 + '#' * 5 + '\n') * 8)

    def test_F_update_args(self):
        """test to update rectangle object with arbitrary arguments
        """
        r = Rectangle(3, 7, 6, 2, 18)
        r.update(500)
        self.assertEqual(r.id, 500)
        r.update(2, 3, 40)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 40)
        r.update(1, 5, 7, 23)
        self.assertEqual(r.x, 23)
        r.update(18, 6, 4, 5, 45)
        self.assertEqual(r.y, 45)

    def test_G_update_kwargs(self):
        """
        Test for update method: kwargs
        """
        r = Rectangle(5, 27, 3, 8, 2)
        r.update(8, id=7)
        self.assertEqual([r.id, r.width, r.height, r.x, r.y], [8, 5, 27, 3, 8])
        r.update(id=6, width=7)
        self.assertEqual([r.id, r.width, r.height, r.x, r.y], [6, 7, 27, 3, 8])
        r.update(x=6, y=7, height=56)
        self.assertEqual([r.id, r.width, r.height, r.x, r.y], [6, 7, 56, 6, 7])
        r.update(x=1, height=2, y=3, width=4, id=8)
        self.assertEqual([r.id, r.width, r.height, r.x, r.y], [8, 4, 2, 1, 3])

    def test_H_to_dictionary(self):
        """
        Test for dictionary of object Rectangle
        """
        r = Rectangle(2, 5, 7)
        dic = {'y': 0, 'id': 1, 'width': 2, 'x': 7, 'height': 5}
        self.assertEqual(r.to_dictionary(), dic)

        r = Rectangle(22, 53, 17, 34, 8)
        dic = {'y': 34, 'id': 8, 'width': 22, 'x': 17, 'height': 53}
        self.assertEqual(r.to_dictionary(), dic)

        r = Rectangle(98, 37)
        r2 = Rectangle(1, 1)
        dic = r.to_dictionary()
        self.assertFalse(r2.update(**dic), dic)

if __name__ == '__main__':
    unittest.main()
