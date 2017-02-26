import java.util.Scanner;

class Product {
    public static void main(String args[] ) 
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long product = 1;
        for (int i=0;i<n;i++)
        {   
            int a = sc.nextInt();
            product = (product * (a % 1000000007)) % 1000000007;
        }
        System.out.print(product);
    }
}
