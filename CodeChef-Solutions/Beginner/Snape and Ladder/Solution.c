#include<stdio.h>
#include<math.h>
 
int main()
{
	int n;
	scanf("%d",&n);
	int i;
	for (i=0;i<n;i++)
	{
		int a,b;
		scanf("%d%d",&a,&b);
		float min = sqrt(abs(a*a-b*b));
		float max = sqrt(a*a+b*b);
		printf("%f %f\n",min,max);
	}
	return 0;
} 