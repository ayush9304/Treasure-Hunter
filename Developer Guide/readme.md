# Developer's Guide

- [Environment Setup](#environment-setup)
    - [Windows](#Windows)
    - [MacOS](#MacOS)
- [Development](#Development)

## Environment Setup
### Windows

- _Step 1_:  **Install Python**
    - Goto [https://www.python.org/downloads/](https://www.python.org/downloads/) of the official Python website.
    - Download the python installer for Windows and run it.
    - Make sure to check the "_Add Python 3.x to PATH_" checkbox (see image)
      
      <a href="https://imgbb.com/"><img src="https://i.ibb.co/THkmfVP/python-installer.png" alt="python-installer" border="0"></a>
      
- _Step 2_: **Install OpenCV for Python**
    - Open Command Prompt
    - Type in the following command: ``` pip install opencv-python ``` and press \<enter\> key
    - This will install OpenCV for Python
- _Step 3_: **Install VSCode**
    - Goto [https://code.visualstudio.com/Download](https://code.visualstudio.com/Download) and download VSCode installer for windows.
    - Run the installer to install it.
    - Make sure to check all four checkboxes (see image)

      <a href="https://imgbb.com/"><img src="https://i.ibb.co/qkTVTbc/vscode-installer.png" alt="vscode-installer" border="0"></a>
      
    - After Installation, Open VSCode and goto *Extension* Tab and search for Python and click the first result which is developed by Microsoft (see image below) and click install
    
      <a href="https://imgbb.com/"><img src="https://i.ibb.co/M6JcjKW/vscode-python.png" alt="vscode-python" border="0"></a> <a href="https://imgbb.com/"><img src="https://i.ibb.co/y8dD13m/vscode-cpp.png" alt="vscode-cpp" border="0"></a><br />
     
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
    
      <a href="https://imgbb.com/"><img src="https://i.ibb.co/jHC8xCz/mac-mingw.png" alt="mac-mingw" border="0"></a>
      
    - Then type the following command ```brew install mingw-w64``` in the terminal and press \<enter\> key to install MinGW C/C++ Compiler.



## Development
