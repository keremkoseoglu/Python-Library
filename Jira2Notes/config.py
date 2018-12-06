import json
import os

class Config:

    _CONFIG_FILE = "/Users/kerem/Dropbox/etc/config/jira2notes.txt"

    jira_base_url = ""
    jira_username = ""
    jira_password = ""

    mac_tmp_file = ""

    note_comment_count = 0

    def __init__(self):

        # Read text file
        script_dir = os.path.dirname(__file__)
        config_path = os.path.join(script_dir, self._CONFIG_FILE)
        txt_file = open(config_path, "r")
        txt_content = txt_file.read()
        txt_file.close()
        json_data = json.loads(txt_content)

        # Parse contents
        self.jira_base_url = json_data["config"]["jira"]["base_url"]
        self.jira_username = json_data["config"]["jira"]["username"]
        self.jira_password = json_data["config"]["jira"]["password"]

        self.mac_tmp_file = json_data["config"]["mac"]["tmp_file"]
        self.note_comment_count = int(json_data["config"]["note"]["comment_count"])
