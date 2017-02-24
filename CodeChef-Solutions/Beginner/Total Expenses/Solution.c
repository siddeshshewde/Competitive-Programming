include<stdio.h>
 
int main()
{
	int n;
	scanf("%d",&n);
	int i;
	for (i=0;i<n;i++)
	{
		int quantity,price;
		scanf("%d%d",&quantity,&price);
		float answer = 0.0;
		answer = quantity * price;
		if (quantity > 1000)
			answer = answer - (answer*10/100);
		printf("%f\n",answer);
	}
	return 0;
}