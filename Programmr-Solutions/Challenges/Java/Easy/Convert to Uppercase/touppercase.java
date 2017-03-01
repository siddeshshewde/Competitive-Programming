import java.io.*;
import java.util.Scanner;

class touppercase
{
  public static void main(String[] args) throws IOException
  {
   
    String str;
    
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    System.out.println("Enter a string:"); 
    str = br.readLine();

    System.out.println(str.toUpperCase());
    
  }
}





