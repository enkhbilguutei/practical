// Write a program merge two ordered arrays to get a single ordered array.

#include <iostream>
using namespace std;

int main()
{
    int a[10], b[10], c[20], i, j, k, n1, n2;
    cout << "Enter the size of first array: ";
    cin >> n1;
    cout << "Enter the elements of first array: ";
    for (i = 0; i < n1; i++)
        cin >> a[i];
    cout << "Enter the size of second array: ";
    cin >> n2;
    cout << "Enter the elements of second array: ";
    for (i = 0; i < n2; i++)
        cin >> b[i];
    i = 0;
    j = 0;
    k = 0;
    while (i < n1 && j < n2)
    {
        if (a[i] < b[j])
        {
            c[k] = a[i];
            i++;
            k++;
        }
        else
        {
            c[k] = b[j];
            j++;
            k++;
        }
    }
    while (i < n1)
    {
        c[k] = a[i];
        i++;
        k++;
    }
    while (j < n2)
    {
        c[k] = b[j];
        j++;
        k++;
    }
    cout << "The merged array is: ";
    for (i = 0; i < n1 + n2; i++)
        cout << c[i] << " ";
    return 0;
}

// Enter the size of first array: 5
// Enter the elements of first array: 1 3 5 7 9
// Enter the size of second array: 5
// Enter the elements of second array: 2 4 6 8 10
// The merged array is: 1 2 3 4 5 6 7 8 9 10
