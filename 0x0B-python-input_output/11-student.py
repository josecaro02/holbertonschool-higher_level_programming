#!/usr/bin/python3


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        diction = {}
        diction['first_name'] = self.first_name
        diction['last_name'] = self.last_name
        diction['age'] = self.age
        return(diction)
