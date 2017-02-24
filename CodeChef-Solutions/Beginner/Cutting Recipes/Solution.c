include <stdio.h>
int main() {
     int  t=0; 
	scanf("%d",&t);
	while(t>0){
	     int flag=1;int a[50];
	     int n,i=0,small=0;
	     scanf("%d",&n);
		
		while(i!=n){
		     scanf("%d",&a[i]);
		     i++;
		}
		small=a[0];
		i=0;
		while(i!=n){
		     if(a[i]<small){
		          small=a[i];
		     }
		     i++;
		}
	//	printf("Small: %d\t",small);
		
		for(small;small>1;small--){
		   if(flag==1)
		   { i=0;
		        while(i!=n)
		        {
		          if(a[i]%small==0)
		          {
		              flag=0;
		          }
		         else {
		              flag=1;
		              break;
		         }
		         i++;
		    } 
		  }
		  else break;
	}
	//	printf("Flag: %d\t",flag);
	 //  printf("Small: %d\t",small);
		if(flag==1){	i=0;
		   while(i!=n){
		        printf("%d ",a[i]);
		        i++;
		   }  
		}
		
		else {i=0;
		     
		     while(i!=n){
		          printf("%d ",a[i]/(small+1));
		          i++;
		     }
		}
		printf("\n");
	     t--;
	}
	return 0;
}