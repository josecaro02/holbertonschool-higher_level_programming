#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        return (self.width * self.height)

    def display(self):
        for y_t in range(self.y):
            print("")
        for i in range(self.__height):
            for x_t in range(self.x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end='')
            print("")

    def update(self, *args, **kwargs):
        if len(args) > 0:
            for att in range(len(args)):
                if att == 0:
                    self.id = args[0]
                if att == 1:
                    self.width = args[1]
                if att == 2:
                    self.height = args[2]
                if att == 3:
                    self.x = args[3]
                if att == 4:
                    self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
                if key == "id":
                    self.id = value

    def to_dictionary(self):

        dict_rect = dict()
        dict_rect["id"] = self.id
        dict_rect["width"] = self.width
        dict_rect["height"] = self.height
        dict_rect["x"] = self.x
        dict_rect["y"] = self.y
        return(dict_rect)

    def __str__(self):
        print("[Rectangle] ({}) {}/{} - {}/{}".
              format(self.id, self.x, self.y, self.width, self.height), end="")
        return("")

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must > 0')
        self.__width = width

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise TypeError('height must >0')
        self.__height = height

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >=0')
        self.__x = x

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('x must be >=0')
        self.__y = y
