#!/usr/bin/python

class ClassicalChinaCoin:
    ############################
    # Helping function
    ############################
    def __pi(self):
        return 3.1416

    ############################
    # Manager function
    ############################
    # Including a default construtctor
    def __init__(self, r, square, ao):
        self.__radius = r
        self.__square = square
        self.__ancientObject = ao
    def __del__(self):
        pass

    ############################
    # Access function
    ############################
    def getRadius(self):
        return self.__radius
    def setRadius(self, r):
        self.__radius = r
    def getSquare(self):
        return self.__square
    def setSquare(self, square):
        self.__square = square
    def getAncientObject(self):
        return self.__ancientObject
    def setAncientObject(self, ao):
        self.__ancientObject = ao
    def isLarge(self):
        return self.__radius > 20
    def isValid(self):
        return self.area() > 0

    ############################
    # Implementor function
    ############################
    def toString(self):
        return(self.getSquare().toString() + "\n" \
               + "Radius= " +  str(self.__radius) + "\n" \
               + self.getAncientObject().toString())
               
    def enlarge(self, r):
        self.__radius += r
    def area(self):
        return self.__radius * self.__radius * self.__pi() - self.getSquare().area()
    def circumference(self):
        return 2 * self.__radius * self.__pi()