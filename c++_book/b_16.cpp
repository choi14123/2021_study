//
//  main.cpp
//  1
//
//  Created by 최창환 on 2020/12/17.
//

#include <iostream>
using namespace std;

int main() {
    
    
    int a = 10;
    int &b = a;
    cout << " a = " << a << " b = " << b << endl;
    b += 300;
    cout << " b = " << b << endl;
    cout << " a = " << a << endl;
    
}

