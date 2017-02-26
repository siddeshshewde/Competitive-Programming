import java.util.Scanner;
class Factorial
{
    public static void main(String args[] ) throws Exception
	{
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int ans = 1;
        while (n != 1)
        {
            ans = ans * n;
            n--;
        }
        System.out.print(ans);
    }
}
