#include <bits/stdc++.h>
using namespace std;

int main (){
    int node; 
    int edge; 
    cin >> node;
    cin >> edge;
    int arr[node*node];
    adj_matrix(node, edge, arr);
    for (int i=0; i < sizeof(arr) / sizeof(arr[0]); i++){
        for (int j=0; j < sizeof(arr) / sizeof(arr[0]); j++){
            cout << arr[i][j] << " ";
        }
    }

}

int adj_matrix(int node, int edge, int arr[]){

}