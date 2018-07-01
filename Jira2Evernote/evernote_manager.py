from config import Config
from evernote.api.client import EvernoteClient
from evernote.edam.type import ttypes
from jira.resources import Issue
from jira_manager import JiraManager

class EvernoteManager:

    def __init__(self, Config):
        # Initialization
        self._config = Config
        self._client = EvernoteClient(token=self._config.evernote_token, sandbox=False)
        self._user_store = self._client.get_user_store()
        self._note_store = self._client.get_note_store()

        # Find target notebook
        notebooks = self._note_store.listNotebooks()
        for notebook in notebooks:
            if notebook.name == self._config.evernote_notebook:
                self._notebook = notebook
                break

    def _get_safe_text(self, unsafe_text: str) -> str:
        output = unsafe_text
        output = output.replace("&", "+")
        return output

    def create_note(self, issue: Issue, jira_man: JiraManager):

        # ______________________________
        # Note object

        note = ttypes.Note()
        note.notebookGuid = self._notebook.guid

        # ______________________________
        # Attributes

        issue_url = jira_man.get_url(issue.key)
        note.attributes = ttypes.NoteAttributes(sourceURL=issue_url)
        note.tagNames = self._config.evernote_tags

        # ______________________________
        # Title

        try:
            note.title = issue.fields.parent.key + " - " + self._get_safe_text(issue.fields.summary)
        except:
            note.title = issue.key + " - " + self._get_safe_text(issue.fields.summary)

        # ______________________________
        # Body

        # Header

        body = '<?xml version="1.0" encoding="UTF-8"?>'
        body += '<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
        body += '<en-note>'

        # URL

        body += 'Madde: <a href="' + issue_url + '">' + issue_url + '</a><br/>'
        try:
            parent_url = jira_man.get_url(issue.fields.parent.key)
            body += 'Üst madde: <a href="' + parent_url + '">' + parent_url + '</a><br/>'
        except:
            pass

        # Summary

        summary = ""

        try:
            summary = self._get_safe_text(issue.fields.summary)
        except:
            pass

        try:
            summary2 = self._get_safe_text(issue.fields.description)
            summary += "<br/><br/>" + summary2
        except:
            pass

        body += '<br/>' + summary + '<br/><br/>'

        # To do

        body += '<hr/><b>İşler</b><br/><br/>'
        body += '<en-todo/>Jira''yı ilerlet<br/><br/>'
        body += '<en-todo/>Geliştirme<br/><br/>'
        body += '<en-todo/>EPC + Task Release<br/><br/>'
        body += '<en-todo/>Teknik test<br/><br/>'
        body += '<en-todo/>Jira''yı ilerlet ve yorum yaz<br/><br/>'

        # Comments

        for i in range(self._config.evernote_comment_count):
            comment_idx = issue.fields.comment.total - 1 - i
            if comment_idx < 0:
                break
            if i == 0:
                body += '<hr/><b>Son yorumlar</b><br/><br/>'
            current_comment = issue.fields.comment.comments[comment_idx]
            comment_body = current_comment.body.replace("\r\n", "<br/>")
            body += '<b>' + current_comment.author.displayName + ", " + current_comment.created + ':</b> <br/>' + comment_body + "<br/><br/>"

        # Bottom

        body += '<br/><hr/><br/>'

        # Finish

        body += '</en-note>'
        note.content = body

        # ______________________________
        # Flush

        self._note_store.createNote(note)
