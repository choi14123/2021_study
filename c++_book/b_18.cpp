#include <iostream>
using namespace std;


int main() {
    
    int a = 5;
    int *p;
    int **pp;
    
    
    p = &a;
    pp = &p;
    
    cout << " p   =>" << p << " &a=>" << &a << endl;
    cout << " *p   =>" << *p << " a=>" << a << endl;
    cout << " pp   =>" << pp << " &p=>" << &p << endl;
    cout << " *pp   =>" << *pp << " p=>" << p << endl;
    cout << " **pp   =>" << **pp << " *p=>" << *p << endl;
    
}

