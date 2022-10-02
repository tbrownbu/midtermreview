import weakref


class Pet:
    def __init__(self, type, weight, limbs, age, name):
        self.__type = type
        self.__weight = weight
        self.__limbs = limbs
        self.__age = age
        self.__name = name

    def getType(self):
        return self.__type
    
    def getWeight(self):
        return self.__weight

    def getLimbs(self):
        return self.__limbs

    def getAge(self):
        return self.__age

    def getName(self):
        return self.__name

    def move(self,num):
        self.__distance = self.__limbs * num

    def getMove(self):
        return self.__distance