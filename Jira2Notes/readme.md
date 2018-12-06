# Jira to Notes

This Mac program will read the current Jira issue on the active Chrome window, and create a corresponding Apple Notes item.

## How it works

Step 1) You start the process by executing **start.applescript** (the generated .app, actually). This file gets the issue number from the URL field of Chrome (using AppleScript),
and passes the value to **j2n.py** .

Step 2) **j2n.py** (Python) connects to your Jira system, reads the issue details and creates a temporary file. Then, it executes **tmp2note.app** .

Step 3) **tmp2note.applescript** reads the temporary file, and creates a new Apple Notes item over AppleScript.

## Configuration

To use the program in your own system, the following steps should be taken.

- Put all of the files to a nice directory.
- Edit **start.applescript** so it points to the correct directory, and export it as an **start.app** (or any name you like). 
- Edit **config.py** so it points to the correct configuration file. A sample file is provided as jira2notes.txt.
- Edit your configuration file (initially named as **jira2notes.txt** ) so it contains correct values.
- Edit **tmp2note.applescript** so it points to the correct temporary folder name in **jira2notes.txt** .

To start the program, simply execute **start.app** (or however you named this file).

## Optional

To disable Mac security warnings, you should enable the script files for accessibility & file system control on your system settings.