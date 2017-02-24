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
                if (a==1 || a==0 )
                {
                        printf("no\n");
                        continue;
		}
		if (a==2)
		{
			printf("yes\n");
			continue;
		}
		int z,x;
		for (z=2;z<a;z++)
		{
			if (a%z==0)
				break;
			
		}
		if (z==a)
			printf("yes\n");
		else
			printf("no\n");
			
	}
	return 0;
}