public class Solution
{
	public static void main(String []arg)
	{
		int a,i,divisors,sum=0;
		for (i=1;;i++)
		{
			a=1;
			sum = sum+i;
			divisors=0;
			while (a<sum)
			{
				if(sum%a==0)
					divisors++;
				a++;
			}
			if(divisors>500)
				break;
		}
		System.out.print(sum);
	}
}