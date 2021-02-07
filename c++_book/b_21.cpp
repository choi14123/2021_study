#include <iostream>
using namespace std;


int main() {

    int target = 20;

    int& ref = target;
    cout << "ref = " << ref << endl;
    cout << "target = " << target << endl;
    cout << "&ref = " << &ref << endl;
    cout << "&target = " << &target << endl;

    ref = 100;
    cout << "ref = " << ref << endl;
    cout << "target = " << target << endl;
}

