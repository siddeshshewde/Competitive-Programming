#include<stdio.h>
int main()
{
    int n,i,x,y,max=0;
     int p=0;
     int s=0,t=0;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
       scanf("%d%d",&x,&y);
       s=s+x;
       t=t+y;
       if((s-t)>max)
       {
           p=1;
           max=(s-t);
       }else if((t-s)>max)
       {
           p=2;
           max=(t-s);
       }
    }
        printf("%d  %d\n",p,max);
        return 0;
}