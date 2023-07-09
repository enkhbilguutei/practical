// Write a program to search given element a set of N numbers.

#include <iostream>

using namespace std;

int main()
{
    int n, a[100], x, flag = 0;
    cout << "Enter the number of elements: ";
    cin >> n;
    cout << "Enter the elements: ";
    for (int i = 0; i < n; i++)
        cin >> a[i];
    cout << "Enter the element to be searched: ";
    cin >> x;
    for (int i = 0; i < n; i++)
    {
        if (a[i] == x)
        {
            flag = 1;
            break;
        }
    }
    if (flag == 1)
        cout << "Element found at position " << i + 1 << endl;
    else
        cout << "Element not found" << endl;
    return 0;
}
// Enter the number of elements: 5
// Enter the elements: 1 2 3 4 5
// Enter the element to be searched: 3
// Element found at position 3
