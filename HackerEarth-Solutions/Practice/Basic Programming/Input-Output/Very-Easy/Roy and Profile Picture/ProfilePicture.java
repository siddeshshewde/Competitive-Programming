
import java.util.Scanner;

class ProfilePicture
{
    public static void main(String args[] )
    {
        Scanner sc = new Scanner(System.in);
        int l = sc.nextInt();
        int n = sc.nextInt();
        for (int i =0;i<n;i++)
        {
            int a = sc.nextInt();
            int b = sc.nextInt();
            if (a>=b && a>=l && a==b)
                System.out.print("ACCEPTED\n");
            if (a<l || b<l)
                System.out.print("UPLOAD ANOTHER\n");
            if (a>=l && b>=l && a!=b)
                System.out.print("CROP IT\n");
        }
    }
}