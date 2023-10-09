#!/usr/bin/python3
"""DocString"""


class square():
    """ Square class """

    def __init__(self, *args, **kwargs):
        """docString"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """docString"""
        return (self.width * 2) + (self.width * 2)

    def __str__(self):
        """docString"""
        return "{}/{}".format(self.width, self.width)

if __name__ == "__main__":
    """docString"""
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
