#include <iostream>
using namespace std;


int main() {
   
    int x;
    
    cout << "정수 값을 입력하세요." << endl;
    
    cin >> x;
    
    if (x % 2 == 1)
        cout << " 홀수이다. " << endl;
    else
        cout << " 짝수이다. " << endl;
}

