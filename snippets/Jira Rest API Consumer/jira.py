import issue
import requests

class Jira():

    __JIRA_REST_API_PREFIX = "/rest/api/2/search?jql=issuekey="
    __JIRA_REST_API_SUFFIX = "startAt=0&expand=names,renderedFields,schema,transitions,operations,editmeta,changelog&maxResults=1"

    __issue_cache = {}
    __password = ""
    __url = ""
    __username = ""

    def __init__(self, url:str, username:str, password:str):
        self.__url = url
        self.__username = username
        self.__password = password

    def __read_issue_from_server(self, issue_key:str):

        # ---Ensure that we don't have this issue yet-----

        if issue_key in self.__issue_cache:
            return

        # ---Read issue from Jira-----

        url = self.__url + self.__JIRA_REST_API_PREFIX + issue_key + "&" + self.__JIRA_REST_API_SUFFIX
        resp = requests.get(url, auth=(self.__username, self.__password))

        # ---Add issue to cache-----

        json = resp.json()
        json_issue_list = json["issues"]
        json_issue = json_issue_list[0]

        new_issue = issue.Issue()
        new_issue.key = json_issue["key"]
        new_issue.summary = json_issue["fields"]["summary"]
        self.__issue_cache[issue_key] = new_issue

    def get_issue(self, issue_key:str) -> issue.Issue:
        self.__read_issue_from_server(issue_key)
        return self.__issue_cache[issue_key]


