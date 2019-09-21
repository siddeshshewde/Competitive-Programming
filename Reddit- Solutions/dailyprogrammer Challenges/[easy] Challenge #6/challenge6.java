import java.math.BigDecimal;
import java.util.Scanner;


public class Find_PI_to_the_Nth_Digit{

    public static void main(String []args){
        
        //Initialize PI as 22/7 using BigDecimal as the limit of characters is skyhigh
        BigDecimal numerator = new BigDecimal(22.0);
        BigDecimal denominator = new BigDecimal(7.0);
        
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter the number of deciaml places to display : ");
        
        //Take Input for number of decimal places.
        int i = sc.nextInt();
        
        //Actual Calculation
        System.out.println(numerator.divide(denominator, i , BigDecimal.ROUND_UP));

    }
}