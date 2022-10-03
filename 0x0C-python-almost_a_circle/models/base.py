#!/usr/bin/python3
"""Define Base class
"""


import json
import csv


class Base:
    """Define Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialisation
        Args:
            id (int, None): integer identification. Defaults to None.
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Function to returns the JSON string
        representation of list_dictionaries
        Args:
            list_dictionaries (dict): instance dictionary
        Returns:
            str: JSON object as a string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of list_objs to a file
        Args:
            list_objs (objects): class instances
        """
        list_cls = []
        if list_objs is not None:
            for i in list_objs:
                list_cls += [(cls.to_dictionary(i))]

        with open(cls.__name__ + ".json", "w", encoding="utf-8") as writer:
            writer.write(cls.to_json_string(list_cls))

    @staticmethod
    def from_json_string(json_string):
        """Function that returns the list of
        the JSON string representation
        Args:
            json_string (str): JSON string representation
        Returns:
            list : list of JSON string
        """
        if json_string == "[]" or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Function with instance
        with all attributes already set
        Returns:
            [object]: instance of the class
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        if cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Function that load the list of JSON strings,
        create instances and returns a list of instances
        Returns:
            list : list of instances
        """
        try:
            with open(cls.__name__ + '.json', encoding="utf-8") as reader:
                data = cls.from_json_string(reader.read())
                return [cls.create(**dic) for dic in data]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Function that write to a CSV file
        from a Python dictionary
        Args:
            list_objs (list): list of objects
        """
        if cls.__name__ == "Rectangle":
            attr = ['id', 'width', 'height', 'x', 'y']
        else:
            attr = ['id', 'size', 'x', 'y']

        with open(cls.__name__ + ".csv", "w", encoding="utf-8") as file:
            write = csv.DictWriter(file, fieldnames=attr)
            write.writeheader()
            for obj in list_objs:
                write.writerow(cls.to_dictionary(obj))

    @classmethod
    def load_from_file_csv(cls):
        """Function that load the objcets of a CSV file
        as dictionary, create instances and returns a
        list of instances
        Returns:
            list : list of intances
        """
        with open(cls.__name__ + ".csv", encoding="utf-8") as file:
            read = csv.DictReader(file)
            new_list = [{k: int(v) for k, v in obj.items()} for obj in read]
            return [cls.create(**dic) for dic in new_list]
