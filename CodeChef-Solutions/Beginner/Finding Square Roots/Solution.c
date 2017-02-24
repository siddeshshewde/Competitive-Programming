#include<stdio.h>
#include<math.h>
 
int main()
{
	int n;
	scanf("%d",&n);
	int i;
	for(i=0;i<n;i++)
	{
		int a, b;
		scanf("%d",&a);
		b = (int)sqrt(a);
		printf("%d\n",b);
	}
	return 0;
}