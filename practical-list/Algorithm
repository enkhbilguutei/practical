#include <iostream>
#include <vector>
using namespace std;

int insertionSort(vector<int>& arr) {
    int comparisons = 0;
    int n = arr.size();
    for (int i = 1; i < n; ++i) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
            comparisons++;
        }
        arr[j + 1] = key;
    }
    return comparisons;
}

int main() {
    vector<int> arr = {12, 11, 13, 5, 6};
    int comparisons = insertionSort(arr);
    cout << "Sorted array: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << "\nNumber of comparisons: " << comparisons << endl;
    return 0;
}
