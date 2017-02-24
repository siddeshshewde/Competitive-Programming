include<stdio.h>
 
int main()
{
	int n;
	scanf("%d",&n);
	int i;
	for (i=0;i<n;i++)
	{
		int a,count=0;
		scanf("%d",&a);
		int m;
		while (a>0)
		{
			m = a%10;
			if (m==4)
				count++;
			a = a/10;
		}
		printf("%d\n",count);
	}
	return 0;
} 