import os, shutil, timestamp

class Backup():

    __DEBUT_FILE_NAME = "tesuji"
    __EXTENSION = "xlsm"
    __SOURCE_PATH = "/Users/Kerem/Dropbox/Software/Tesuji/Tesuji/Billing/"
    __ARCHIVE_FOLDER = "Archive"

    __first_stop = ""
    __source_file_name = ""
    __source_file_path = ""
    __target_file_name = ""
    __time_stamp = None

    def __init__(self):
        pass

    def __build_source_paths_lazy(self):

        if self.__source_file_name != "":
            return

        self.__source_file_name = \
            self.__DEBUT_FILE_NAME \
            + "." \
            + self.__EXTENSION

        self.__source_file_path = \
            self.__SOURCE_PATH \
            + self.__source_file_name

    def __build_target_file_name(self):

        self.__target_file_name = \
            self.__DEBUT_FILE_NAME \
            + " " \
            + self.__time_stamp.get_time_stamp() \
            + "." \
            + self.__EXTENSION

    def __move_file_to_destination(self):

        target_folder = \
            self.__SOURCE_PATH \
            + self.__ARCHIVE_FOLDER \
            + "/" \
            + self.__time_stamp.get_year()

        target_path = target_folder + "/" + self.__target_file_name

        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        shutil.move(self.__first_stop, target_path)

    def __move_file_to_first_stop(self):
        self.__first_stop = self.__SOURCE_PATH + self.__target_file_name
        shutil.copyfile(self.__source_file_path, self.__first_stop)

    def run_backup(self):

        self.__time_stamp = timestamp.TimeStamp()
        self.__build_source_paths_lazy()
        self.__build_target_file_name()
        self.__move_file_to_first_stop()
        self.__move_file_to_destination()



