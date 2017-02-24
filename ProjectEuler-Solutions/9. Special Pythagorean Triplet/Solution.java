public final class Solution
{

	public static void main(String[] args)
	{
		int a,b,c;
		for (a=1;a<1000;a++)
		{
			for (b=1;b<1000;b++)
			{
				c=1000-(a*a+b*b);
				if(a*a+b*b==c*c)
				{
					System.out.print(a*b*c);
					break;
				}
			}
			if(a+b+c==1000)
				{
					break;
				}
		}
	}
}