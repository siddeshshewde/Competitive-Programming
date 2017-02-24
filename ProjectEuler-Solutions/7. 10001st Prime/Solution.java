public class Solution
{
	public static void main(String args[])
	{
		int n=10001,j=1;
		for (int i=3;;i++)
		{
			int k=2;
			while (k<i)
			{
				if (i%k==0)
					break;
				k++;
			}
			if(k==i)
			{
				j++;
				if(j==n)
				{
					System.out.println(i);
					break;
				}
			}
		}
	}
}