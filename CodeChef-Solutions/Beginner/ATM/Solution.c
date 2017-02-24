#include<stdio.h>
int main()
{
	double a,b,c=0.5000000,d;
	scanf("%lf%lf",&a,&b);
	int x=a;
	d = b-a-c;
	if((x%5==0)&&(b>=a+0.50000)) 
	printf("%.2lf",d);
	else
	printf("%.2lf",b);
	return(0);
}