// Write a program to search a given element in a set of N numbers using Binary search 1. with recursion 2. without recursion.

#include <iostream>
using namespace std;

int binarySearch(int a[], int low, int high, int key)
{
    int mid;
    if (low > high)
        return -1;
    mid = (low + high) / 2;
    if (a[mid] == key)
        return mid;
    else if (a[mid] > key)
        return binarySearch(a, low, mid - 1, key);
    else
        return binarySearch(a, mid + 1, high, key);
}

int main()
{
    int a[10], n, i, key, pos;
    cout << "Enter the size of array: ";
    cin >> n;
    cout << "Enter the elements of array: ";
    for (i = 0; i < n; i++)
        cin >> a[i];
    cout << "Enter the element to be searched: ";
    cin >> key;
    pos = binarySearch(a, 0, n - 1, key);
    if (pos == -1)
        cout << "Element not found";
    else
        cout << "Element found at position " << pos + 1;
    return 0;
}

// Enter the size of array: 5
// Enter the elements of array: 1 2 3 4 5
// Enter the element to be searched: 3
// Element found at position 3
// Enter the size of array: 5
// Enter the elements of array: 1 2 3 4 5
// Enter the element to be searched: 6
// Element not found
