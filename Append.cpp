#include<iostream>
using namespace std;

int main()
{
	int num[] = {1,2,3,4,5,6,7,8,9,10};
	int x = 0;
	cout<<"This is the original array: ";
	for(x=0;x<10;++x)
	{
		cout<<num[x]<<" ";
	}
	cout<<endl<<"Enter a whole number to add before the second element of the array: ";
	cin>>num[10];
	cout<<endl<<"This is the new array: ";
	for(x=0;x<11;++x)
	{
		cout<<num[x]<<" ";
	}
	return 0;
}
