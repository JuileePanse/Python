#!/usr/bin/python

# Eye.py

class Eye:
 ############################
 # Helping function
 ############################
   def __pi(self):
       return 3.1416

 ############################
 # Manager function
 ############################
   def __init__(self, r):
       self.__radius = r
   def __del__(self):
       pass

 ############################
 # Access function
 ############################
   def getRadius(self):
       return self.__radius
   def setRadius(self, r):
       self.__radius = r
   def isSmall(self):
       return self.__radius < 10
   def isClose(self):
       return self.__radius == 1

 ############################
 # Implementor function
 ############################
   def toString(self):
       return ("Radius = " + str(self.__radius))
   def close(self):
       self.__radius = 1;