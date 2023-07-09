// Write a program to calculate GCD of two numbers.

#include <iostream>

using namespace std;

int main()
{
    int a, b, gcd;
    cout << "Enter two numbers:";
    cin >> a >> b;
    for (int i = 1; i <= a && i <= b; i++)
    {
        if (a % i == 0 && b % i == 0)
            gcd = i;
    }

    cout << "GCD of " << a << " and " << b << " is " << gcd << endl;
    return 0;
}

// Enter two numbers:12 18
// GCD of 12 and 18 is 6

// Enter two numbers:5 7
// GCD of 5 and 7 is 1
