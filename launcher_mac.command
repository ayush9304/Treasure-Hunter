#! /bin/bash

if [ -z "$1" ]
then
    echo "WARNING!!! Please provide the maze filename as argument"
else
    if [ -f "maze/$1" ]
    then
        echo "Displaying Maze"
        python3 displayImage.py maze/$1
        echo "Running algorithms to find the path to the Treasure ..."

        if [ -f "bfs.cpp" ]
        then
            g++ -o bfs bfs.cpp
            ./bfs $1
            if [ -f "mazeSolution/bfs/$1" ]
            then
                python3 displayImage.py mazeSolution/bfs/$1 BFS
            else
                echo "WARNING!!! Solution File not found"
                echo "HINT: Make sure to save the solution matrix of maze puzzle at location 'mazeSolution/bfs/' with the same name (in this case '$1') in the C++ program"
            fi
        fi
    else
        echo "WARNING!!! File does not exists."
    fi
fi
