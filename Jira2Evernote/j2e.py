from config import Config
from evernote_manager import EvernoteManager
from jira_manager import JiraManager
import sys

desired_issue = sys.argv[1]
#desired_issue="VOL-6281"

my_config = Config()
my_jira_manager = JiraManager(my_config)
my_evernote_manager = EvernoteManager(my_config)

issue = my_jira_manager.get_issue(desired_issue)
my_evernote_manager.create_note(issue, my_jira_manager)

