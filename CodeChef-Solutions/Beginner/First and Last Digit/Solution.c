#include<stdio.h>
 
int main()
{
	int n;
	scanf("%d",&n);
	int i;
	for (i=0;i<n;i++)
	{
		int a,last,first;
		scanf("%d",&a);
		last = a%10;
		while(a>0)
		{
			first = a%10;
			a=a/10;
		}
		printf("%d\n",first+last);
	}
	return 0;
}