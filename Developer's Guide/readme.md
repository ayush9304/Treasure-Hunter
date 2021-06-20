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
      
      <img src="https://i.ibb.co/THkmfVP/python-installer.png" alt="python-installer" border="0">
      
- _Step 2_: **Install OpenCV for Python**
    - Open Command Prompt
    - Type in the following command: ``` pip install opencv-python ``` and press \<enter\> key
    - This will install OpenCV for Python
- _Step 3_: **Install VSCode**
    - Goto [https://code.visualstudio.com/Download](https://code.visualstudio.com/Download) and download VSCode installer for windows.
    - Run the installer to install it.
    - Make sure to check all four checkboxes (see image)

      <img src="https://i.ibb.co/qkTVTbc/vscode-installer.png" alt="vscode-installer" border="0">
    - After Installation, Open VSCode and goto *Extension* Tab and search for Python and click the first result which is developed by Microsoft (see image below) and click install
    
      <a href="https://imgbb.com/"><img src="https://i.ibb.co/KbgdMLN/image.png" alt="image" border="0"></a><br /><a target='_blank' href='https://imgbb.com/'>upload pictures free</a>
     
    - Again search for C/C++ and click first result which is developed by Microsoft (see image above) and click install
- _Step 4_: **Install MinGW C/C++ Compiler**
    - Follow [this YouTube Tutorial](https://www.youtube.com/watch?v=sXW2VLrQ3Bs) to install MinGW Compiler.


### MacOS

- _Step 1_: **Install Python**
    - Goto [https://www.python.org/downloads/](https://www.python.org/downloads/) of the official Python website.
    - Download the python installer for macOS and install it.
- _Step 2_: **Install OpenCV for Python**
    - Open Terminal
    - Type in the following command: ``` pip install opencv-python ``` and press \<enter\> key
    - This will install OpenCV for Python
- _Step 2_: **Install VSCode**
    - Goto [https://code.visualstudio.com/Download](https://code.visualstudio.com/Download) and download VSCode installer for macOS.
    - Run the installer to install it.
    - After Installation, Follow the ***4th & 5th point for Installing VSCode in Windows*** section
- _Step 3_: **Install MinGW C/C++ Compiler**
    - Goto [https://brew.sh](https://brew.sh) and copy the link (see image), paste it in the terminal and run it to install Homebrew Package manager.
    
      <img src="https://i.ibb.co/jHC8xCz/mac-mingw.png" alt="mac-mingw" border="0">
      
    - Then type the following command ```brew install mingw-w64``` in the terminal and press \<enter\> key to install MinGW C/C++ Compiler.



## File Structure

   - `maze` - Directory in which maze files are stored
   - `mazeSolution` - Directory in which solutions of maze puzzles will be stored
        - `bfs` - Directory in which solutions of maze puzzles solved using **BFS algorithm** will be stored
        - `dfs` - Directory in which solutions of maze puzzles solved using **DFS algorithm** will be stored
   - `.gitignore` - File that contains names of directories, files & file types that will not be uploaded to github
   - `README.md` - File that introduces the project to viewers
   - `bfs.cpp` - C++ program that solves the maze puzzle using **BFS algorithm**
   - `dfs.cpp` - C++ program that solves the maze puzzle using **DFS algorithm**
   - `displayImage.py` - Python program to show the graphical representation of maze
   - `displayParameters.py` - Python program that contains various parameters on how to show the maze
   - `launcher.cmd` - Batch file to run this application on **Windows OS**<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&emsp;&emsp;&emsp;&emsp; _It takes one argument 'filename' of the maze that we want to solve which is inside ```maze``` directory_
   - `launcher_mac.command` - Shell script to run this application on **macOS**<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&emsp;&emsp;&emsp;&emsp; _It takes one argument 'filename' of the maze that we want to solve which is inside ```maze``` directory_
   - `test.cpp` - It's just a test file. **NO USE**  in this project


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
        - Type `launcher.cmd <maze_filename>` (e.g, `launcher.cmd maze1.txt`)
   - _For macOS_: 
        - Open Terminal, navigate to project directory using `cd` command
        - Type `chmod +x launcher_mac.command` to give the script file permission to run
        - Type `launcher_mac.command <maze_filename>` (e.g, `launcher_mac.command maze1.txt`)
