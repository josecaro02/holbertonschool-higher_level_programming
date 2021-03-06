#!/usr/bin/python3
""" Square class file """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class that inherits Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ __init__ method """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ overload method __str__ """
        return("[Square] ({}) {}/{} - {}".
               format(self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """ Method updates info of square """
        if len(args) > 0:
            for att in range(len(args)):
                if att == 0:
                    self.id = args[0]
                if att == 1:
                    self.size = args[1]
                if att == 2:
                    self.x = args[2]
                if att == 3:
                    self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
                if key == "id":
                    self.id = value

    def to_dictionary(self):
        """ Converts square info to a dictionary """
        dict_rect = dict()
        dict_rect["id"] = self.id
        dict_rect["size"] = self.height
        dict_rect["x"] = self.x
        dict_rect["y"] = self.y
        return(dict_rect)

    @property
    def size(self):
        """ Getter size of square """
        return self.width

    @size.setter
    def size(self, size):
        """ Setter size of square """
        self.width = size
        self.height = size
