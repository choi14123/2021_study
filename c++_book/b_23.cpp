#include <iostream>
using  namespace  std;



int  main()
{
    
     int temp = 0;
     int result = 0;
    
    unsigned int scores[10] = { 10, 100, 94, 36, 72, 88, 60, 60, 80, 24 };
    
    for (int i =0; (i =10); i++)
    {
    temp += scores [i];
    }
    
    result = temp / 10;
    
    
    cout << result << endl;
    
}

