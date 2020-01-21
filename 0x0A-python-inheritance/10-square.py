#!/user/bin/python3


class BaseGeometry:

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')


class Rectangle(BaseGeometry):

        def __init__(self, width, height):
            self.integer_validator("width", width)
            self.integer_validator("height", height)
            self.__width = width
            self.__height = height

        def area(self):
            return (self.__width * self.__height)

        def __str__(self):
            return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)
