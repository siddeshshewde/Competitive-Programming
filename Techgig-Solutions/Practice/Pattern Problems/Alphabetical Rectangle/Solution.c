//https://www.techgig.com/practice/question/alphabetical-rectangle/NTM2N0AjJEAjJDIwNjY4MDlAIyRAIyQzOTgwNTI1QCMkQCMkMTQ4OTE3OTgyOQ==/1

/* Read input from STDIN. Print your output to STDOUT*/
#include<stdio.h>
int main(int argc, char *a[])
{
	int n,i;
	char z = 'A';
	scanf("%d",&n);
	for (i=0;i<n;i++)
	{
	    printf("%c %c %c %c %c\n",z,z,z,z,z);
	    z++;
	}
}
