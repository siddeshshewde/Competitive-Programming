#include<stdio.h>
 
int main()
{
	int n;
	scanf("%d",&n);
	int i;
	for (i=0;i<n;i++)
	{
		int a,x=0,count = 0;
		scanf("%d",&a);
		int b = a;
		while (x!=b)
		{
			if (a>=100)
			{
				x = x+100;
				a = a-100;
				count++;
			}
			else if (a>=50)
			{
				x = x+50;
				a = a-50;
				count++;
			}
			else if (a>=10)
			{
				x = x+10;
				a = a-10;
				count++;
			}
			else if (a>=5)
			{
				x = x+5;
				a = a-5;
				count++;
			}
			else if (a>=2)
			{
				x = x+2;
				a = a-2;
				count++;
			}
			else if (a>=1)
			{
				x = x+1;
				a = a-1;
				count++;
			}	
		}
		printf("%d\n",count);
	}
	return 0;
}