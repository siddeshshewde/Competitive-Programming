import java.util.Scanner;

class TestClass
{
    public static void main(String args[] )
    {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        String text = Integer.toString(a);
        if(text.contains("000000") || text.contains("111111"))
            System.out.print("Sorry, sorry!");
        else
            System.out.print("Good luck!");
    }
}