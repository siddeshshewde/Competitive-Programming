#include<stdio.h>
#include<stdlib.h>
int main()
{
int a,b;
long n;
scanf("%d",&a);
while(a--)
{
b=0;
scanf("%ld",&n);
while(n!=0)
{
b+=n/5;
n/=5;
}
printf("%d\n",b);
}
return 0;
}  