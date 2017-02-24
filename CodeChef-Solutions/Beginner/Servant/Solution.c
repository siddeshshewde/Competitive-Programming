import java.util.*;
 
class a
{
	public static void main(String args[])
	{
		int n;
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		for (int i=0;i<n;i++)
		{
			int a;
			a= sc.nextInt();
			if (a < 10)
				System.out.println("What an obedient servant you are!");
			else
				System.out.println("-1");
		}
	}
} 