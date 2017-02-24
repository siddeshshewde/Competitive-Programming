public class Solution{
	
	public static void main(String args[])
	{
	
		int a,b,c;
		int ans=1;
		for (int i=100;i<1000;i++)
		{
			for (int j = i;j<1000;j++)
			{
				a=i*j;
				b=a;
				c=0;
				while(b>0)
				{
					c=c*10+(b%10);
					b=b/10;
				}
				if(c==a && a>ans)
				{
					ans = a;
				}
			}
		}
		System.out.print(ans);
	}
}