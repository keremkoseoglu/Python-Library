import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from gui.calc_event import CalcEvent
from lib.calculator import Calculator

class ButtonRow(GridLayout):

    __num1 = None
    __num2 = None
    __num3 = None
    __oper = None
    __event = None

    def __init__(self, **kwargs):
        super(ButtonRow, self).__init__(**kwargs)

        self.__num1 = Button()
        self.__num2 = Button()
        self.__num3 = Button()
        self.__oper = Button()

        self.__num1.bind(on_press=self.button1_click)
        self.__num2.bind(on_press=self.button2_click)
        self.__num3.bind(on_press=self.button3_click)
        self.__oper.bind(on_press=self.oper_click)

        self.cols = 4
        self.add_widget(self.__num1)
        self.add_widget(self.__num2)
        self.add_widget(self.__num3)
        self.add_widget(self.__oper)

        self.__event = CalcEvent()

    def button1_click(self, instance):
        self.__event.button_clicked(self.__num1.text)

    def button2_click(self, instance):
        self.__event.button_clicked(self.__num2.text)

    def button3_click(self, instance):
        self.__event.button_clicked(self.__num3.text)

    def oper_click(self, instance):
        self.__event.button_clicked(self.__oper.text)

    def add_event_listener(self, handler):
        self.__event.add_handler(handler)

    def set_button_text(self, btn: int, text: str):
        if btn == 1: self.__num1.text = text
        if btn == 2: self.__num2.text = text
        if btn == 3: self.__num3.text = text
        if btn == 4: self.__oper.text = text

    def set_button_texts(self, text1: str, text2: str, text3: str, text4: str):
        self.set_button_text(1, text1)
        self.set_button_text(2, text2)
        self.set_button_text(3, text3)
        self.set_button_text(4, text4)


class Face(GridLayout):

    __button_row_1 = ButtonRow()
    __button_row_2 = ButtonRow()
    __button_row_3 = ButtonRow()
    __button_row_4 = ButtonRow()
    __screen = Label()
    __calc = Calculator()
    __number = ""

    def __init__(self, **kwargs):
        super(Face, self).__init__(**kwargs)

        self.__button_row_1.set_button_texts("1", "2", "3", "+")
        self.__button_row_2.set_button_texts("4", "5", "6", "-")
        self.__button_row_3.set_button_texts("7", "8", "9", "x")
        self.__button_row_4.set_button_texts("C", "0", "C", "/")

        self.__button_row_1.add_event_listener(self.__handle_button_click)
        self.__button_row_2.add_event_listener(self.__handle_button_click)
        self.__button_row_3.add_event_listener(self.__handle_button_click)
        self.__button_row_4.add_event_listener(self.__handle_button_click)

        self.__screen.font_size = "100dp"

        self.cols = 1
        self.add_widget(self.__screen)
        self.add_widget(self.__button_row_1)
        self.add_widget(self.__button_row_2)
        self.add_widget(self.__button_row_3)
        self.add_widget(self.__button_row_4)

    def __handle_button_click(self, text:str):
        if text == "1" \
            or text == "2" \
            or text == "3" \
            or text == "4" \
            or text == "5" \
            or text == "6" \
            or text == "7" \
            or text == "8" \
            or text == "9" \
            or text == "0":
            self.__number = self.__number + text
            self.__screen.text = self.__number
        elif text == "+" \
            or text == "-" \
            or text == "x" \
            or text == "/":
            self.__calc.set_number(int(self.__number))
            self.__calc.set_operation(text)
            self.__number = ""
            self.__screen.text = str(self.__calc.get_result())
        elif text == "C":
            self.__number = ""
            self.__screen.text = ""
            self.__calc.clear()


class CalcApp(App):

    def build(self):
        return Face()