#include<iostream>
	using namespace std;
	
	int main()
	{
		 int arr[200],m,x,temp=0,n,t;
		 cin>>t;
		 while(t)
		 {
		 cin>>n;
		 arr[0]=1;
		 m=1;
		 for(int mult=1;mult<=n;mult++)		 
		 {
		   for(int i=0;i<m;i++)
		  {
		  	x=arr[i]*mult+temp;
		  	arr[i]=x%10;
		  	temp=x/10;
		  }
		  while(temp)
		  {
			arr[m]=temp%10;
		  	temp=temp/10;
		  	m++;
		  } 
	    }
	    for(int i=m-1;i>=0;i--)
		{
		  	cout<<arr[i];
		   }
		 cout<<endl;
		 t--;
    }
} 