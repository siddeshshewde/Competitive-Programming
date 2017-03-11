//https://www.techgig.com/practice/question/ascending-numerical-right-angle-triangle/NTM3NUAjJEAjJDIwNjY4MDlAIyRAIyQzOTgxMjk5QCMkQCMkMTQ4OTIxMTkwMQ==/1

/* Read input from STDIN. Print your output to STDOUT*/
#include<stdio.h>
int main(int argc, char *a[])
{
	int n,i,j;
	scanf("%d",&n);
	for (i=1;i<=n;i++)
	{
	    for (j=1;j<=i;j++)
	    {
	        printf("%d",j);
	        if (j != i)
	            printf(" ");
	    }
	    printf("\n");
	}
}
