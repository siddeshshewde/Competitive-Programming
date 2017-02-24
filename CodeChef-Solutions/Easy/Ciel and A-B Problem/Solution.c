#include<stdio.h>
int main(){
 
int num1, num2;
int diff;
int dividend, remaind;
int new_rem=0;
int answer=0;
 
scanf("%d%d",&num1, &num2);
diff = num1-num2;
 
if(diff<0)
diff = -diff;
 
dividend = diff/10;
remaind = diff%10;
 
 
 
if(remaind == 0)
        new_rem = 5;
else if(remaind > 5)
        new_rem = remaind - 1;
else
        new_rem = remaind + 1;
 
diff -= remaind;
diff += new_rem;
//answer = dividend*10 + new_rem;
//printf("%d\n",answer);
 
printf("%d\n",diff);
 
return 0;
}