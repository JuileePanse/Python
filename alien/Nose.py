#!/usr/bin/python

# Nose.py

class Nose:
    ############################
    # Helping function
    ############################
    def __trace(self, s):
        print(s)

    ############################
    # Manager function
    ############################
    # Including a default construtctor
    def __init__(self, x, y, z):
        self.__side_x = x
        self.__side_y = y
        self.__side_z = z
    def __del__(self):
        pass

    ############################
    # Access function
    ############################
    def getSideX(self):
        return self.__side_x
    def setSideX(self, x):
        self.__side_x = x
    def getSideY(self):
        return self.__side_y
    def setSideY(self, y):
        self.__side_y = y
    def getSideZ(self):
        return self.__side_z
    def setSideZ(self, z):
        self.__side_z = z
    def isBig(self):
        return self.__side_x > 10 or self.__side_y > 10 or self.__self_z > 10

    ############################
    # Implementor function
    ############################
    def toString(self):
       return ("Side X = " + str(self.__side_x) + " Side Y = " + str(self.__side_y) + " Side Z = " + str(self.__side_z))
    def break1(self):
       self.__side_x = 0;