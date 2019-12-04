#!/usr/bin/python

# Head.py
from Eye import *
from Nose import *
from Mouth import *

class Head:
    ############################
    # Helping function
    ############################
    def __trace(self, s):
        print(s)

    ############################
    # Manager function
    ############################
    # Including a default constructor
    def __init__(self, h, r, eye1, eye2, nose, mouth):
        self.__numHair = h
        self.__R = r
        self.__left = eye1
        self.__right = eye2
        self.__n = nose
        self.__m = mouth

    def __del__(self):
        pass

    ############################
    # Access function
    ############################
    def getNumHair(self):
        return self.__numHair
    def setNumHair(self, h):
        self.__numHair = h
    def getR(self):
        return self.__R
    def setR(self, r):
        self.__numHair = r
    def getLeft(self):
        return self.__left
    def setLeft(self, eye_left):
        self.__left = eye_left
    def getRight(self):
        return self.__right
    def setRight(self, eye_right):
        self.__right = eye_right
    def setNose(self, nose):
        self.__n = nose
    def getNose(self):
        return self.__n
    def setMouth(self, mouth):
        self.__m = mouth
    def getMouth(self):
        return self.__m
    def isNormal(self):
        return self.getLeft().getRadius() == self.getRight().getRadius()

    ############################
    # Implementor function
    ############################
    def toString(self):
       return ("" + "\n" \
       + "Num Hair = " + "" \
       + str(self. __numHair) + "\n" \
       + 'Head Radius = ' + "" \
       + str(self.__R) + "\n" \
       + "Left Eye" + "  " \
       + self.getLeft().toString() + "\n" \
       + "Right Eye" + "  " \
       + self.getRight().toString() + "\n" \
       + "Nose" + ":  " \
       + self.getNose().toString() + "\n" \
       + "Mouth" + ":  " \
       + self.getMouth().toString())
    def headAche(self):
        return self.getLeft().isClose() and self.getRight().isClose() and self.getMouth().isClose()