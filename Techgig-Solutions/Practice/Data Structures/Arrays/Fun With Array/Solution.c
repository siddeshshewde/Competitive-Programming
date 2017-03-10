//https://www.techgig.com/practice/question/fun-with-array/NTQ0MkAjJEAjJDIwNjY4MDlAIyRAIyQzOTgwNTU1QCMkQCMkMTQ4OTE4MTcyNQ==/1

/* Read input from STDIN. Print your output to STDOUT*/
#include<stdio.h>
int main(int argc, char *a[])
{
	int i, j, length, arr[100], hlength, flag=0, count;
	scanf("%d",&length);
	for(i = 0; i < length; i++)
	{
	    scanf("%d",&arr[i]);
	}
	hlength = length/2;
	for(i = 0; i < length; i++)
	{
	    count = 0;
	    for(j = 0; j < length; j++)
    	{
    	    if(arr[i] == arr[j])
    	    {
    	        count ++;
    	    }
    	}
    	if(count >= hlength)
    	{
    	    flag = 1;
    	    break;
    	}
	}
	if(flag == 1)
	{
	    printf("%d",arr[i]);
	}
	else
	{
	    printf("-1");
	}
}
