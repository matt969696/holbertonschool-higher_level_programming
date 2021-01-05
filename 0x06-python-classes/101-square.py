#!/usr/bin/python3
"""
Square Module - Contains simple class definition of Square
"""


class Square:
    """
    Square Class : simple implementation
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Square Init : initialize a square

        Attributes:
        size (int): Size of the square, must be positive or 0
        position (tuple) : Position of the square, tuple of 2 positive integers
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter for size attribute of square object
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Setter for size attribute of square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        """
        Getter for position attribute of square object
        """
        return self.__position

    @position.setter
    def position(self, position):
        """
        Setter for position attribute of square object
        """
        iscorrect = 0
        if isinstance(position, tuple):
            if len(position) == 2:
                if isinstance(position[0], int):
                    if isinstance(position[1], int):
                        if position[0] >= 0 and position[1] >= 0:
                            iscorrect = 1

        if iscorrect:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
        Return the current square area
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
        Prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)

    def __str__(self):
        """
        Prints in stdout the square with the character #
        """
        if self.__size == 0:
            return ""

        out = ""
        for i in range(self.__position[1]):
            out += '\n'
        for i in range(self.__size):
            out += ' ' * self.__position[0]
            out += '#' * self.__size
            out += '\n'
        return out[:-1]
