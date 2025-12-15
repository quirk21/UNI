#include <iostream>

int main() {
    int N, S;
    std::cin >> N >> S;
    
    int arr[N];
    for (int i = 0; i < N; i++) {
        std::cin >> arr[i];
    }
    
    int left = 0, right = N - 1;
    while (left < right) {
        int sum = arr[left] + arr[right];
        if (sum == S) {
            std::cout << left + 1 << " " << right + 1 << std::endl;
            return 0;
        } else if (sum < S) {
            left++;
        } else {
            right--;
        }
    }
    
    std::cout << -1 << std::endl;
    return 0;
}
