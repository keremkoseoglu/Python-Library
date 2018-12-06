on getNoteContents()
	set fileHandle to open for access "/Users/Kerem/Downloads/j2n.txt"
	set theLines to paragraphs of (read fileHandle as Çclass utf8È)
	close access fileHandle
	set theLines to rest of theLines
	
	set saveTID to text item delimiters
	set text item delimiters to ", "
	set ret to theLines as text
	set text item delimiters to saveTID
	
	return ret
end getNoteContents

on getNoteTitle()
	set fileHandle to open for access "/Users/Kerem/Downloads/j2n.txt"
	set theLines to first paragraph of (read fileHandle as Çclass utf8È)
	close access fileHandle
	return theLines
end getNoteTitle

set title to getNoteTitle()
set content to getNoteContents()

tell application "Notes"
	tell account "iCloud"
		make new note at folder "ecz" with properties {name:title, body:content}
	end tell
end tell