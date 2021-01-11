#!/usr/bin/python3
"""
Rectangle Module - Contains simple class definition of Rectangle Class
"""


class Rectangle:
    """
    Rectangle Class : simple implementation
    Class attribute :
    number_of_instances : number of rectangles
    print_symbol : symbol used for printing rectangles
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Rectangle : initialize a rectangle
        Attributes :
        Private instance attribute: width must be positive integer
        Private instance attribute: height must be positive integer
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ Getter for the width attribute"""
        return self.__width

    @width.setter
    def width(self, width):
        """ Setter for the width attribute"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        """ Getter for the height attribute"""
        return self.__height

    @height.setter
    def height(self, height):
        """ Setter for the height attribute"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def area(self):
        """ Method that return the current rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """ Method that return the current rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """ Return a string with rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""

        out = ""
        for i in range(self.__height):
            out += str(self.print_symbol) * self.__width
            out += '\n'
        return out[:-1]

    def __repr__(self):
        """ Return a string representation of the rectangle"""
        out = "Rectangle(" + str(self.__width)
        out = out + ", " + str(self.__height) + ")"
        return out

    def __del__(self):
        """ Deleter for instance of Rectangle)"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Compares the area of 2 Rectangle objects"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """ Create a square instance of Rectangle class"""
        return cls(size, size)
