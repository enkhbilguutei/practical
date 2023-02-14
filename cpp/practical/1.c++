//Write a program to find the largest of n natural numbers.

#include <iostream>
using namespace std;

int main() {
    int n, max_num = 0, num;
    cout << "Enter the number of natural numbers: ";
    cin >> n;
    for (int i = 0; i < n; i++) {
        cout << "Enter a natural number: ";
        cin >> num;
        if (num > max_num) {
            max_num = num;
        }
    }
    cout << "The largest of the " << n << " natural numbers is " << max_num << endl;
    return 0;
}


// This program first prompts the user to enter the number of natural numbers they would like to compare. It then asks the user to enter each natural number one by one and compares it to the current maximum value. If the new number is greater than the current maximum value, it becomes the new maximum. Finally, the program outputs the largest number found.



