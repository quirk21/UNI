#include <iostream>

int main(){
    int usr1;
    std::cin >> usr1;

    for (int i = 0; i < usr1; i++){
        long long usr2;
        std::cin >> usr2;
        std::cout << (usr2*(usr2+1)/2)<<"\n";
    }

}