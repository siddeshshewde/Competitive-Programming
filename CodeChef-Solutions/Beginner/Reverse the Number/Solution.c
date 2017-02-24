#include<stdio.h>
int main()
{
    int n,a,rem;
    scanf("%d",&n);
    while(n--)
    {
    int t=0;
    scanf("%d",&a);
    while(a!=0)
    {
        rem=a%10;
        t=t*10+ rem;
        a=a/10;
    }
    printf("%d\n",t);
    }
    return 0;
    } 