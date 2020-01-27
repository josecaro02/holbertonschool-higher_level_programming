#!/usr/bin/python3
"""Base class file """
import json
import csv


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ method that convert a dictionary to a json"""
        if list_dictionaries is None:
            return ("[]")
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ method that converts a json to a  dictionary"""
        list_rtn = []
        if json_string is None:
            return (list_rtn)
        return (json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        """ method that save a list of objects into a file  """
        list_dicts = []
        if list_objs is not None:
            for i in range(len(list_objs)):
                dict_class = list_objs[i].to_dictionary()
                list_dicts.append(dict_class)
        obj_class = cls.to_json_string(list_dicts)
        file_name = cls.__name__
        file_name += ".json"
        with open(file_name, 'w', encoding="utf-8") as f:
            f.write(obj_class)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ method that save a list of objects into a csv file """
        list_names = []
        list_values = []
        created_names = 0
        pos_key = 0
        for i in range(len(list_objs)):
            list_values.append([])
            dict_class = list_objs[i].to_dictionary()
            if created_names == 0:
                for j in dict_class:
                    list_names.append(j)
                created_names = 1
        file_name = cls.__name__
        file_name += ".csv"
        with open(file_name, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=list_names)

            writer.writeheader()
            for i in range(len(list_objs)):
                dict_class = list_objs[i].to_dictionary()
                writer.writerow(dict_class)

    @classmethod
    def load_from_file_csv(cls):
        """ Method that load the info of a csv file """
        dict_csv = {}
        list_inst = []
        file_name = cls.__name__
        file_name += ".csv"
        try:
            with open(file_name, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    for key in row:
                        dict_csv[key] = int(row[key])
                    list_inst.append(cls.create(**dict_csv))
                return (list_inst)
        except:
            return (list_inst)

    @classmethod
    def create(cls, **dictionary):
        """ Method that instantiate an objecte in base of a dict info """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
            dummy.update(**dictionary)
            return (dummy)
        if cls.__name__ == "Square":
            dummy = cls(1)
            dummy.update(**dictionary)
            return (dummy)

    @classmethod
    def load_from_file(cls):
        """ Method that loads info from a json file and asign it to a object"""
        list_inst = []
        file_name = cls.__name__
        file_name += ".json"
        try:
            with open(file_name) as f:
                text_file = f.read()
                string_json = cls.from_json_string(text_file)
                for text_str in string_json:
                    list_inst.append(cls.create(**text_str))
                return (list_inst)
        except:
            return(list_inst)
