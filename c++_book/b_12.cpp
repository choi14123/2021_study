#include <iostream>
using namespace std;

int main() {
    

    int x;
    
    cout << "정수를 입력하시요 => " << endl;
    cin >> x;
    
    if (x >= 0)
        cout << x << " 양수 입니다. ";
        else
            cout << x << " 음수 입니다. ";
            
}

