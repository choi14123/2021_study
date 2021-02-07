#include <iostream>
using namespace std;


int main() {
    struct Rectangle
    {
    int x, y;
    int width, height;
    };
    Rectangle rc = { 100, 100, 50, 50};

    Rectangle* p = &rc;

    (*p).x = 200;
    p->y = 250;
    cout << "rc = ( " << rc.x << ", " << rc.y << ", ";
    cout << rc.width << ", " << rc.height << ")\n";    
    }

