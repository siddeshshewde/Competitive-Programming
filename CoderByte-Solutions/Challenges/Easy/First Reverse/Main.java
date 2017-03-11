//https://coderbyte.com/information/First%20Reverse

import java.util.*; 
import java.io.*;

class Main {  
  public static String FirstReverse(String str) { 
  
    return new StringBuffer(str).reverse().toString();
    
  } 
  
  public static void main (String[] args) {  
    // keep this function call here     
    Scanner s = new Scanner(System.in);
    System.out.print(FirstReverse(s.nextLine())); 
  }   
  
}