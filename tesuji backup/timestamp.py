import datetime

class TimeStamp():

    __ZERO = "0"

    __now = None
    __time_stamp = ""
    __year = ""

    def __init__(self):
        self.__now = datetime.datetime.now()

    def __build_time_stamp_lazy(self):
        if not self.__time_stamp == "":
            return
        self.__build_year_lazy()
        self.__time_stamp = \
            self.__year \
            + self.__get_two_digit_str(self.__now.month) \
            + self.__get_two_digit_str(self.__now.day) \
            + self.__get_two_digit_str(self.__now.hour) \
            + self.__get_two_digit_str(self.__now.minute) \
            + self.__get_two_digit_str(self.__now.second)

    def __build_year_lazy(self):
        if not self.__year == "":
            return
        self.__year = str(self.__now.year)

    def __get_two_digit_str(self, timepiece):
        output = str(timepiece)
        while len(output) < 2 :
            output = self.__ZERO + output
        return output

    def get_time_stamp(self):
        self.__build_time_stamp_lazy()
        return self.__time_stamp

    def get_year(self):
        self.__build_year_lazy()
        return self.__year