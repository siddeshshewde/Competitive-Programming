import java.util.Scanner;

class TestClass {
    public static void main(String args[] )
    {
        Scanner sc = new Scanner(System.in);
        
        int l = sc.nextInt();
        int r = sc.nextInt();
        int k = sc.nextInt();
        int count = 0;
        for (int i=l;i<=r;i++)
        {
            if (i % k ==0)
                count++;
        }
        System.out.print(count);
    }
}