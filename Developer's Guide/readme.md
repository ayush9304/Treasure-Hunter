# Developer's Guide

- [Environment Setup](#environment-setup)
    - [Windows](#Windows)
    - [MacOS](#MacOS)
- [File Structure](#file-structure)
- [Contributing Guide](#contributing-guide)
- [How to run](#how-to-run)

## Environment Setup
### Windows

- _Step 1_:  **Install Python**
    - Goto [https://www.python.org/downloads/](https://www.python.org/downloads/) of the official Python website
    - Download the python installer for Windows and run it
    - Make sure to check the "_Add Python 3.x to PATH_" checkbox (see image)
      
      <img src="https://i.ibb.co/2qL141J/python-installer.png" alt="python-installer" border="0">
      
- _Step 2_: **Install Python dependencies**
    - Open Command Prompt
    - Type in the following command: ``` pip3 install -r requirements.txt ``` and press \<enter\> key
    - This will install all the Python dependencies for this project
- _Step 3_: **Install VSCode**
    - Goto [https://code.visualstudio.com/Download](https://code.visualstudio.com/Download) and download VSCode installer for windows.
    - Run the installer to install it.
    - Make sure to check all four checkboxes (see image)

      <img src="https://i.ibb.co/qkTVTbc/vscode-installer.png" alt="vscode-installer" border="0">
    - After Installation, Open VSCode and goto *Extension* Tab and search for Python and click the first result which is developed by Microsoft (see image below) and click install
    
        <img src="https://i.ibb.co/9yZDK6b/vscode-python.png" alt="vscode-python" border="0">


### MacOS

- _Step 1_: **Install Python**
    - Goto [https://www.python.org/downloads/](https://www.python.org/downloads/) of the official Python website.
    - Download the python installer for macOS and install it.
- _Step 2_: **Install Python dependencies**
    - Open Terminal
    - Type in the following command: ``` pip3 install -r requirements.txt ``` and press \<enter\> key
    - This will install all the Python dependencies for this project
- _Step 4_: **Install VSCode**
    - Goto [https://code.visualstudio.com/Download](https://code.visualstudio.com/Download) and download VSCode installer for macOS.
    - Run the installer to install it.
    - After Installation, Follow the ***4th point for Installing VSCode in Windows*** section



## File Structure

   - `img` - Directory in which image files that are used in this project are stored
   - `.gitignore` - File that contains names of directories, files & file types that will not be uploaded to github
   - `Collaborators.md` - File contains list of all collaborators in this project.
   - `README.md` - File that introduces the project to viewers
   - `bfs.py` - Python program that solves the maze puzzle using **BFS algorithm**
   - `displayImage.py` - Python program to show the graphical representation of maze
   - `displayParameters.py` - Python program that contains various parameters on how to show the maze
   - `mazeGenerator.py` - Python program to generate random maze of give size
   - `requirements.txt` - File that contains list of all Python dependencies
   - `main.py` - Main Python Program to run the application
   - `ui_design.py` - Python file that contains basic structure for Graphical User Interface
   - `ui_design.ui` - Raw XML file for GUI


## Contributing Guide

   - _Step 1_: Download Git from [https://git-scm.com/downloads](https://git-scm.com/downloads) and install it.
   - _Step 2_: Fork this repository by clicking <img src="https://i.ibb.co/PD6HY9s/fork.png" alt="fork" border="0"> button on upper-right corner of the screen in the github repository page
   - _Step 3_: Create new branch with your name (for example, see image)<br/>
        <img src="https://i.ibb.co/yW9NcJB/branch.png" alt="branch" border="0">
   - _Step 4_: Copy the forked repository link (see image)<br/>
        <img src="https://i.ibb.co/85xZTGb/image-1.png" alt="image-1" border="0">
   - _Step 5_: Type in ```git clone <copied_url>``` command in the terminal to clone the forked repository to your local machine.<br/>
        &nbsp;&nbsp;&nbsp;&emsp;&emsp;&emsp; _Replace the <copied_url> in the command with the url of forked repository_
   - _Step 6_: Now open the terminal and navigate to the project folder (In this case directory name will be **Treasure-Hunter**) using `cd` command
   - _Step 7_: Type in the terminal `git checkout <branch_name>` command and press \<enter\>.<br/>
            &nbsp;&nbsp;&nbsp;&nbsp;&emsp;&emsp;&emsp;&emsp; _Replace <branch_name> with the branch you created in step 3_
   - _Step 8_: Then type `code .` and press \<enter\> to open VSCode at this directory location.
   - _Step 9_: Write your code, save it and [run the application](#how-to-run) to see the result.
   - _Step 10_: Then add your changes to commit by typing in the terminal `git add .` command
   - _Step 11_: Now to commit the changes type `git commit -m "<message>"` command<br/>
            &nbsp;&nbsp;&nbsp;&nbsp;&emsp;&emsp;&emsp;&emsp; _Replace the \<message\> in the command with appropriate message (like what changes you did)_
   - _Step 12_: Push the changes in your local repository to remote repository (e.g, GitHub) by typing `git push` command
   - _Step 13_: When you're done with all changes, goto GitHub website, open the forked repository, make a pull request by clicking **Compare & pull request** button (see image)<br/><img src="https://i.ibb.co/JF0m5Jx/pull.png" alt="pull" border="0">
   - _Step 14_: Then write appropriate comment about your changes in the code and click **Create pull request** button


## How to run

   - _For Windows OS_: 
        - Open Command prompt, navigate to project directory using `cd` command
        - Type `py main.py`
   - _For macOS_: 
        - Open Terminal, navigate to project directory using `cd` command
        - Type `python3 ./main.py`
