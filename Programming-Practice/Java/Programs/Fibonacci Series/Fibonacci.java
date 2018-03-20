import java.util.Scanner;

class Fibonacci
{
	public static void main (String args[])
	{
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int a=0,b=1,c=0;
		System.out.print("0\n1\n");
		for (int i = 1 ; i < n-1 ; i++)
		{
			c = a + b;
			System.out.println(c);
			a = b;
			b = c;
		}
	}
}