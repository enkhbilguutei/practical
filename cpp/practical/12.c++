//  WAP to accept a name from a user. Raise and handle appropriate exception(s) if the text
// entered by the user contains digits and/or special characters.
#include <iostream>
#include <string>
#include <stdexcept>
#include <cctype>

using namespace std;

bool containsDigitsOrSpecialChars(const string& s) {
    for (char c : s) {
        if (isdigit(c) || ispunct(c)) {
            return true;
        }
    }
    return false;
}

int main() {
    string name;
    cout << "Enter your name: ";
    getline(cin, name);

    try {
        if (containsDigitsOrSpecialChars(name)) {
            throw invalid_argument("Name should not contain digits or special characters.");
        }
        cout << "Hello, " << name << "!" << endl;
    } catch (const exception& e) {
        cerr << "Error: " << e.what() << endl;
    }
    return 0;
}
