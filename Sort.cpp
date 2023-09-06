#include<iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
	int num[] = {5, 4, 3, 2, 1};
	int x = 0;
	int n = sizeof(num) / sizeof(num[0]);
	cout<<"This is the original array: ";
	for(x=0;x<5;x++)
	{
		cout<<num[x]<<" ";
	}
	
	sort(num, num + n);
	cout<<endl<<"This is the sorted array: ";
	for(x=0;x<5;x++)
	{
		cout<<num[x]<<" ";
	}
	return 0;
}
