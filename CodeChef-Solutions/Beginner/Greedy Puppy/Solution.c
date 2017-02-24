#include<stdio.h>
int main()
{
	int t;
	scanf("%d",&t);
	while (t--)
	{
		int k,n,r,g=0,i;
		scanf("%d %d",&n,&k);
	    for (i=1;i<=k;i++)
	    {
	    	r=n%i;
	    	if (r>g)
	    	{
	              g=r;
	    	}
	    }
	    	printf("%d\n",g);
	}
	return 0;
}