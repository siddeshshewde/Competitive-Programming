#include<stdio.h>
 
int main()
{
	int n,k;
	scanf("%d%d",&n,&k);
	int a=0,i;
	int b[n];
	for (i=0;i<n;i++)
	{
		scanf("%d",&b[i]);
		if (b[i]%k==0)
			a++;
	}
	printf("%d",a);
	
	
	return 0;
} 