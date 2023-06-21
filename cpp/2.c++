// WAP to remove duplicates from an array

#include <iostream>
using namespace std;
int main()
{
    int a[10], n, i, j, k;
    cout << "Enter the size of array: ";
    cin >> n;
    cout << "Enter the elements of array: ";
    for (i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    cout << "The array is: ";
    for (i = 0; i < n; i++)
    {
        cout << a[i] << " ";
    }
    cout << endl;
    for (i = 0; i < n; i++)
    {
        for (j = i + 1; j < n;)
        {
            if (a[i] == a[j])
            {
                for (k = j; k < n; k++)
                {
                    a[k] = a[k + 1];
                }
                n--;
            }
            else
            {
                j++;
            }
        }
    }
    cout << "The array after removing duplicates is: ";
    for (i = 0; i < n; i++)
    {
        cout << a[i] << " ";
    }
    return 0;
}

// Output of the upper program
//  Enter the size of array: 10
//  Enter the elements of array: 1 2 3 4 5 6 7 8 9 10
//  The array is: 1 2 3 4 5 6 7 8 9 10
//  The array after removing duplicates is: 1 2 3 4 5 6 7 8 9 10