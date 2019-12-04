class AncientObject:
    ############################
    # Helping function
    ############################
    def __trace(self, s):
        print(s)

    ############################
    # Manager function
    ############################
    # Including a default contrutctor
    def __init__(self, a, metal):
        self.__age = a
        self.__metal = metal
    def __del__(self):
        pass

    ############################
    # Access function
    ############################
    def getAge(self):
        return self.__age
    def setAge(self, a):
        self.__age = a
    def getMetal(self):
        return self.__metal
    def setMetal(self, metal):
        self.__metal = metal
    def isOld(self):
        return self.__age > 1000
    def isDestroyed(self):
        return self.__age == -1

    ############################
    # Implementor function
    ############################
    def toString(self):
        return(self.getMetal().toString() + "\n" \
               + "Age= " +  str(self.__age))
               
    def destroy(self):
        self.__age = -1