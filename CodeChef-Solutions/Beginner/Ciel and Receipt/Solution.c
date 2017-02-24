#include<stdio.h>
#include <math.h>
int main() {
 int t,i, p, arr[12], count;
 for(i=0; i<12; i++) arr[i]=pow(2, i);
 scanf("%d",&t);
 while(t--) {
  count=0;
  scanf("%d",&p);
  while(p>0) {
   for(i=11; i>=0; i--) {
    if(p>=arr[i]) {
     p=p-arr[i]; count++; i++;
    }
   }
  }
  printf("%d\n",count);
 }
 return 0;
}