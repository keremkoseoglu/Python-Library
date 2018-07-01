class CalcEvent():

    __handlers = None

    def __init__(self):
        self.__handlers = []

    def add_handler(self, handler):
        self.__handlers.append(handler)

    def button_clicked(self, text: str):
        for handler in self.__handlers:
            handler(text)