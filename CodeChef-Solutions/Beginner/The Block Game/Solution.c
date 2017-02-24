#include<stdio.h>
 
int main()
{
	int n;
	scanf("%d",&n);
	int i;
	for (i=0;i<n;i++)
	{
		int a,b,reverse=0;
		scanf("%d",&a);
		b = a;
		while (a>0)
		{
			reverse = reverse*10+(a%10);
			a = a/10;
		}
		if (b == reverse)
			printf("wins\n");
		else
			printf("losses\n");
		
	}
	return 0;
} 