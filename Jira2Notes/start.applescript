tell application "Google Chrome"
	set x to (URL of active tab of first window as text)
end tell

do shell script "/Users/kerem/Dropbox/Software/Kerem/Development/Python\\ Library/Jira2Notes/venv/bin/python /Users/kerem/Dropbox/Software/Kerem/Development/Python\\ Library/Jira2Notes/j2n.py " & x