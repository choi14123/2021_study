#include <stdio.h>
#include <stdlib.h>


int main(void)
{
    int *x;
    int *y;

    x = malloc(sizeof(int));
	//x에 size of 를 이용해 4byte 공간 지정
    *x = 42;
	// x 에 42 넣기
		cout << x;

    y = x;
	//y랑 x 는 같다.
		*y 13;
	// x의 자리에 y의 13 값 지정
		cout << y;
}
