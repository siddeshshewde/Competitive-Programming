public class Solution
{
	public static void main(String []args)
	{
		int ans = 0;
		for(int i=0;i<1000;i++)
		{
			if (i%3==0 || i%5==0)
				ans = ans + i;
		}
		System.out.print(ans);
	}
}