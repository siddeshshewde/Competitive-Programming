public class Solution
{
	public static void main(String args[])
	{
		int n = 100,sum=0;
		float fact = 1;
		for (i=1;i<=n;i++)
		{
			fact = fact*i;
		}
		while(fact>0)
		{
			sum = sum + fact%10;
			fact = fact/10;
		}
		System.out.print(sum);
	}
}