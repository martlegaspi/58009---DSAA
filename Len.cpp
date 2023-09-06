#include<iostream>
using namespace std;


int main()
{
	int num[] = {5, 4, 3, 2, 1};
	int x = 0;
	cout<<"This is the original array: ";
	for(x=0;x<5;++x)
	{
		cout<<num[x]<<" ";
	}
	cout<<endl<<"The length of the original array is: "<<x;
	return 0;
}
