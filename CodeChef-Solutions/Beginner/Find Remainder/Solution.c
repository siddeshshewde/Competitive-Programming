#include<stdio.h>
 
int main()
{
	int n;
	scanf("%d",&n);
	int i;
	for (i=0;i<n;i++)
	{
		int a,b;
		scanf("%d%d",&a,&b);
		printf("%d\n",a%b);
	}
	return 0;
}