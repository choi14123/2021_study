#include <iostream>
using namespace std;

int main() {
	// your code goes here
		
	cout<<"plese enter one number"<<endl;
	int num = 0;
	cin>>num;
	cout<<num<<endl;
	
	int j=0;
	
	while(num>0){
		j=num;
		while(j>0){
			cout<<"*";
			j—-;
		}
		num —-;
		cout<<endl;
	}
	return 0;
}
