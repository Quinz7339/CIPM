# CIPM
Password manager with cyber education and awareness components. Heavily inspired by KeePassXC but developed using the Qt(Python) GUI framework.


## Working environment
Python -> version 3.11.1 
<br>PyQt6 -> version 6.4.2
<br>Argon2-cffi-bindings -> version 21.3.0
<br>requests


## To Refactor/Rename files
1. Change the original file name in <projectname>.pyproject to the new file name.
2. Change the original file name in <projectname>.pyproject.user to the new file name.
As of 13/02/2023, there is no support from QtCreator to automate the refactoring process with a single click. One would need to rename the filenames manually. Refer:
[Stack Overflow](https://stackoverflow.com/questions/5528134/how-can-files-and-classes-be-renamed-in-qt-creator)


## External References
Markdown [Link](https://www.markdownguide.org/cheat-sheet/)
<br>Playlist/Video to get started [Youtube](https://www.youtube.com/playlist?list=PL3JVwFmb_BnSOj_OtnKlsc2c7Jcs6boyB)
<br>Argon2 [Repo](https://github.com/p-h-c/phc-winner-argon2#bindings)
<br> Visual C++ 14.0 to build Argon2 Library [Link](https://answers.microsoft.com/en-us/windows/forum/all/microsoft-visual-c-140/6f0726e2-6c32-4719-9fe5-aa68b5ad8e6d)

## Notable obstacles
1. File encryption
2. QPushButton.disconnect() -> causes recursions
3. 


## To-do
- main.py --> ensure initializing of resources 
- main.py --> include a requirement.txt to enable users to install required libraries
- readme.md --> include an installation guide

~~- manager.py (Main) --> visual bug whr new duplicated entries are hidden~~ (solved by using var enumerating the credList for table population instead)
~~- manager.py(Main) --> add show/hide password function on QLabel (line 111)~~
~~- manager.py --> Add Credential and be reflected in table (partially done, has a recursion problem. initialization of button connect might be the issue)~~
~~- manager.py --> fetch favicon based on entered domain~~ (scrapped)
- manager.py --> Edit Credential and be reflected in table
~~- manager.py(Add/Edit) - random password generator ~~
~~- manager.py(Edit) -if any fields are changed upon clicking "Confirm", update the dictionary, update date modified~~
~~- manager.py(Edit) -if nothing is changed, set the "Confirm" button to be disabled~~
~~- manager.py(Setting) - create UI~~
~~- manager.py(Setting) - allow default length of generated password (use slider) --> self.password_length~~
- reflect changes correctly on the local database file
- open file in 'w' mode to overwrite with the currently updated database (do it when then are changes OR at the end of the program execution)



- extension: rss news site
- extension: password integration (extra)
- extension: security tips (sendiri generate tips)
- extension: malicious link detection (either thru webpage signature or virustotal)