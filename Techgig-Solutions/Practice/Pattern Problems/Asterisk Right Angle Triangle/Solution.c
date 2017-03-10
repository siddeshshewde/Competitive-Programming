//https://www.techgig.com/practice/question/asterisk-right-angle-triangle/NTM3M0AjJEAjJDIwNjY4MDlAIyRAIyQzOTgwNTUxQCMkQCMkMTQ4OTE4MTIwOA==/1

/* Read input from STDIN. Print your output to STDOUT*/
#include<stdio.h>
int main(int argc, char *a[])
{
	int i,j,n;
	scanf("%d",&n);
	for(i=0;i<n;i++){
	    for(j=i;j>0;j--){
	        printf("* ");
	    }
	    printf("*\n");
	}
	return 0;
}