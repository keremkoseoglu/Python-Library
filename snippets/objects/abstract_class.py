from abc import ABC, abstractmethod

class MyAbstract(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def doSomething(self):
        pass
    

class MyClass1(MyAbstract):

    def __init__(self):
        pass
    
    def doSomething(self):
        print("abstract method")

    def doSomethingElse(self):
        print("abstract method 2")

c1 = MyClass1()
c1.doSomething()
c1.doSomethingElse()
