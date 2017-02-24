public class Solution
{
	public static void main(String []args)
	{
		int sum=0,a=0,b=1,c=0;
		while(a<4000000 &&b<4000000)
		{
			c=a+b;
			if(c%2==0)
				sum+=c;
			a=b;
			b=c;
		}
		System.out.print(sum);
	}
}