//https://www.techgig.com/codebattle/question/fibonacci-numbers/NDcxOEAjJEAjJDIwNjY4MDlAIyRAIyQ0MDYzMDAzQCMkQCMkMTQ5MDUwOTI5MA==/1

#include<stdio.h>
#include<string.h>
int arr[10];
int* fibonacci_series(int input1,int input2)
{
	int i=2;
	arr[0]=input1;arr[1]=input2;
	while(i<=10)
	{
	    arr[i]=input1+input2;
	    input1=input2;
	    input2=arr[i];
	    i++;
	}
	return arr;
}