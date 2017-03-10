//https://www.techgig.com/practice/question/alphabetical-rectangle-reverse/NTM3MUAjJEAjJDIwNjY4MDlAIyRAIyQzOTgwNTM4QCMkQCMkMTQ4OTE4MDQ3OQ==/1

/* Read input from STDIN. Print your output to STDOUT*/
#include<stdio.h>
int main()
{
	int n,i;
	char a = 'A';
	scanf("%d",&n);
	a = a+n-1;
	for (i=n;i>0;i--,a--)
	{
	    printf("%c %c %c %c %c\n",a,a,a,a,a);
	}
}
