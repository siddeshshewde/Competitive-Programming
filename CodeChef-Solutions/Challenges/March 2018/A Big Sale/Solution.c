//https://www.codechef.com/MARCH18B/problems/BIGSALE

#include <stdio.h>

int main()
{
	int t, i;
	scanf("%d",&t);
	for (i=0;i<t;i++)
	{
		int n, j;
		float final=0.0F;
		scanf("%d",&n);
		for (j=0;j<n;j++)
		{
		    float ans=0.0F;
			float price, quantity, discount;
			scanf("%f%f%f", &price, &quantity, &discount);
			float price1 = (price + price * discount / 100.0F);
			price1 = price1 - price1 * discount / 100.0F;
			ans = (price - price1) * quantity;
			final = final + ans;
		}
		printf("%f\n",final);
	}
	return 0;
}