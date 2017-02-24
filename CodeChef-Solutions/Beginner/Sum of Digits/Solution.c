#include<stdio.h>
 
int main()
{
	int n;
	scanf("%d",&n);
	int i;
	for (i=0;i<n;i++)
	{
		int a,m=1,sum=0;
		scanf("%d",&a);
		while (a>0)
		{
			m = a%10;
			sum = sum + m;
			a = a/10;
		}
		printf("%d\n",sum);
	}
	return 0;
}