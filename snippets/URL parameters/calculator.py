class Calculator:

    __result = 0

    def __init__(self):
        pass

    def add(self, i: int):
        self.__result = self.__result + i

    def subtract(self, i: int):
        self.__result = self.__result - i

    def getResult(self):
        return self.__result
