/*
Title:
	Greedy Gift Givers

Link:
	https://train.usaco.org/usacoprob2?a=sR33WcbUPbP&S=gift1

Description:
	A group of NP (2 ≤ NP ≤ 10) uniquely named friends has decided to exchange gifts of money. Each of these friends might or might not give some money to some or all of the other friends (although some might be cheap and give to no one). Likewise, each friend might or might not receive money from any or all of the other friends. Your goal is to deduce how much more money each person receives than they give.

	The rules for gift-giving are potentially different than you might expect. Each person goes to the bank (or any other source of money) to get a certain amount of money to give and divides this money evenly among all those to whom he or she is giving a gift. No fractional money is available, so dividing 7 among 2 friends would be 3 each for the friends with 1 left over – that 1 left over goes into the giver's "account". All the participants' gift accounts start at 0 and are decreased by money given and increased by money received.

	In any group of friends, some people are more giving than others (or at least may have more acquaintances) and some people have more money than others.

	Given:

	a group of friends, no one of whom has a name longer than 14 characters,
	the money each person in the group spends on gifts, and
	a (sub)list of friends to whom each person gives gifts,
	determine how much money each person ends up with.

Example:	
	Input:
		5
		dave
		laura
		owen
		vick
		amr
		dave
		200 3
		laura
		owen
		vick
		owen
		500 1
		dave
		amr
		150 2
		vick
		owen
		laura
		0 2
		amr
		vick
		vick
		0 0

	Output:
		dave 302
		laura 66
		owen -359
		vick 141
		amr -150
	
*/



/*
ID   : siddesh3
LANG : JAVA
TASK : gift1
PROG : gift1
*/

import java.util.*;
import java.io.*;

public class gift1
{
	public static void main(String args []) throws IOException
	{
		BufferedReader br = new BufferedReader(new FileReader("gift1.in"));
		PrintWriter out  = new PrintWriter(new FileWriter("gift1.out"));

		int friends = Integer.parseInt(br.readLine());
		LinkedHashMap <String, Integer> friendNames = new LinkedHashMap<String, Integer>();

		for (int i = 0 ; i < friends ; i++)
		{
			friendNames.put(br.readLine(), 0);
		}

		for (int i = 0 ; i < friends ; i++)
		{
			String giver = br.readLine();
			String a [] = br.readLine().split(" ");
			int amount = Integer.parseInt(a[0]);
			int takers = Integer.parseInt(a[1]);
			int split = 0;

			if (takers != 0)
				split = amount/takers;

			friendNames.put(giver, friendNames.get(giver) - split * takers);

			for (int j = 0 ; j < takers ; j++)
			{
				String taker = br.readLine();
				friendNames.put(taker, friendNames.get(taker) + split);
			}

		}

		for (String key : friendNames.keySet())
		{
			String r = key + " " + friendNames.get(key);
			out.println(r);
		}

		out.close();     //close the output file
		System.exit(0);  //don't omit this

	}

}