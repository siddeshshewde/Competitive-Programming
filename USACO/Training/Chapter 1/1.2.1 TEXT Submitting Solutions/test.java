/*
Title:
	The First Challenge

Link:
	https://train.usaco.org/usacotext2?a=Di95zySl5wx&S=grade

Description:
	The simplest programming challenge is named 'test' and requires you to read a pair of small integers from a single input line in the file 'test.in' and print their sum to the file 'test.out'.

*/





/*
ID   : siddesh3
LANG : JAVA
TASK : test
*/

import java.util.*;
import java.io.*;

public class test 
{
	public static void main (String [] args) throws IOException
	{
		BufferedReader in = new BufferedReader (new FileReader ("test.in"));

		PrintWriter out = new PrintWriter(new FileWriter("test.out"));

		StringTokenizer st = new StringTokenizer(in.readLine());

		int a = Integer.parseInt(st.nextToken());
		int b = Integer.parseInt(st.nextToken());

		out.println(a+b);

		out.close();

	}

}