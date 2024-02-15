#include <iostream>
#include <vector>

void countingSort(std::vector<int>& arr, int exp) {
    int n = arr.size();
    std::vector<int> output(n), count(10, 0);
    
    for (int i = 0; i < n; ++i)
        count[(arr[i] / exp) % 10]++;
    
    for (int i = 1; i < 10; ++i)
        count[i] += count[i - 1];
    
    for (int i = n - 1; i >= 0; --i) {
        output[count[(arr[i] / exp) % 10] - 1] = arr[i];
        count[(arr[i] / exp) % 10]--;
    }
    
    for (int i = 0; i < n; ++i)
        arr[i] = output[i];
}

void radixSort(std::vector<int>& arr) {
    int maxElement = *std::max_element(arr.begin(), arr.end());
    
    for (int exp = 1; maxElement / exp > 0; exp *= 10)
        countingSort(arr, exp);
}

int main() {
    std::vector<int> arr = {170, 45, 75, 90, 802, 24, 2, 66};
    
    std::cout << "Array before sorting: ";
    for (int num : arr)
        std::cout << num << " ";
    std::cout << std::endl;
    
    radixSort(arr);
    
    std::cout << "Array after Radix Sort: ";
    for (int num : arr)
        std::cout << num << " ";
    std::cout << std::endl;
    
    return 0;
}
