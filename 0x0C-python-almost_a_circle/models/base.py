#!/usr/bin/python3
"""Module for Base class."""

import json
import csv


class Base:
    """Base class for other geometric classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries.
        """

        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.
        """

        filename = cls.__name__ + ".json"
        with open(filename, "w") as myfile:
            if list_objs is None:
                myfile.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                myfile.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string.
        """
        if not json_string or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            raise Exception("Class not recognized for instance creation")
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a file containing JSON strings.

        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_str = file.read()
                dictionaries = cls.from_json_string(json_str)
                return [cls.create(**d) for d in dictionaries]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV string representation of list_objs to a file.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fieldnames = ["id", "size", "x", "y"]
            else:
                raise Exception("Class not recognized for CSV serialization")

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances from a file containing CSV strings.

        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                reader = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict(row) for row in reader if row["id"] != "id"]
                for d in list_dicts:
                    for key, value in d.items():
                        d[key] = int(value)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []
