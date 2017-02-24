#include<stdio.h>
int main()
{
    int n,i;
    while(1)
    {
        scanf("%d",&n);
        int a[n],b[n];
        if(n==0)
            break;
        else
        {
           for(i=0;i<n;i++)
           {
               scanf("%d",&a[i]);
               b[a[i]-1]=i+1;
           }
           for(i=0;i<n;i++)
           {
               if(a[i]!=b[i])
                break;
           }
           if(i==n)
            printf("ambiguous\n");
           else
            printf("not ambiguous\n");
        }
    }
    return 0;
}