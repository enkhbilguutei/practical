#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <cmath>
#include <fstream>

using namespace std;

int selectionSort(vector<int>& arr) {
    int comparisons = 0;
    int n = arr.size();
    for (int i = 0; i < n - 1; ++i) {
        int minIndex = i;
        for (int j = i + 1; j < n; ++j) {
            comparisons++;
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        if (minIndex != i) {
            swap(arr[i], arr[minIndex]);
        }
    }
    return comparisons;
}

void plotData(const vector<int>& inputSizes, const vector<double>& comparisonsSelectionSort, const vector<double>& comparisonsNLogN) {
    ofstream dataFile("comparison_data.txt");
    if (dataFile.is_open()) {
        for (size_t i = 0; i < inputSizes.size(); ++i) {
            dataFile << inputSizes[i] << " " << comparisonsSelectionSort[i] << " " << comparisonsNLogN[i] << endl;
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
    vector<double> comparisonsSelectionSort;
    vector<double> comparisonsNLogN;

    for (int size = 30; size <= 1000; size += 10) {
        long long totalComparisonsSelectionSort = 0;
        long long totalComparisonsNLogN = 0;

        for (int instance = 0; instance < 10; ++instance) {
            vector<int> arr(size);
            for (int i = 0; i < size; ++i) {
                arr[i] = rand() % 1000; // Random integers between 0 and 999
            }

            vector<int> arrCopy = arr; // Create a copy for nlogn

            totalComparisonsSelectionSort += selectionSort(arr);
            sort(arrCopy.begin(), arrCopy.end()); // Using std::sort for nlogn
            totalComparisonsNLogN += size * log2(size); // nlogn comparisons
        }

        double averageComparisonsSelectionSort = static_cast<double>(totalComparisonsSelectionSort) / 10.0;
        double averageComparisonsNLogN = static_cast<double>(totalComparisonsNLogN) / 10.0;

        inputSizes.push_back(size);
        comparisonsSelectionSort.push_back(averageComparisonsSelectionSort);
        comparisonsNLogN.push_back(averageComparisonsNLogN);

        cout << "Input Size: " << size << ", Average Comparisons Selection Sort: " << averageComparisonsSelectionSort << ", Average Comparisons NLogN: " << averageComparisonsNLogN << endl;
    }

    plotData(inputSizes, comparisonsSelectionSort, comparisonsNLogN);

    return 0;
}

