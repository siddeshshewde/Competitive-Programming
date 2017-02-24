#include<stdio.h>
 
int main()
{
	int n;
	scanf("%d",&n);
	int i;
	for(i=0;i<n;i++)
	{
		int a,b;
		scanf("%d%d",&a,&b);
		int min;
		if (a<=b)
			min = b;
		else
			min = a;
		int max = a+b;
		printf("%d %d\n",min,max);
	}
	return 0;
}