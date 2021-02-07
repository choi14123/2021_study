#include <iostream>
using namespace std;
int add (int x, int y);



int main() {
    
    int a = 10,b = 20, sum;
    sum = add (a,b);
    cout << "sum = " << sum << endl;
    
}

int add (int x, int y)
{
    int z;
    z = x + y;
    return (z) ;
}
