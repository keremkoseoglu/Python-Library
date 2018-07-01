class Calculator():

    __result = 1

    def __init__(self):
        pass

    def add(self, i):
        self.__result = self.__result + i

    def subtract(self, i):
        self.__result = self.__result - i

    def getResult(self):
        return self.__result

c = Calculator()
c.add(22)
c.subtract(4)

x = c.getResult()
print(x)
