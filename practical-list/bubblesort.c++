#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <cmath>
#include <fstream>

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

void plotData(const vector<int>& inputSizes, const vector<double>& comparisonsBubbleSort, const vector<double>& comparisonsNLogN) {
    ofstream dataFile("comparison_data.txt");
    if (dataFile.is_open()) {
        for (size_t i = 0; i < inputSizes.size(); ++i) {
            dataFile << inputSizes[i] << " " << comparisonsBubbleSort[i] << " " << comparisonsNLogN[i] << endl;
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
    vector<double> comparisonsBubbleSort;
    vector<double> comparisonsNLogN;

    for (int size = 30; size <= 1000; size += 10) {
        long long totalComparisonsBubbleSort = 0;
        long long totalComparisonsNLogN = 0;

        for (int instance = 0; instance < 10; ++instance) {
            vector<int> arr(size);
            for (int i = 0; i < size; ++i) {
                arr[i] = rand() % 1000; // Random integers between 0 and 999
            }

            vector<int> arrCopy = arr; // Create a copy for nlogn

            totalComparisonsBubbleSort += bubbleSort(arr);
            sort(arrCopy.begin(), arrCopy.end()); // Using std::sort for nlogn
            totalComparisonsNLogN += size * log2(size); // nlogn comparisons
        }

        double averageComparisonsBubbleSort = static_cast<double>(totalComparisonsBubbleSort) / 10.0;
        double averageComparisonsNLogN = static_cast<double>(totalComparisonsNLogN) / 10.0;

        inputSizes.push_back(size);
        comparisonsBubbleSort.push_back(averageComparisonsBubbleSort);
        comparisonsNLogN.push_back(averageComparisonsNLogN);

        cout << "Input Size: " << size << ", Average Comparisons Bubble Sort: " << averageComparisonsBubbleSort << ", Average Comparisons NLogN: " << averageComparisonsNLogN << endl;
    }

    plotData(inputSizes, comparisonsBubbleSort, comparisonsNLogN);

    return 0;
}
