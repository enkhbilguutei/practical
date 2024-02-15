#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <fstream>
#include <algorithm>

using namespace std;

int countSort(vector<int>& arr) {
    int comparisons = 0;
    int max_element = *max_element(arr.begin(), arr.end());
    int min_element = *min_element(arr.begin(), arr.end());
    int range = max_element - min_element + 1;
    
    vector<int> count(range), output(arr.size());
    
    // Count the occurrences of each element
    for(int i = 0; i < arr.size(); i++) {
        count[arr[i] - min_element]++;
    }
    
    // Calculate cumulative count
    for(int i = 1; i < range; i++) {
        count[i] += count[i - 1];
    }
    
    // Build the output array
    for(int i = arr.size() - 1; i >= 0; i--) {
        output[count[arr[i] - min_element] - 1] = arr[i];
        count[arr[i] - min_element]--;
        comparisons++;
    }
    
    // Copy the sorted elements to the original array
    for(int i = 0; i < arr.size(); i++) {
        arr[i] = output[i];
    }
    
    return comparisons;
}

void generateRandomArray(vector<int>& arr, int size) {
    arr.clear();
    for (int i = 0; i < size; ++i) {
        arr.push_back(rand() % 1000); // Random integers between 0 and 999
    }
}

void plotData(const vector<int>& inputSizes, const vector<double>& comparisonsCountSort, const vector<double>& comparisonsNLogN) {
    ofstream dataFile("comparison_data.txt");
    if (dataFile.is_open()) {
        for (size_t i = 0; i < inputSizes.size(); ++i) {
            dataFile << inputSizes[i] << " " << comparisonsCountSort[i] << " " << comparisonsNLogN[i] << endl;
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
    vector<double> comparisonsCountSort;
    vector<double> comparisonsNLogN;

    for (int size = 30; size <= 1000; size += 10) {
        long long totalComparisonsCountSort = 0;
        long long totalComparisonsNLogN = 0;

        for (int instance = 0; instance < 10; ++instance) {
            vector<int> arr;
            generateRandomArray(arr, size);

            totalComparisonsCountSort += countSort(arr);

            // Calculating nlogn
            totalComparisonsNLogN += size * log2(size);
        }

        double averageComparisonsCountSort = static_cast<double>(totalComparisonsCountSort) / 10.0;
        double averageComparisonsNLogN = static_cast<double>(totalComparisonsNLogN) / 10.0;

        inputSizes.push_back(size);
        comparisonsCountSort.push_back(averageComparisonsCountSort);
        comparisonsNLogN.push_back(averageComparisonsNLogN);

        cout << "Input Size: " << size << ", Average Comparisons Count Sort: " << averageComparisonsCountSort << ", Average Comparisons NLogN: " << averageComparisonsNLogN << endl;
    }

    plotData(inputSizes, comparisonsCountSort, comparisonsNLogN);

    return 0;
}
