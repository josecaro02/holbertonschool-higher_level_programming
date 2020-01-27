#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        print("[Square] ({}) {}/{} - {}".
              format(self.id, self.x, self.y, self.width), end="")
        return("")

    def update(self, *args, **kwargs):
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

        dict_rect = dict()
        dict_rect["id"] = self.id
        dict_rect["size"] = self.height
        dict_rect["x"] = self.x
        dict_rect["y"] = self.y
        return(dict_rect)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError('width must be an integer')
        if size <= 0:
            raise ValueError('width must > 0')
        self.width = size
        self.height = size
