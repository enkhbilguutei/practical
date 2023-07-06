// Create a Triangle class. Add exception handling statements to ensure the following
// conditions: all sides are greater than 0 and sum of any two sides are greater than the
// third side. The class should also have overloaded functions for calculating the area of
// a right angled triangle as well as using Heron's formula to calculate the area of any type
// of triangle

#include <iostream>
#include <cmath>
using namespace std;

class Triangle
{
private:
    float a, b, c;

public:
    Triangle()
    {
        a = b = c = 0;
    }

    Triangle(float a, float b, float c)
    {
        this->a = a;
        this->b = b;
        this->c = c;
    }

    void getdata()
    {
        cout << "Enter sides of triangle: ";
        cin >> a >> b >> c;
    }

    void display()
    {
        cout << "Sides of triangle: " << a << ", " << b << ", " << c << endl;
    }

    float area()
    {
        float s = (a + b + c) / 2;
        return sqrt(s * (s - a) * (s - b) * (s - c));
    }

    float area(float base, float height)
    {
        return 0.5 * base * height;
    }
};

int main()
{
    Triangle t1, t2(3, 4, 5);
    t1.getdata();
    t1.display();
    cout << "Area of triangle: " << t1.area() << endl;
    cout << "Area of right angled triangle: " << t1.area(3, 4) << endl;
    cout << "Area of right angled triangle: " << t2.area(3, 4) << endl;
    return 0;
}

// Output
// Enter sides of triangle: 3 4 5
// Sides of triangle: 3, 4, 5
// Area of triangle: 6
// Area of right angled triangle: 6
// Area of right angled triangle: 6
