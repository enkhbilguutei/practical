// Write a menu driven program to perform string manipulatin ( without using inbiilt string functions):
// 1. Show address of each character in string
// 2. Concatenate two strings
// 3. Compare two strings
// 4. Calculate length of the string(use pointers)
// 5. Convert all lowercase characters to uppercase
// 6. Reverse the string
// 7. Insert a string in another string at a user specified position.

#include <iostream>
#include <string.h>
#include <ctype.h>

using namespace std;

int main()
{
    char str1[100], str2[100], str3[100];
    int choice, i, j, k, len1, len2, len3, pos;
    char ch;
    do
    {
        cout << "\n\n1. Show address of each character in string";
        cout << "\n2. Concatenate two strings";
        cout << "\n3. Compare two strings";
        cout << "\n4. Calculate length of the string(use pointers)";
        cout << "\n5. Convert all lowercase characters to uppercase";
        cout << "\n6. Reverse the string";
        cout << "\n7. Insert a string in another string at a user specified position.";
        cout << "\n8. Exit";
        cout << "\nEnter your choice: ";
        cin >> choice;
        switch (choice)
        {
        case 1:
            cout << "\nEnter a string: ";
            cin >> str1;
            len1 = strlen(str1);
            for (i = 0; i < len1; i++)
            {
                cout << "\nAddress of " << str1[i] << " is " << &str1[i];
            }
            break;
        case 2:
            cout << "\nEnter first string: ";
            cin >> str1;
            cout << "\nEnter second string: ";
            cin >> str2;
            len1 = strlen(str1);
            len2 = strlen(str2);
            for (i = 0; i < len2; i++)
            {
                str1[len1 + i] = str2[i];
            }
            str1[len1 + i] = '\0';
            cout << "\nConcatenated string is " << str1;
            break;
        case 3:
            cout << "\nEnter first string: ";
            cin >> str1;
            cout << "\nEnter second string: ";
            cin >> str2;
            len1 = strlen(str1);
            len2 = strlen(str2);
            if (len1 != len2)
            {
                cout << "\nStrings are not equal";
                break;
            }
            for (i = 0; i < len1; i++)
            {
                if (str1[i] != str2[i])
                {
                    cout << "\nStrings are not equal";
                    break;
                }
            }
            if (i == len1)
                cout << "\nStrings are equal";
            break;
        case 4:
            cout << "\nEnter a string: ";
            cin >> str1;
            len1 = strlen(str1);
            cout << "\nLength of the string is " << len1;
            break;
        case 5:

            cout << "\nEnter a string: ";
            cin >> str1;
            len1 = strlen(str1);
            for (i = 0; i < len1; i++)
            {
                if (str1[i] >= 'a' && str1[i] <= 'z')
                    str1[i] = str1[i] - 32;
            }
            cout << "\nString in uppercase is " << str1;
            break;
        case 6:
            cout << "\nEnter a string: ";
            cin >> str1;
            len1 = strlen(str1);
            for (i = 0, j = len1 - 1; i < j; i++, j--)
            {
                ch = str1[i];
                str1[i] = str1[j];
                str1[j] = ch;
            }
            cout << "\nReversed string is " << str1;
            break;
        case 7:
            cout << "\nEnter first string: ";
            cin >> str1;
            cout << "\nEnter second string: ";
            cin >> str2;
            cout << "\nEnter position at which second string is to be inserted: ";
            cin >> pos;
            len1 = strlen(str1);
            len2 = strlen(str2);
            for (i = 0; i < pos; i++)
            {
                str3[i] = str1[i];
            }
            for (j = 0; j < len2; j++)
            {
                str3[i + j] = str2[j];
            }
            for (k = i; k < len1; k++)
            {
                str3[i + j] = str1[k];
                i++;
            }
            str3[i + j] = '\0';
            cout << "\nString after insertion is " << str3;
            break;
        case 8:
            break;
        default:
            cout << "\nInvalid choice";
        }
    } while (choice != 8);
    return 0;
}
