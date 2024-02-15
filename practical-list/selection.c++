#include <iostream>
#include <vector>
using namespace std;

int selectionSort(vector<int>& arr) {
    int comparisons = 0;
    int n = arr.size();
    for (int i = 0; i < n - 1; ++i) {
        int min_index = i;
        for (int j = i + 1; j < n; ++j) {
            if (arr[j] < arr[min_index]) {
                min_index = j;
            }
            comparisons++;
        }
        swap(arr[i], arr[min_index]);
    }
    return comparisons;
}

int main() {
    vector<int> arr = {12, 11, 13, 5, 6};
    int comparisons = selectionSort(arr);
    cout << "Sorted array: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << "\nNumber of comparisons: " << comparisons << endl;
    return 0;
}
