ECHO OFF

IF [%1] EQU [] GOTO :error
IF NOT EXIST maze/%1 GOTO :filedoesnotexist

py displayImage.py maze/%1

IF EXIST dfs.cpp (
    g++ -o dfs dfs.cpp
    dfs maze/%1
    py displayImage.py maze/%1 DFS
)

IF EXIST bfs.cpp (
    g++ -o bfs bfs.cpp
    bfs maze/%1
    py displayImage.py maze/%1 BFS
)

IF EXIST mazeSolution/%1 (
    py displayImage.py mazeSolution/%1
)
GOTO :finish

:noargument
ECHO WARNING!!! Please provide the maze filename as argument
GOTO :finish

:filedoesnotexist
ECHO WARNING!!! File does not exists.

:finish