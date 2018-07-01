from abc import ABC, abstractmethod

class AbstractClass(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def get_text(self) -> str:
        pass