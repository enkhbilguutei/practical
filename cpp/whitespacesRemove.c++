// Copy the contents of one text file to another file, after removing all whitespaces

#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin("11.c++");
    ofstream fout("10.c++");
    char ch;
    while (fin.get(ch))
    {
        if (ch != ' ')
            fout << ch;
    }
    fin.close();
    fout.close();
    return 0;
}
