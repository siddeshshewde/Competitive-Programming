import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.math.BigInteger;
 
 
public class HelloWorld {
    public static void main(String [] args) {
        try
        {
           FileReader fro = new FileReader( "one-hundred_50.txt" );
           BufferedReader bro = new BufferedReader( fro );
       
           BigInteger tally = BigInteger.ZERO;
          
           String line;
           while ((line = bro.readLine()) != null)   {
               BigInteger bi = new BigInteger(line);
               tally = tally.add(bi);
           }
           System.out.println("tally = " + tally);
        }
        catch( FileNotFoundException filenotfoundexcption )
           {
             System.out.println( "one-hundred_50.txt, does not exist" );
           }
          
        catch( IOException ioexception )
           {
             ioexception.printStackTrace( );
           }
    }
 
}