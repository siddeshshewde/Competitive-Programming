#include<stdio.h>

int main ()
{
	int t,i = 0;
	scanf("%d",&t);
	for (i=0;i<t;i++)
	{
		int j,n = 0;
		scanf("%d",&n);
		int a[n],b[n];
		
		for (j=0;j<n;j++)
		{
			scanf("%d",&a[j]);
		}
		
		for (j=0;j<n;j++)
		{
			scanf("%d",&b[j]);
		}
		
		int k = 0;
		
		for (j=0;j<n;j++)
		{
			if(a[j]<=b[j])
			{
				if(j==n-1)
					k=k+1;
			}
			else
			{
				break;
			}
		}
		
		for (j=0;j<n;j++)
		{
			if(a[j]<=b[n-j-1])
			{
				if(j==n-1)
					k=k+2;
			}
			else
				break;
		}
		
		if (k==0) printf("none\n");
		if (k==1) printf("front\n");
		if (k==2) printf("back\n");
		if (k==3) printf("both\n");
		
	}
	return 0;
}