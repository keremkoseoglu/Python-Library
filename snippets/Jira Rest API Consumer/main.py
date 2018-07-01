import jira

__URL = "http://jira.example.com"
__USER = "my_user"
__PASS = "my_pass"
__ISSUE = "VOL-1234"

my_jira = jira.Jira(__URL, __USER, __PASS)
my_issue = my_jira.get_issue(__ISSUE)
print(my_issue.summary)