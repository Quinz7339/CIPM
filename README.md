# CIPM
Password manager with cyber education and awareness components. Heavily inspired by KeePassXC but developed using the Qt(Python) GUI framework.


## Working environment
Python -> version 3.11.1 
<br>PyQt6 -> version 6.4.2
<br>Argon2-cffi-bindings -> version 21.3.0


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

## To-do
- main.py --> ensure initializing of resources 
- main.py --> include a requirement.txt to enable users to install required libraries
- readme.md --> include an installation guide
~~- design UI for database unlocking (unlockdb)~~
- database.py --> call (unlockdb).ui and close original window
- database.py --> decrypt db to be sent to interface.py 
~~- password.py --> decryptor~~
- dashboard aka main interface
~~- load credentials dynamically into QTable~~ (done semi dynamically)
- track user selected credential, prompt info into the existing fields
- if any fields are changed upon clicking "Confirm", update the dictionary
- if nothing is changed, set the "Confirm" button to be disabled
- add password generating function
- add show/hide password function
- manager.py --> Add Credential and be reflected in table
- manager.py --> fetch favicon based on entered domain
- manager.py --> Edit Credential and be reflected in table
~~- figure out whether when self.close is called, dashboard function can be called or not~~

- extension: rss news site
- extension: password integration
- extension: security tips (sendiri generate tips)
- extension: malicious link detection (either thru webpage signature or virustotal)