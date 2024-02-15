#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <fstream>

using namespace std;

// Function to get the maximum element from an array
int getMax(vector<int>& arr) {
    int max = arr[0];
    for (size_t i = 1; i < arr.size(); ++i) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

// A function to do counting sort of arr[] according to the digit represented by exp.
int countingSort(vector<int>& arr, int exp, int& comparisons) {
    int n = arr.size();
    vector<int> output(n);
    int count[10] = {0};

    // Store count of occurrences in count[]
    for (int i = 0; i < n; i++) {
        count[(arr[i] / exp) % 10]++;
    }

    // Change count[i] so that count[i] now contains actual position of this digit in output[]
    for (int i = 1; i < 10; i++) {
        count[i] += count[i - 1];
    }

    // Build the output array
    for (int i = n - 1; i >= 0; i--) {
        output[count[(arr[i] / exp) % 10] - 1] = arr[i];
        count[(arr[i] / exp) % 10]--;
        comparisons++; // Increment comparisons
    }

    // Copy the output array to arr[], so that arr[] now contains sorted numbers according to current digit
    for (int i = 0; i < n; i++) {
        arr[i] = output[i];
    }
}

// Main function to implement Radix Sort
int radixSort(vector<int>& arr) {
    int comparisons = 0;
    int max = getMax(arr);

    // Do counting sort for every digit.
    // Instead of passing digit number, exp is passed. exp is 10^i where i is the current digit number
    for (int exp = 1; max / exp > 0; exp *= 10) {
        countingSort(arr, exp, comparisons);
    }

    return comparisons;
}

void generateRandomArray(vector<int>& arr, int size) {
    arr.clear();
    for (int i = 0; i < size; ++i) {
        arr.push_back(rand() % 1000); // Random integers between 0 and 999
    }
}

void plotData(const vector<int>& inputSizes, const vector<double>& comparisonsRadixSort, const vector<double>& comparisonsNLogN) {
    ofstream dataFile("comparison_data.txt");
    if (dataFile.is_open()) {
        for (size_t i = 0; i < inputSizes.size(); ++i) {
            dataFile << inputSizes[i] << " " << comparisonsRadixSort[i] << " " << comparisonsNLogN[i] << endl;
        }
        dataFile.close();
        cout << "Data saved to comparison_data.txt" << endl;
    } else {
        cout << "Unable to open file for writing." << endl;
    }
}

int main() {
    srand(time(0));

    vector<int> inputSizes;
    vector<double> comparisonsRadixSort;
    vector<double> comparisonsNLogN;

    for (int size = 30; size <= 1000; size += 10) {
        long long totalComparisonsRadixSort = 0;
        long long totalComparisonsNLogN = 0;

        for (int instance = 0; instance < 10; ++instance) {
            vector<int> arr;
            generateRandomArray(arr, size);

            totalComparisonsRadixSort += radixSort(arr);

            // Calculating nlogn
            totalComparisonsNLogN += size * log2(size);
        }

        double averageComparisonsRadixSort = static_cast<double>(totalComparisonsRadixSort) / 10.0;
        double averageComparisonsNLogN = static_cast<double>(totalComparisonsNLogN) / 10.0;

        inputSizes.push_back(size);
        comparisonsRadixSort.push_back(averageComparisonsRadixSort);
        comparisonsNLogN.push_back(averageComparisonsNLogN);

        cout << "Input Size: " << size << ", Average Comparisons Radix Sort: " << averageComparisonsRadixSort << ", Average Comparisons NLogN: " << averageComparisonsNLogN << endl;
    }

    plotData(inputSizes, comparisonsRadixSort, comparisonsNLogN);

    return 0;
}
