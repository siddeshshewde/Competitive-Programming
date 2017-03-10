//https://coderbyte.com/editor/guest:First%20Factorial:Java

import java.util.*; 
import java.io.*;

class Main {  
  public static int FirstFactorial(int num) { 
    int result = 1;
    for (int i=1;i<=num;i++)
    {
        result = result * i;
    }
    return result;
    
  } 
  
  public static void main (String[] args) {  
    // keep this function call here     
    Scanner s = new Scanner(System.in);
    System.out.print(FirstFactorial(s.nextLine())); 
  }   
  
}