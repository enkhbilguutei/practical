#include <iostream>
#include <vector>

void countSort(std::vector<int>& arr) {
    int maxElement = *std::max_element(arr.begin(), arr.end());
    int minElement = *std::min_element(arr.begin(), arr.end());
    int range = maxElement - minElement + 1;

    std::vector<int> count(range), output(arr.size());
    
    for (int i = 0; i < arr.size(); ++i)
        count[arr[i] - minElement]++;
    
    for (int i = 1; i < range; ++i)
        count[i] += count[i - 1];
    
    for (int i = arr.size() - 1; i >= 0; --i) {
        output[count[arr[i] - minElement] - 1] = arr[i];
        count[arr[i] - minElement]--;
    }
    
    for (int i = 0; i < arr.size(); ++i)
        arr[i] = output[i];
}

int main() {
    std::vector<int> arr = {4, 2, 2, 8, 3, 3, 1};
    
    std::cout << "Array before sorting: ";
    for (int num : arr)
        std::cout << num << " ";
    std::cout << std::endl;
    
    countSort(arr);
    
    std::cout << "Array after Count Sort: ";
    for (int num : arr)
        std::cout << num << " ";
    std::cout << std::endl;
    
    return 0;
}
