from pack2.abstract_class import AbstractClass

class ConcreteClass(AbstractClass):

    def get_text(self) -> str:
        return "This is pack2.ConcreteClass speaking"