//https://www.techgig.com/practice/question/numerical-right-angle-triangle/NTM3NEAjJEAjJDIwNjY4MDlAIyRAIyQzOTgwNTUyQCMkQCMkMTQ4OTE4MTM2NQ==/1

/* Read input from STDIN. Print your output to STDOUT*/
#include<stdio.h>
int main()
{
	int n,i,j;
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
	    for (j=1;j<=i;j++)
	    {
	        printf("%d",i);
	        if (j<i)
	            printf(" ");
	    }
	    printf("\n");
	}
}
