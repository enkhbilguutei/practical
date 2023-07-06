// Define a class Person having name as a data member. Inherit two classes Student and Employee from Person. Student has additional attributes as course, marks and year and Employee has department and salary. Write display() method in all the three classes to display the corresponding attributes. Provide the necessary methods to show runtime polymorphism and entered by user.

#include <iostream>
#include <string>

class Person
{
protected:
    std::string name;

public:
    Person(const std::string &personName) : name(personName) {}

    virtual void display()
    {
        std::cout << "Name: " << name << std::endl;
    }
};

class Student : public Person
{
private:
    std::string course;
    int marks;
    int year;

public:
    Student(const std::string &studentName, const std::string &studentCourse, int studentMarks, int studentYear)
        : Person(studentName), course(studentCourse), marks(studentMarks), year(studentYear) {}

    void display() override
    {
        std::cout << "Name: " << name << std::endl;
        std::cout << "Course: " << course << std::endl;
        std::cout << "Marks: " << marks << std::endl;
        std::cout << "Year: " << year << std::endl;
    }
};

class Employee : public Person
{
private:
    std::string department;
    double salary;

public:
    Employee(const std::string &employeeName, const std::string &employeeDepartment, double employeeSalary)
        : Person(employeeName), department(employeeDepartment), salary(employeeSalary) {}

    void display() override
    {
        std::cout << "Name: " << name << std::endl;
        std::cout << "Department: " << department << std::endl;
        std::cout << "Salary: " << salary << std::endl;
    }
};

int main()
{
    Person *person = new Person("Bilguutei");
    Student *student = new Student("Bat Badral", "Computer Science", 95, 2023);
    Employee *employee = new Employee("Bat Badral", "Human Resources", 5000.0);

    person->display(); // Calls display() from the Person class
    std::cout << std::endl;

    student->display(); // Calls display() from the Student class
    std::cout << std::endl;

    employee->display(); // Calls display() from the Employee class
    std::cout << std::endl;

    delete person;
    delete student;
    delete employee;

    return 0;
}

// #include <iostream>
// #include <string>
// using namespace std;

// class Person
// {
// protected:
//     string name;

// public:
//     void getname()
//     {
//         cout << "Enter name: ";
//         cin >> name;
//     }
//     void display()
//     {
//         cout << "Name: " << name << endl;
//     }
// };

// class Student : public Person
// {
// protected:
//     string course;
//     int marks, year;

// public:

//     void getdata()
//     {
//         cout << "Enter course: ";
//         cin >> course;
//         cout << "Enter marks: ";
//         cin >> marks;
//         cout << "Enter year: ";
//         cin >> year;
//     }
//     void display()
//     {
//         cout << "Course: " << course << endl;
//         cout << "Marks: " << marks << endl;
//         cout << "Year: " << year << endl;
//     }
// };

// class Employee : public Person
// {
// protected:
//     string department;
//     int salary;

// public:

//     void getdata()
//     {
//         cout << "Enter department: ";
//         cin >> department;
//         cout << "Enter salary: ";
//         cin >> salary;
//     }
//     void display()
//     {
//         cout << "Department: " << department << endl;
//         cout << "Salary: " << salary << endl;
//     }
// };

// int main()
// {
//     Student s;
//     Employee e;
//     s.getname();
//     s.getdata();
//     e.getname();
//     e.getdata();
//     s.display();
//     e.display();
//     return 0;
// }

// Output
// Enter name: John
// Enter course: BCA
// Enter marks: 80
// Enter year: 2
// Enter name: Smith
// Enter department: IT
// Enter salary: 50000
// Course: BCA
// Marks: 80
// Year: 2
// Department: IT
// Salary: 50000