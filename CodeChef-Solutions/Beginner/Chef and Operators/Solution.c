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
		if (a>b)
			printf(">\n");
		if (a==b)
			printf("=\n");
		if (a<b)
			printf("<\n");
	}
	return 0;
} 
Comments 
