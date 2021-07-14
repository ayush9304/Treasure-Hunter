#include <iostream>
#include <fstream>
#include <vector>
#include <ctime>
#include <string>
using namespace std;
int main()
{
    srand(time(0));
    vector<vector<int>> mat;
    int r = rand() % 15;
    int c = rand() % 25;
    // srand(time(NULL));
    for (int i = 0; i < r; i++)
    {
        vector<int> row;
        for (int j = 0; j < c; j++)
        {
            int n = rand() % 2;
            row.push_back(n);
        }
        mat.push_back(row);
    }
    string filename;
    cout << "Enter the file:" << endl;
    cin >> filename;
    string fileaddress = "maze/" + filename;

    ofstream of(fileaddress);
    for (int i = 0; i < r; i++)
    {
        // vector<int > row;
        for (int j = 0; j < c; j++)
        {
            // int n=rand()%2;
            // row.push_back(n);
            of << mat[i][j] << " ";
        }
        of << endl;
        // mat.push_back(row);
    }
    of.close();
    return 0;
}