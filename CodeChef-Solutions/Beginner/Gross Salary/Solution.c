#include <stdio.h>
 
int main(void) {
	// your code goes here
	int t;
	scanf("%d",&t);
	while(t--)
	{
		int  basic;
		double salary;
		scanf("%d",&basic);
		if(basic  < 1500)
		{
			salary = 2*basic;
		}
		else
		{
			salary = basic + 500 + (98*basic)/100.0;
		}
		printf("%g\n",salary);
	}
	return 0;
}