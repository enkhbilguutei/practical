#include <iostream>
#include <tuple>
#include <algorithm>

using namespace std;

int main() {
    tuple<int, int, int, int, int, int, int, int, int, int> t1 = make_tuple(1, 2, 5, 7, 9, 2, 4, 6, 8, 10);

    // a. Print half the values of the tuple in one line and the other half in the next line.
    int half_size = get<tuple_size<decltype(t1)>::value / 2>(t1);
    for (int i = 0; i < half_size; i++) {
        cout << get<i>(t1) << " ";
    }
    cout << endl;
    for (int i = half_size; i < tuple_size<decltype(t1)>::value; i++) {
        cout << get<i>(t1) << " ";
    }
    cout << endl;

    // b. Print another tuple whose values are even numbers in the given tuple.
    tuple<int, int, int, int, int, int, int, int, int, int> t2;
    int j = 0;
    for (int i = 0; i < tuple_size<decltype(t1)>::value; i++) {
        if (get<i>(t1) % 2 == 0) {
            get<j>(t2) = get<i>(t1);
            j++;
        }
    }
    for (int i = 0; i < j; i++) {
        cout << get<i>(t2) << " ";
    }
    cout << endl;

    // c. Concatenate a tuple t2=(11,13,15) with t1.
    tuple<int, int, int, int, int, int, int, int, int, int, int, int, int> t3 = tuple_cat(t1, make_tuple(11, 13, 15));
    for (int i = 0; i < tuple_size<decltype(t3)>::value; i++) {
        cout << get<i>(t3) << " ";
    }
    cout << endl;

    // d. Return maximum and minimum value from this tuple.
    int max_val = *max_element(t1);
    int min_val = *min_element(t1);
    cout << "Max value: " << max_val << endl;
    cout << "Min value: " << min_val << endl;

    return 0;
}
