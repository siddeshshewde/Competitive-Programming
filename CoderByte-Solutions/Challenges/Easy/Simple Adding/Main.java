//https://coderbyte.com/information/Simple%20Adding

import java.util.*; 
import java.io.*;

class Main {  
  public static int SimpleAdding(int num) { 
  int ans = 0;
		for (int i=1;i<=num;i++)
		{
			ans = ans + i;
		}
    return ans;
    
  } 
  
  public static void main (String[] args) {  
    // keep this function call here     
    Scanner s = new Scanner(System.in);
    System.out.print(SimpleAdding(s.nextLine())); 
  }   
  
}