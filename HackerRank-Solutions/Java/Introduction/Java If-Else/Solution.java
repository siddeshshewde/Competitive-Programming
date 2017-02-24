    import java.io.*;
    import java.util.*;
    import java.text.*;
    import java.math.*;
    import java.util.regex.*;

    public class Solution {

        public static void main(String[] args) {

            Scanner sc = new Scanner(System.in);
            int n = sc.nextInt();
            if ( n%2 != 0 )
                   System.out.println("Weird");
            if ( n%2 == 0 && n>1 && n<6)
                   System.out.println("Not Weird");
            if ( n%2 == 0 && n>5 && n<21)
                    System.out.println("Weird");
            if ( n%2 == 0 && n>21)
                    System.out.println("Not Weird");
        }
    }
