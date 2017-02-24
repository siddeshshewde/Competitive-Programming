public class Solution
{
	public static void main(String args[])
	{
		int sum=0;
		int i=2;
		while (i<2000000)
		{
			int k=2;
			while (k<i)
			{
				if(i%k==0)
					break;
				k++;
			}
			if(k==i)
			{
				sum = sum+k;
			}
			
		}
		System.out.print(sum);
	}
}