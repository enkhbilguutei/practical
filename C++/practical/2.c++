//Write a program to find whether a given number is prime or not.

#include <iostream>
using namespace std;

int main() {
    int num;
    bool is_prime = true;
    cout << "Enter a positive integer: ";
    cin >> num;

    if (num <= 1) {
        is_prime = false;
    } else {
        for (int i = 2; i <= num/2; i++) {
            if (num % i == 0) {
                is_prime = false;
                break;
            }
        }
    }

    if (is_prime) {
        cout << num << " is a prime number." << endl;
    } else {
        cout << num << " is not a prime number." << endl;
    }

    return 0;
}
