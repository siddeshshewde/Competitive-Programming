/*
# Problem      : InsideOut
# Used In      : SRM 224
# Date         : 12.22.2004
# Category     : String Manipulation
# Division     : 2
# Level        : 1
# Round        : 1  
# Points       : 250
# Difficulty   : Easy
# Problem Type : Single
# Description  : https://community.topcoder.com/stat?c=problem_statement&pm=3452

# Class Name   : InsideOut
# Method Name  : unscramble
# Return Type  : String
# Arg Type     : String

"""
## Problem Statement
Your printer has been infected by a virus and is printing gibberish. After staring at several printed pages for a while, 
you realize that it is printing every line inside-out. In other words, the left half of each line is being printed starting 
in the middle of the page and proceeding out toward the left margin. Similarly, the right half of each line is being printed 
starting at the right margin and proceeding in toward the middle of the page. For example, the line
    THIS LINE IS GIBBERISH
is being printed as
    I ENIL SIHTHSIREBBIG S
Your task is to unscramble a String line from its printed form back into its original order. You can assume that line contains 
an even number of characters.

## Definition
Class:	InsideOut
Method:	unscramble
Parameters:	String
Returns:	String
Method signature:	String unscramble(String line)
(be sure your method is public)

## Limits
Time limit (s): 840.000
Memory limit (MB): 64

## Constraints
- line contains between 2 and 50 characters, inclusive.
- line contains an even number of characters.
- line contains only uppercase letters ('A'-'Z') and spaces (' ').

## Examples

"I ENIL SIHTHSIREBBIG S"
Returns: "THIS LINE IS GIBBERISH"
The example above.
    	
"LEVELKAYAK"
Returns: "LEVELKAYAK"
    	
"H YPPAHSYADILO"
Returns: "HAPPY HOLIDAYS"
    	
"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Returns: "MLKJIHGFEDCBAZYXWVUTSRQPON"
    	
"RUT OWT SNEH HCNERF EERHTEGDIRTRAP A DNA  SEVODELT"
Returns: "THREE FRENCH HENS TWO TURTLEDOVES  AND A PARTRIDGE"

**This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.**

*/

//Solution
public class InsideOut {
	public String unscramble(String line) {
		return new StringBuffer(line.substring(0, line.length() / 2)).reverse()
				.toString()
				+ new StringBuffer(line.substring(line.length() / 2)).reverse()
						.toString();
	}
}

// Points Received : 216.05