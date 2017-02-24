#include<stdio.h>
int main()
{
	int t,n,j,max=0,l,i;
	scanf("%d",&t);
	int arr[1000];
	for(i=0;i<t;i++)
	{
		scanf("%d",&n);
		l=n/2;
		arr[i]=l+1;
	}
	for(i=0;i<t;i++)
	printf("%d \n",arr[i]);
	return 0;
 
}