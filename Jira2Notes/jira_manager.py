from config import Config
from jira import JIRA

class JiraManager:

    _ISSUE_URL_DECORATOR = "/browse/"

    def __init__(self, configuration):
        self._config = configuration

        options = {
            "server": self._config.jira_base_url
        }
        self._jira = JIRA(options, basic_auth=(self._config.jira_username, self._config.jira_password))

    def get_issue(self, issue_key: str):
        issue = self._jira.issue(issue_key)
        return issue

    def get_issue_by_url(self, url: str):
        fragments = url.split("/")
        issue_key = fragments[len(fragments)-1]
        return self.get_issue(issue_key)

    def get_url(self, issue_key: str) -> str:
        return self._config.jira_base_url + self._ISSUE_URL_DECORATOR + issue_key
