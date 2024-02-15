#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

using namespace std;

int bubbleSort(vector<int>& arr) {
    int comparisons = 0;
    int n = arr.size();
    for (int i = 0; i < n - 1; ++i) {
        for (int j = 0; j < n - i - 1; ++j) {
            comparisons++;
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
    return comparisons;
}

int main() {
    srand(time(0));

    // Test the algorithm on 100 different input sizes varying from 30 to 1000
    for (int size = 30; size <= 1000; size += 10) {
        long long totalComparisons = 0;

        // Average on 10 different input instances
        for (int instance = 0; instance < 10; ++instance) {
            vector<int> arr(size);
            for (int i = 0; i < size; ++i) {
                arr[i] = rand() % 1000; // Random integers between 0 and 999
            }

            totalComparisons += bubbleSort(arr);
        }

        // Calculate the average number of comparisons
        double averageComparisons = static_cast<double>(totalComparisons) / 10.0;

        // Output the average number of comparisons for the current input size
        cout << "Input Size: " << size << ", Average Comparisons: " << averageComparisons << endl;
    }

    return 0;
}

