# CIPM
Password manager with cyber education and awareness components. Heavily inspired by KeePassXC but developed using the Qt(Python) GUI framework.
![Landing Page](https://github.com/Quinz7339/CIPM/blob/master/Images/Main%20Landing%20Page.png)
![Main Manager Interface](https://github.com/Quinz7339/CIPM/blob/master/Images/Main%20Password%20Manager%20Interface.png)

## Getting started
### Prerequisites
##### Ensure Python is installed. The running version is 3.11.1
Install the latest version [here](https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe).

### Installation
To install the application to your system, you can either download or clone the repo using the command as shown:
```bash
git clone https://github.com/Quinz7339/CIPM.git
```
Then install the required libraries:
```bash
pip3 install requirements.txt 
```

### To use
Change the working directory to the cloned repo file location.
```bash
cd C:\Users\<username>\CIPM\main.py
```
Execute the main program.
```bash
python3 main.py
```


## External references/Lessons Learnt Register

### To Refactor/Rename files
1. Change the original file name in <projectname>.pyproject to the new file name.
2. Change the original file name in <projectname>.pyproject.user to the new file name.
As of 13/02/2023, there is no support from QtCreator to automate the refactoring process with a single click. One would need to rename the filenames manually. Refer:
[Stack Overflow](https://stackoverflow.com/questions/5528134/how-can-files-and-classes-be-renamed-in-qt-creator)


### Links to references
Markdown Cheatsheet [MarkDownGuide](https://www.markdownguide.org/cheat-sheet/)
<br>Playlist/Video to get started [Youtube](https://www.youtube.com/playlist?list=PL3JVwFmb_BnSOj_OtnKlsc2c7Jcs6boyB)
<br>Argon2 [Repo](https://github.com/p-h-c/phc-winner-argon2#bindings)
<br> Visual C++ 14.0 to build Argon2 Library in case argon2 is unusable [Ms Answers](https://answers.microsoft.com/en-us/windows/forum/all/microsoft-visual-c-140/6f0726e2-6c32-4719-9fe5-aa68b5ad8e6d)
