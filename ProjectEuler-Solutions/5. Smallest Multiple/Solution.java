public class Solution
{
	public static void main(String args[])
	{
		int j;
		for(int i=1;;i++)
		{
			for(j=1;j<21;j++)
			{
				if(i%j!=0)
					break;
			}
			if(j==21)
			{
				System.out.print(i);
				break;
			}
		}
	}
}