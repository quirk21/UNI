#include <iostream>

long long mergeSort(long long arr[], int left, int right);
long long merge(long long arr[], int left, int mid, int right);


int main()
{
    int num;
    std::cin >> num;
    long long arr [num];
    for (int i = 0; i < num; i ++) std::cin >> arr[i];

    mergeSort(arr, 0, num-1);
    for (int i: arr) std::cout << i << " ";
    return 1;
}

long long mergeSort(long long arr[], int left, int right)
{   
    long long count = 0;
    if (sizeof(arr) <= 1){
        return arr;
    }
    else:
        mid = len(arr)//2
        a1 = mergeSort(............)
        a2 = mergeSort(............)
        return merge(a1, a2) 
    return 0;
}

long long merge(long long arr[], int left, int mid, int right)
{
    return 0;
}
