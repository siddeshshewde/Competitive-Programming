#include<stdio.h>
#include<math.h>
int main(){
	int t,temp;
	scanf("%d",&t);
	while(t--){
		int n,i,yf=0,iyf=0;
		scanf("%d",&n);
		char arr[n+1];
		scanf("%s",arr);
		for(i=0;i<n;i++){
			if(arr[i]=='Y')
				yf++;
			if(arr[i]=='I')
				iyf++;
		}
		if(iyf!=0)
			printf("INDIAN\n");
		else if(yf!=0)
			printf("NOT INDIAN\n");
		else
			printf("NOT SURE\n");	
	}
	return 0;
}