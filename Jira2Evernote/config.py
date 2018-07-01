import json, os


class Config:

    _CONFIG_FILE = "/Users/kerem/Dropbox/etc/config/jira2evernote.txt" # Check sample_config.txt

    evernote_comment_count = 0
    evernote_notebook = ""
    evernote_token = ""
    evernote_tags = {}

    jira_base_url = ""
    jira_username = ""
    jira_password = ""

    def __init__(self):

        # Read text file
        script_dir = os.path.dirname(__file__)
        config_path = os.path.join(script_dir, self._CONFIG_FILE)
        txt_file = open(config_path, "r")
        txt_content = txt_file.read()
        txt_file.close()
        json_data = json.loads(txt_content)

        # Parse contents
        self.evernote_comment_count = int(json_data["config"]["evernote"]["comment_count"])
        self.evernote_token = json_data["config"]["evernote"]["token"]
        self.evernote_notebook = json_data["config"]["evernote"]["notebook"]
        self.evernote_tags = json_data["config"]["evernote"]["tags"]

        self.jira_base_url = json_data["config"]["jira"]["base_url"]
        self.jira_username = json_data["config"]["jira"]["username"]
        self.jira_password = json_data["config"]["jira"]["password"]
