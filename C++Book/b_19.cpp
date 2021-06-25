
#include <iostream>
using namespace std;
#define ROW  3
#define COL  4


int main() {
    
    int a [ROW] [COL] = {   { 90,  85  , 95  , 100},
                            {75,95,80,90},
                            {90, 80, 70, 60}
                                            };
    
    
    cout << " 이중 for 문으로 배열의 주소를 출력" << endl;
    cout << endl;
    cout << "------------------------" << endl;
    cout << endl;
    cout << endl;
    
    for (int r = 0; r < ROW; r++){
        
        cout << r << "번째 행 " << endl;
        cout << endl;
        for (int c= 0; c < COL; c++){
        cout << endl;
        cout << &a[r][c];
        }
    }
    cout << endl;
}

