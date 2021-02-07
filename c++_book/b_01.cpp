#include <iostream>
using namespace std;


int main() {
   
    int x;
    
    cout << "정수 값을 입력하세요 ? => ";
    cin >> x;
    
    if (x < 0)
        x = -x;
    
    cout << " 절대값 => " << x << endl;
    
}

