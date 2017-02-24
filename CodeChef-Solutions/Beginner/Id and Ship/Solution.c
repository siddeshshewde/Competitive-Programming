#include<stdio.h>
    typedef long long int ui;
    int main()
    {
    	int t;
    	scanf("%d",&t);
    	char ch;
    	while(t--)
    	{
    	    scanf(" %c",&ch);
    	    ch=toupper(ch);
    	    if(ch=='B' || ch=='b')
    	        printf("BattleShip\n");
    	    else if(ch=='C' || ch=='c')
    	        printf("Cruiser\n");
    	    else if(ch=='F' || ch=='f')
    	        printf("Frigate\n");
    	    else
    	        printf("Destroyer\n");
    	}
    	return 0;
    }