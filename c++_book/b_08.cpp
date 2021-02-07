#include <iostream>
using namespace std;

int main() {
    
    
    int x;
    
    cout << "구구단의 단수를 입력하여 주새요.! " << endl;
    cin >> x;
    
    for (int i = 1; i < 10; i++)
    {
        cout << x << " x = "  << x * i << endl;
    }
    
}

