// Create a class Student containing fields for Rol No, Name, Class, Year and Total Marks.
//  Write a program to store 5 objects of Student class in a file. Retrieve these records from the file and display them

#include <iostream>
#include <fstream>
#include <string>

class Student
{
private:
    int rollNo;
    std::string name;
    std::string className;
    int year;
    double totalMarks;

public:
    Student(int roll, const std::string &studentName, const std::string &cls, int studentYear, double marks)
        : rollNo(roll), name(studentName), className(cls), year(studentYear), totalMarks(marks) {}

    friend std::ostream &operator<<(std::ostream &os, const Student &student)
    {
        os << "Roll No: " << student.rollNo << std::endl;
        os << "Name: " << student.name << std::endl;
        os << "Class: " << student.className << std::endl;
        os << "Year: " << student.year << std::endl;
        os << "Total Marks: " << student.totalMarks << std::endl;
        return os;
    }

    friend std::istream &operator>>(std::istream &is, Student &student)
    {
        is >> student.rollNo;
        is.ignore(); // Ignore the newline character
        std::getline(is, student.name);
        std::getline(is, student.className);
        is >> student.year;
        is >> student.totalMarks;
        is.ignore(); // Ignore the newline character
        return is;
    }
};

int main()
{
    std::ofstream outFile("students.txt");

    if (!outFile)
    {
        std::cerr << "Error opening the file." << std::endl;
        return 1;
    }

    // Store 5 student objects in the file
    for (int i = 1; i <= 5; ++i)
    {
        int rollNo;
        std::string name, className;
        int year;
        double totalMarks;

        std::cout << "Enter details for Student " << i << std::endl;
        std::cout << "Roll No: ";
        std::cin >> rollNo;
        std::cin.ignore(); // Ignore the newline character
        std::cout << "Name: ";
        std::getline(std::cin, name);
        std::cout << "Class: ";
        std::getline(std::cin, className);
        std::cout << "Year: ";
        std::cin >> year;
        std::cout << "Total Marks: ";
        std::cin >> totalMarks;
        std::cin.ignore(); // Ignore the newline character

        Student student(rollNo, name, className, year, totalMarks);
        outFile << student;
        outFile << std::endl;
    }

    outFile.close();

    std::ifstream inFile("students.txt");

    if (!inFile)
    {
        std::cerr << "Error opening the file." << std::endl;
        return 1;
    }

    std::cout << "Records from the file: " << std::endl;
    Student student;

    while (inFile >> student)
    {
        std::cout << student << std::endl;
    }

    inFile.close();

    return 0;
}

// #include <iostream>
// #include <fstream>
// #include <string>
// using namespace std;

// class Student
// {
// private:
//     int rollno;
//     string name, cls;
//     int year, marks;

// public:
//     void getdata()
//     {
//         cout << "Enter roll no: ";
//         cin >> rollno;
//         cout << "Enter name: ";
//         cin >> name;
//         cout << "Enter class: ";
//         cin >> cls;
//         cout << "Enter year: ";
//         cin >> year;
//         cout << "Enter marks: ";
//         cin >> marks;
//     }

//     void display()
//     {
//         cout << "Roll no: " << rollno << endl;
//         cout << "Name: " << name << endl;
//         cout << "Class: " << cls << endl;
//         cout << "Year: " << year << endl;
//         cout << "Marks: " << marks << endl;
//     }

//     void write(ofstream &fout)
//     {
//         fout << rollno << endl;
//         fout << name << endl;
//         fout << cls << endl;
//         fout << year << endl;
//         fout << marks << endl;
//     }

//     void read(ifstream &fin)
//     {
//         fin >> rollno;
//         fin >> name;
//         fin >> cls;
//         fin >> year;
//         fin >> marks;
//     }
// };

// int main()
// {
//     Student s[5];
//     ofstream fout("student.txt");
//     for (int i = 0; i < 5; i++)
//     {
//         s[i].getdata();
//         s[i].write(fout);
//     }
//     fout.close();
//     ifstream fin("student.txt");
//     for (int i = 0; i < 5; i++)
//     {
//         s[i].read(fin);
//         s[i].display();
//     }
//     fin.close();
//     return 0;
// }

// // Output
// // Enter roll no: 1
// // Enter name: A
// // Enter class: 10
// // Enter year: 2020
// // Enter marks: 100
// // Enter roll no: 2
// // Enter name: B
// // Enter class: 10
// // Enter year: 2020
// // Enter marks: 100
// // Enter roll no: 3
// // Enter name: C
// // Enter class: 10
// // Enter year: 2020
// // Enter marks: 100
// // Enter roll no: 4
// // Enter name: D
// // Enter class: 10
// // Enter year: 2020
// // Enter marks: 100
// // Enter roll no: 5
// // Enter name: E
// // Enter class: 10
// // Enter year: 2020
// // Enter marks: 100
// // Roll no: 1
