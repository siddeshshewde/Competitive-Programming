public class Solution
{
	public static void main(String []args)
	{
		int i,start=0,max=0,count;
		for(i=2;i<=1000000;i++)
		{
			count=1;
			long k=i;
			while(k>1)
			{
				if(k%2==0)
				{
					k=k/2;
				}
				else
				{
					k=(3*k)+1;
				}
				count++;
			}
			if(count>max)
			{
				max=count;
				start = i;
			}
		}
		System.out.print(start);
	}
}