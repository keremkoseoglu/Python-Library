from config import Config
import os
from jira_manager import JiraManager

class TempFile:

    def __init__(self, configuration: Config, jira_man: JiraManager):
        self._config = configuration
        self._jira_man = jira_man

    def write_file(self, issue, url):
        f = open(self._config.mac_tmp_file, "w")
        f.write(self._get_body(issue, url))
        f.close()

    def _get_body(self, issue, issue_url) -> str:

        body = ""

        # ______________________________
        # Title

        try:
            body += issue.fields.parent.key + " - " + self._get_safe_text(issue.fields.summary)
        except:
            body += issue.key + " - " + self._get_safe_text(issue.fields.summary)

        body += "\r\n<br><br>"

        # ______________________________
        # Body

        # URL

        try:
            parent_url = self._jira_man.get_url(issue.fields.parent.key)
            body += 'Üst madde: <a href="' + parent_url + '">' + parent_url + '</a><br>'
        except:
            pass
        body += 'Madde: <a href="' + issue_url + '">' + issue_url + '</a><br>'

        # Summary

        summary = ""

        try:
            summary = self._get_safe_text(issue.fields.summary)
        except:
            pass

        try:
            summary2 = self._get_safe_text(issue.fields.description)
            summary += "<br><br>" + summary2
        except:
            pass

        body += '<br>' + summary + '<br><br>'

        # Comments

        for i in range(self._config.note_comment_count):
            comment_idx = issue.fields.comment.total - 1 - i
            if comment_idx < 0:
                break
            if i == 0:
                body += '______________________________<br><br>'
                body += '<b>Son yorumlar</b><br><br>'
            current_comment = issue.fields.comment.comments[comment_idx]
            comment_body = self._get_safe_text(current_comment.body).replace("\r\n", "<br>")
            body += '<b>' + current_comment.author.displayName + ", " + current_comment.created + ':</b> <br>' + comment_body + "<br><br>"

        # Bottom

        body += '______________________________<br><br>'

        # Finish

        return body

    def _get_safe_text(self, unsafe_text: str) -> str:
        output = unsafe_text.replace("<", "&lt;")
        output = output.replace(">", "&lt;")
        return output

