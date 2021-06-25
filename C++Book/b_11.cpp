//
//  main.cpp
//  page
//
//  Created by 최창환 on 2021/01/21.
//

#include <iostream>
using namespace std;


int main() {
    
    int num;
    cout << "수를 입력하세요.! (0를 입력하면 종료합니다.)  : ";
    cin >> num;
    
    while (num != 0) {
        cout << num << "를 입력하셨습니다. " << endl;
        cin >> num;
    }
    
    cout << num << "을 입력하였기에 반복문이 종료되었습니다." << endl;
}
