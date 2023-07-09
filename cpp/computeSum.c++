#include <iostream>
#include "math.h"

using namespace std;

int main()
{
    int a;
    cout << "Enter n : ";
    cin >> a;

    float s = 0;
    for (int i = 1; i <= a; i++)
    {
        for (i % 2 == 1)
        {
            float x = i;

            s += ((float)1 / (float)powf(x, x));
        }
        else
        {
            float x = i;
    s -= ((float) 1/ (float) powf(x,x);
        }
    }
    cout << s;

        )
    )
}