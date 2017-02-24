import java.math.BigInteger;
 
 
public class Solution {
    public static void main(String args[])
    {
        BigInteger result = BigInteger.ZERO;
        BigInteger two = BigInteger.valueOf(2);
        BigInteger one_thousand = BigInteger.valueOf(1000);
        result = pow(two, one_thousand);
        String string_result = new String(result.toString());
         
        int Answer = 0;
        for (int i = 0; i < string_result.length(); i++)
        {
            Character c = new Character(string_result.charAt(i));
            String s = c.toString();
            int n = Integer.parseInt(s);
            Answer = Answer + n;
        }
 
        System.out.println(Answer);
 
    }
     
    public static BigInteger pow(BigInteger base, BigInteger exponent)
    {
        BigInteger result = BigInteger.ONE;
        while (exponent.signum() > 0)
        {
            if (exponent.testBit(0)) result = result.multiply(base);
            base = base.multiply(base);
            exponent = exponent.shiftRight(1);
        }
          return result;
    }
 
}