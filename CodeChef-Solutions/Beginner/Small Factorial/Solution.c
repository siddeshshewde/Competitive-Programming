#include<stdio.h>
 
int main()
{
	int n;
	scanf("%d",&n);
	int i;
	for (i=0;i<n;i++)
	{
		int a;
		scanf("%d",&a);
		int j,fact = 1;
		for (j=1;j<=a;j++)
		{
			fact = fact*j;
		}
		printf("%d\n",fact);
	}
	return 0;
}