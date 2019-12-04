#!/usr/bin/python

class Square:
    ############################
    # Helping function
    ############################
    def __trace(self, s):
        print(s)

    ############################
    # Manager function
    ############################
    # Including a default contrutctor
    def __init__(self, b=1):
        self.__side = b
    def __del__(self):
        pass

    ############################
    # Access function
    ############################
    def getSide(self):
        return self.__side
    def setSide(self, b):
        self.__side = b
    def isLarge(self):
        return self.__side > 10

    ############################
    # Implementor function
    ############################
    def toString(self):
        return("Side= " + str(self.__side))
    def area(self):
        return self.__side * self.__side
    def perimeter(self):
        return self.__side * 4