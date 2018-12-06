import sys
import config
from jira_manager import JiraManager
from temp_file import TempFile
from subprocess import call
import os


##############################
# Initialization
##############################

my_config = config.Config()

##############################
# Read issue from Jira
##############################

url = sys.argv[1]
my_jira = JiraManager(my_config)
issue = my_jira.get_issue_by_url(url)

##############################
# Download temp file
##############################

my_temp_file = TempFile(my_config, my_jira)
my_temp_file.write_file(issue, url)

##############################
# Create new Apple Note
##############################

path = os.path.dirname(os.path.abspath(__file__)).replace(" ", "\ ")
path = os.path.join(path, "tmp2note.app")
cmd = "open " + path
call(["/bin/bash", "-c", cmd])
