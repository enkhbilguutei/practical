// Write a program that prints a table indicating the number of occurences of each alphabet in the text entered as command line arguments
#include <iostream>
#include <string.h>
using namespace std;

int main(int argc, char *argv[])
{
    int i, j, k, count = 0;
    char a[100];
    cout << "Enter the string: ";
    cin >> a;
    for (i = 0; i < strlen(a); i++)
    {
        for (j = i + 1; j < strlen(a);)
        {
            if (a[i] == a[j])
            {
                for (k = j; k < strlen(a); k++)
                {
                    a[k] = a[k + 1];
                }
                count++;
            }
            else
            {
                j++;
            }
        }
        cout << a[i] << " " << count << endl;
        count = 0;
    }
    return 0;
}