#include <iostream>
#include <vector>
#include <random>
#include <chrono>
#include <algorithm>
#include <cmath>
#include "matplotlibcpp.h" // matplotlibcpp library for plotting

namespace plt = matplotlibcpp;

int insertionSort(std::vector<int>& arr) {
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
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> dist(1, 1000);

    std::vector<int> inputSizes;
    std::vector<double> avgComparisons;

    for (int size = 30; size <= 1000; size += 10) {
        inputSizes.push_back(size);
        double totalComparisons = 0;

        for (int instance = 0; instance < 10; ++instance) {
            std::vector<int> arr(size);
            for (int& num : arr) {
                num = dist(gen);
            }
            
            std::vector<int> arrCopy = arr;
            totalComparisons += insertionSort(arrCopy);
        }
        
        double averageComparisons = totalComparisons / 10.0;
        avgComparisons.push_back(averageComparisons);
    }

    // Plotting
    plt::figure();
    plt::plot(inputSizes, avgComparisons, "b", {{"label", "Average Comparisons"}});
    plt::named_plot("nlogn", inputSizes, plt::convert(std::vector<double>(inputSizes.size(), 10)), "r--");
    plt::xlabel("Input Size");
    plt::ylabel("Average Comparisons");
    plt::title("Comparison of Insertion Sort with nlogn");
    plt::legend();
    plt::show();

    return 0;
}
