import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(); // the number of temperatures to analyse
        if(n==0)
        {
            System.out.print(0);
        }
        int ans=0;
        if(n!=0)
            ans = in.nextInt();
        
        for (int i = 1; i < n; i++) {
            int t = in.nextInt(); // a temperature expressed as an integer ranging from -273 to 5526
            if(t==0)
            {
                ans=0;
                break;
            }
            if (t>0)
            {
                if(t<=Math.abs(ans))
                    ans = t;
            }
            else if (t<0)
            {
                if(Math.abs(t)<Math.abs(ans))
                {
                    if (Math.abs(t)!=Math.abs(ans))
                        ans = t;
                }
            }
        }

        if(n!=0)
        	System.out.println(ans);
    }
}