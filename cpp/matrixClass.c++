// Create a Matrix class. Write a menu-driven program to perform following Matrix
// operations (exceptions should be thrown by the functions if matrices passed to them are
// incompatible and handled by the main() function):
// a) Sum
// b) Product
// c) Tanspose

#include <iostream>
#include <conio.h> //compilation terminated with this code in VS Code
#include <stdlib.h>

using namespace std;

class Matrix
{
    int a[10][10], b[10][10], c[10][10], m, n, p, q, i, j, k;

public:
    void getdata();
    void sum();
    void product();
    void transpose();
    void display();
};

void Matrix::getdata()
{
    cout << "Enter the number of rows and columns of matrix A: ";
    cin >> m >> n;
    cout << "Enter the number of rows and columns of matrix B: ";
    cin >> p >> q;
    if (m != p || n != q)
    {
        cout << "Matrices are incompatible for addition and multiplication.";
        exit(0);
    }
    cout << "Enter the elements of matrix A: ";
    for (i = 0; i < m; i++)
        for (j = 0; j < n; j++)
            cin >> a[i][j];
    cout << "Enter the elements of matrix B: ";
    for (i = 0; i < p; i++)
        for (j = 0; j < q; j++)
            cin >> b[i][j];
}

void Matrix::sum()
{
    for (i = 0; i < m; i++)
        for (j = 0; j < n; j++)
            c[i][j] = a[i][j] + b[i][j];
}

void Matrix::product()
{
    for (i = 0; i < m; i++)
        for (j = 0; j < q; j++)
        {
            c[i][j] = 0;
            for (k = 0; k < n; k++)
                c[i][j] += a[i][k] * b[k][j];
        }
}

void Matrix::transpose()
{
    for (i = 0; i < m; i++)
        for (j = 0; j < n; j++)
            c[j][i] = a[i][j];
}

void Matrix::display()
{
    cout << "Matrix A: " << endl;
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
            cout << a[i][j] << "\t";
        cout << endl;
    }
    cout << "Matrix B: " << endl;
    for (i = 0; i < p; i++)
    {
        for (j = 0; j < q; j++)
            cout << b[i][j] << "\t";
        cout << endl;
    }
    cout << "Matrix C: " << endl;
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < q; j++)
            cout << c[i][j] << "\t";
        cout << endl;
    }
}

int main()
{
    Matrix m;
    int ch;
    char choice;
    do
    {
        cout << "1. Sum\n2. Product\n3. Transpose\nEnter your choice: ";
        cin >> ch;
        switch (ch)
        {
        case 1:
            m.getdata();
            m.sum();
            m.display();
            break;
        case 2:
            m.getdata();
            m.product();
            m.display();
            break;
        case 3:
            m.getdata();
            m.transpose();
            m.display();
            break;
        default:
            cout << "Invalid choice.";
        }
        cout << "Do you want to continue? (y/n): ";
        cin >> choice;
    } while (choice == 'y' || choice == 'Y');
    getch();
    return 0;
}
