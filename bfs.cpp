#include <iostream>
#include <fstream>
#include <vector>
#include <stdexcept>
#include <iterator>
#include <algorithm>
#include <sstream>

using namespace std;

struct Coordinate{
    int x;
    int y;
};

struct Node{
    Coordinate state;
    Node *previous;
};

class Queue{

    vector<Node*> list;
    int front = 0;
    int last = -1;

public:

    void add(Node *n){
        list.push_back(n);
        last++;
    }

    Node* remove(){
        if(front>last){
            throw underflow_error("Underflow!");}
        else{
            return list[front++];
        }
    }

    bool isEmpty(){
        if(front>last)
            return true;
        else
            return false;
    }

};

class Maze{

public:
    vector<vector<char> > matrix;
    vector<vector<int> > visited;
    int row;
    int column;
    Coordinate start;
    Coordinate goal;
    string filename;

    void load(){
        string fileaddress = "maze/" + filename;
        ifstream file(fileaddress);
        if (!file){
            throw invalid_argument("No file found!");
        }
        string line;

        while (getline(file, line))
        {
            istringstream iss(line);
            vector<char> tmp;

            copy(
                    istream_iterator<char>(iss),
                    istream_iterator<char>(),
                    back_inserter(tmp)
            );
            matrix.push_back(tmp);
        }

        /*for (int i = 0; i < matrix.size(); ++i) {
            cout<<"\n";
            for (int j = 0; j < matrix[i].size(); ++j) {
                cout<<matrix[i][j];
            }
        }*/


        row = matrix.size();
        if(row == 0 || row > 79){throw logic_error("Invalid maze!");}
        column = matrix[0].size();
        if(column == 0 || column > 156){throw logic_error("Invalid maze!");}
        for(int i = 0; i < matrix.size(); i++){
            if(column != matrix[i].size()){throw logic_error("Invalid maze!");}
            vector<int> temp = {};
            for(int j = 0; j < matrix[i].size(); j++){
                if(matrix[i][j] == 'S'){start = {j, i};}
                if(matrix[i][j] == 'D'){goal = {j, i};}
                if(matrix[i][j] == '1'){temp.push_back(2);}
                else{temp.push_back(0);}
            }
            visited.push_back(temp);
        }
    }
    Coordinate checkNeighbour(Coordinate state, int dir){
        Coordinate var;
        var.x = var.y = -1;
        if(dir == 0){
            if (state.x-1 >= 0){
                if (visited[state.y][state.x-1] == 0){
                    var = {state.x-1, state.y+0};
                }
            }
        }
        if(dir == 1){
            if (state.x+1 < column){
                if (visited[state.y][state.x+1] == 0){
                    var = {state.x+1, state.y+0};
                }
            }
        }
        if(dir == 2){
            if (state.y-1 >= 0){
                if (visited[state.y-1][state.x] == 0){
                    var = {state.x+0, state.y-1};
                }
            }
        }
        if(dir == 3){
            if (state.y+1 < row){
                if (visited[state.y+1][state.x] == 0){
                    var = {state.x+0, state.y+1};
                }
            }
        }
        return var;
    }

    void writeSolution(){
        string fileaddress = "mazeSolution/bfs/" + filename;
        ofstream fw(fileaddress, ofstream::out);

        if (!fw.is_open()){
            throw invalid_argument("Could not open file!");
        }

        for (int i = 0; i < matrix.size(); ++i) {
            for (int j = 0; j < matrix[i].size(); ++j) {

                fw<<matrix[i][j];
                if(j != matrix[i].size()-1)
                    fw<<" ";
            }
            if(i != matrix.size()-1)
                fw<<"\n";
        }
    }

};

int main(int argc, char** argv){
    
    cout<<"\nSolving using BFS algorithm.\n";
    Queue queue;
    Maze maze;
    maze.filename = argv[1];
    maze.load();
    Node start = {maze.start, NULL};
    Node goal;
    goal.state.x = goal.state.y = -1;
    queue.add(&start);
    maze.visited[maze.start.y][maze.start.x] = 1;

    while (!queue.isEmpty()){

        Node *current = queue.remove();
        for (int i = 0; i < 4; i++) {
            Coordinate neighbour = maze.checkNeighbour(current->state, i);
            if (neighbour.x != -1 && neighbour.y != -1){
                Node *temp = new Node;
                *temp = {neighbour, current};
                queue.add(temp);
                maze.visited[neighbour.y][neighbour.x] = 1;
                //cout<<neighbour.y<<","<<neighbour.x;
                if (maze.goal.x == neighbour.x && maze.goal.y == neighbour.y){
                    goal = *temp;
                    break;
                }
            }
        }
    }

    if (goal.state.x == -1 || goal.state.y == -1){
        throw logic_error("No solution found!");
    } else{
        Node *current = &goal;
        while (current->previous != NULL){
            maze.matrix[current->state.y][current->state.x] = 'P';
            current = current->previous;
        }
        maze.matrix[maze.start.y][maze.start.x] = 'S';
        maze.matrix[maze.goal.y][maze.goal.x] = 'D';
    }

    maze.writeSolution();

    return 0;
}