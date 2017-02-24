public class Solution
{
	public static void main(String args[])
	{
		int ans=0,answer=0;
		for (int i=1;i<101;i++)
		{
			ans=ans+(i*i);
		}
		for (int i=1;i<101;i++)
		{
			answer=answer+i;
		}
		answer = answer*answer;
		System.out.println(ans-answer);
	}
}