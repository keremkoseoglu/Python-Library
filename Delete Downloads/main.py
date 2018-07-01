import os, shutil

_FOLDER = "/Users/kerem/Downloads"

for current_item in os.listdir(_FOLDER):
    current_path = os.path.join(_FOLDER, current_item)
    try:
        if os.path.isfile(current_path):
            os.unlink(current_path)
        elif os.path.isdir(current_path):
            shutil.rmtree(current_path)
    except Exception as e:
        print(e)