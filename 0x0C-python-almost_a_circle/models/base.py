#!/usr/bin/python3
import json
import csv

class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):

        if list_dictionaries is None:
            return ("[]")
        return json.dumps(list_dictionaries)

    def from_json_string(json_string):

        if json_string is None:
            return ("[]")
        return (json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):

        list_dicts = []
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
#            writer = csv.DictWriter(csvfile, fieldnames=list_names)
#            writer.writeheader()
            writer = csv.writer(csvfile)
            writer.writerow(list_names)
#            for i in range(len(list_objs)):
            dict_class = list_objs[i].to_dictionary()
#                print(dict_class)
            writer.writerow(dict_class)

    @classmethod
    def load_from_file_csv(cls):

        dict_csv = {}
        list_inst = []
        file_name = cls.__name__
        file_name += ".csv"
        try:
            with open(file_name, 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    print(row)
                    for i in row:
                        dict_csv[str(row)] = row[i]
                    list_inst.append(cls.create(**row))
                return (list_inst)
        except:
            return (list_inst)

    @classmethod
    def create(cls, **dictionary):

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
            for i in dictionary:
                setattr(dummy, i, dictionary[str(i)])
            return (dummy)
        if cls.__name__ == "Square":
            dummy = cls(1)
            for i in dictionary:
                 setattr(dummy, i , dictionary[str(i)])
            return (dummy)

    @classmethod
    def load_from_file(cls):

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
