#include<stdio.h>
#include<string.h>
void main() {
     int t;
     scanf("%d",&t);
     while(t>0)
     {
          char ex[400];
          char stack[400],res[400];
          int i=0,l=0,flag=0;int len=0;
       	scanf("%s",ex);
       	
	
	len=strlen(ex);
	for(i=0;i<400;i++){
	     stack[i]=0;
	     res[i]=0;
	}
	i=0;
     while(i!=len){
	     if(ex[i]=='('){
               }
	     else if(ex[i]=='+'||ex[i]=='-'||ex[i]=='*'||ex[i]=='/'||ex[i]=='^'||ex[i]=='%')
		    {
               stack[l]=ex[i];
			l++;
            }
         else if(ex[i]==')'){
		     res[flag]=stack[l-1];
			stack[l-1]=0;
     		l--;
			flag++;
			
              }
          
          else
               {    
               res[flag]=ex[i];
			flag++;	
               }
          i++;     
          }  
	
         i=0;
         while(i!=len){
	     if(res[i]!=0){
          printf("%c",res[i]);
	     }
          i++;
         }
printf("\n");
     t--;
	}	
}