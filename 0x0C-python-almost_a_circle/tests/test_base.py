#!/usr/bin/python3
"""Unittests for Base class
"""
import unittest
import json
import inspect
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for Base class
    Args:
        unittest (TestCase): inherited class
    """

    def test_AA_documentation(self):
        """test class Base documentation in methods and functions
        """
        self.assertTrue(len(Base.__doc__) > 0)
        func = inspect.getmembers(Base, predicate=inspect.ismethod)
        for name, method in func:
            self.assertTrue(len(method.__doc__) > 0)
        func2 = inspect.getmembers(Base, predicate=inspect.isfunction)
        for name, method in func2:
            self.assertTrue(len(method.__doc__) > 0)

    def test_pep8_Base_class(self):
        """Test that we conform to PEP8 for base class"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors")

    def test_pep8_test_base(self):
        """Test that we conform to PEP8 in test for base class"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors")

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_A_ID_value(self):
        """tests for class base differente instances
        """
        obj = Base()
        self.assertEqual(obj.id, 1)
        obj2 = Base(5)
        self.assertEqual(obj2.id, 5)
        obj3 = Base()
        self.assertEqual(obj3.id, 2)

    def test_B_JSON_repr_success(self):
        """tests for JSON object string representation
        for Rectangle class and Square class
        """
        r1 = Rectangle(15, 10, 5, 3)
        json_string = Base.to_json_string([r1.to_dictionary()])
        self.assertIn('"width": 15', json_string)
        self.assertIn('"height": 10', json_string)
        self.assertIn('"y": 3', json_string)
        self.assertIn('"x": 5', json_string)
        self.assertIs(type(json_string), str)

        s1 = Square(6, 3, 9)
        json_string2 = Base.to_json_string([s1.to_dictionary()])
        self.assertIn('"size": 6', json_string2)
        self.assertIn('"x": 3', json_string2)
        self.assertIn('"y": 9', json_string2)
        self.assertIs(type(json_string2), str)

    def test_C_JSON_repr_empty(self):
        """tests for JSON object string representation in case
        None and empty list entry arguments
        """
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")
        self.assertIs(type(json_string), str)

        json_string2 = Base.to_json_string(None)
        self.assertEqual(json_string2, "[]")
        self.assertIs(type(json_string2), str)

    def test_D_SAVE_to_file_empty(self):
        """Test for save to file method in case of empty
        list in entry argument
        """
        Base.save_to_file([])
        with open("Base.json", encoding="utf-8") as reader:
            self.assertEqual(reader.read(), "[]")

    def test_E_SAVE_to_file(self):
        """Test for save to file method for Rectangle and Square
        objects
        """
        r1 = Rectangle(4, 9, 13)
        r2 = Rectangle(7, 3, 1, 2, 6)
        Rectangle.save_to_file([r1, r2])
        dic_r1 = {"id": 1, "width": 4, "height": 9, "x": 13, "y": 0}
        dic_r2 = {"id": 6, "width": 7, "height": 3, "x": 1, "y": 2}
        with open("Rectangle.json", encoding="utf-8") as reader:
            self.assertIs(type(reader.read()), str)
            self.assertEqual(r1.to_dictionary(), dic_r1)
            self.assertEqual(r2.to_dictionary(), dic_r2)

        s1 = Square(12, 4, 6)
        s2 = Square(5)
        Square.save_to_file([s1, s2])
        dic_s1 = {"id": 2, "size": 12, "x": 4, "y": 6}
        dic_s2 = {"id": 3, "size": 5, "x": 0, "y": 0}
        with open("Square.json", encoding="utf-8") as reader:
            self.assertIs(type(reader.read()), str)
            self.assertEqual(s1.to_dictionary(), dic_s1)
            self.assertEqual(s2.to_dictionary(), dic_s2)

    def test_F_from_string_empty(self):
        """test to check list of JSON string representation
        of empty list and None arguments
        """
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string(None), [])

    def test_G_from_string(self):
        """test to check list of JSON string representation
        of Rectangle and Square objects
        """
        list_dic = [
                    {'id': 56, 'width': 16, 'height': 8},
                    {'id': 9, 'width': 1, 'height': 7}
                ]
        json_list = Rectangle.to_json_string(list_dic)
        list_output = Rectangle.from_json_string(json_list)
        self.assertListEqual(list_output, list_dic)
        self.assertIs(type(list_output), list)

        list_dic2 = [
                        {'id': 7, 'size': 23}
                    ]
        json_list2 = Square.to_json_string(list_dic2)
        list_output2 = Square.from_json_string(json_list2)
        self.assertListEqual(list_output2, list_dic2)
        self.assertIs(type(list_output2), list)

    def test_H_create(self):
        """test new objects with Rectangle and Square class
        """
        r = Rectangle(8, 6, 10)
        check = Rectangle.create(**r.to_dictionary())
        self.assertFalse(r is check)
        self.assertFalse(r == check)

        s = Square(9)
        check = Square.create(**s.to_dictionary())
        self.assertFalse(s is check)
        self.assertFalse(s == check)


if __name__ == '__main__':
    unittest.main()
