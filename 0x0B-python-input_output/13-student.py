#!/usr/bin/python3


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        diction = {}
        if type(attrs) == list and (type(i) == str for i in attrs):
            for i in attrs:
                try:
                    getattr(self, i)
                    diction[i] = getattr(self, i)
                except:
                    continue
        else:
            diction['first_name'] = self.first_name
            diction['last_name'] = self.last_name
            diction['age'] = self.age
        return(diction)

    def reload_from_json(self, json):
        try:
            self.first_name = json["first_name"]
        except:
            pass
        try:
            self.last_name = json["last_name"]
        except:
            pass
        try:
            self.age = json["age"]
        except:
            pass
