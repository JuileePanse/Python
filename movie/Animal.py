class Animal:
    ############################
    # Helping function
    ############################
    def __trace(self, s):
        print(s)

    ############################
    # Manager function
    ############################
    # Including a default construtctor
    def __init__(self, l):
        self.__legs = l
    def __del__(self):
        pass

    ############################
    # Access function
    ############################
    def getLegs(self):
        return self.__legs
    def setLegs(self, l):
        self.__legs = l
    def isDisable(self):
        return self.__legs == 0

    ############################
    # Implementor function
    ############################
    def toString(self):
       return ("Legs = " + str(self.__legs))
    def removeLegs(self, l):
        self.__legs -= l