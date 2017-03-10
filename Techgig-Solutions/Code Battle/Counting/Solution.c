//https://www.techgig.com/codebattle/question/counting/NDgxMEAjJEAjJDIwNjY4MDlAIyRAIyQzOTgwNTcwQCMkQCMkMTQ4OTE4Mjc5Mw==/1

/* Read input from STDIN. Print your output to STDOUT*/
#include<stdio.h>
int main()
{
	int n,count = 0;
	scanf("%d",&n);
	while(n > 0)
	{
	    int digit = n % 10;
	    if (digit == 3)
	        count++;
	    n = n / 10;
	}
	printf("%d",count);
}
