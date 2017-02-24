#include<stdio.h>
#include<math.h>
int main()
{
	int i,t,x1,y1,x2,y2,x3,y3,r,a;
	float dist1;
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		a=0;
		scanf("%d",&r);
		scanf("%d %d %d %d %d %d",&x1,&y1,&x2,&y2,&x3,&y3);
		dist1=sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
		if(r>=dist1)
		a++;
		dist1=sqrt((x2-x3)*(x2-x3)+(y2-y3)*(y2-y3));
		if(r>=dist1)
		a++;
		dist1=sqrt((x3-x1)*(x3-x1)+(y3-y1)*(y3-y1));
		if(r>=dist1)
		a++;
		if(a<=1)
		printf("no\n");
		else
		printf("yes\n");
	}
	return 0;
}