#include <iostream>
#include <vector>
using namespace std;

int bubbleSort(vector<int>& arr) {
    int comparisons = 0;
    int n = arr.size();
    for (int i = 0; i < n - 1; ++i) {
        for (int j = 0; j < n - i - 1; ++j) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
            comparisons++;
        }
    }
    return comparisons;
}

int main() {
    vector<int> arr = {12, 11, 13, 5, 6};
    int comparisons = bubbleSort(arr);
    cout << "Sorted array: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << "\nNumber of comparisons: " << comparisons << endl;
    return 0;
}
