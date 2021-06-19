ECHO OFF

IF [%1] EQU [] GOTO :noargument
IF NOT EXIST maze/%1 GOTO :filedoesnotexist

ECHO Displaying Maze
py displayImage.py maze/%1
ECHO Running algorithms to find the path to the Tresure ...


IF EXIST dfs.cpp (
    g++ -o dfs dfs.cpp
    dfs maze/%1
    IF EXIST mazeSolution/dfs/%1 (
        py displayImage.py mazeSolution/dfs/%1 DFS
        GOTO :bfs
    )
    ECHO WARNING!!! Solution File not found
    ECHO HINT: "Make sure to save the solution matrix of maze puzzle at location 'mazeSolution/dfs/' with the same name (in this case '%1') in the C++ program"
)

:bfs
IF EXIST bfs.cpp (
    g++ -o bfs bfs.cpp
    bfs maze/%1
    IF EXIST mazeSolution/bfs/%1 (
        py displayImage.py mazeSolution/bfs/%1 BFS
        GOTO :next
    )
    ECHO WARNING!!! Solution File not found
    ECHO HINT: "Make sure to save the solution matrix of maze puzzle at location 'mazeSolution/bfs/' with the same name (in this case '%1') in the C++ program"
)

:next

GOTO :finish

:noargument
ECHO WARNING!!! Please provide the maze filename as argument
GOTO :finish

:filedoesnotexist
ECHO WARNING!!! File does not exists.

:finish