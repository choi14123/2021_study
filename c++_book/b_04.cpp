#include <iostream>
using namespace std;


int main() {
   
    int score;
    char grade;
    
    
    cout << " 점수를 입력하세요. " << endl;
    cin >> score;
    
    
    switch (score/10)
    {case 10 : grade = 'A';break;
        case 9 : grade = 'B';break;
        case 8 : grade = 'C';break;
        case 7 : grade = 'D';break;
        case 6 : grade = 'F';break;
    }
    
    
    cout << "입력한 점수 " << score << "입니다. , 학점은  "  << grade << " 입니다.  "<< endl;
}

