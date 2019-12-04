#!/usr/bin/python

# Mouth.py

class Mouth:
    ############################
    # Helping function
    ############################
    def __trace(self, s):
        print(s)

    ############################
    # Manager function
    ############################
    # Including a default constructor
    def __init__(self, w, h):
        self.__width = w
        self.__height = h
    def __del__(self):
        pass

    ############################
    # Access function
    ############################
    def getWidth(self):
        return self.__width
    def setWidth(self, w):
        self.__width = w
    def getHeight(self):
        return self.__height
    def setWidth(self, h):
        self.__height = h
    def isBig(self):
        return self.__height > 5 and self.__width > 10
    def isClose(self):
        return self.__height == 1

    ############################
    # Implementor function
    ############################
    def toString(self):
       return ("Height = " + str(self.__height) + " Width = " + str(self.__width))
    def close(self):
        self.__height = 1