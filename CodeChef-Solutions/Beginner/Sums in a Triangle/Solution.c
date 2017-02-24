#include <stdio.h>
 
int mat[100][100];
 
int max(int x, int y){
  if(x>y)
    return x;
  else
    return y;
}
 
int solve(int x){
  int k,l;
 
  if(x==1)
    return mat[0][0];
  
  for(k=x-2;k>=0;k--){
    for(l=0;l<=k;l++){
      mat[k][l] += max(mat[k+1][l],mat[k+1][l+1]);
    }
  }
 
  return mat[0][0];
}
 
int main(){
  int i,j,k,l,w;
  scanf("%d",&j);
  int x;
 
  for (i=0;i<j;i++){
    scanf("%d",&x);    
    for(k=0;k<x;k++){
      for(l=0;l<k+1;l++){
        scanf("%d",&w);  
        mat[k][l]=w;
      }
    }
    printf("%d\n",solve(x));
  }  
 
return 0;
}