/*
# Problem      : LetterStrings
# Used In      : SRM 100
# Date         : 04.30.2003
# Category     : Simple Math, String Manipulation
# Division     : 2
# Level        : 1
# Round        : 1  
# Points       : 250
# Difficulty   : Easy
# Problem Type : Single
# Description  : https://community.topcoder.com/stat?c=problem_statement&pm=961

# Class Name   : LetterStrings
# Method Name  : sum
# Parameter    : String[]
# Return Type  : Int

"""
## Problem Statement
A letter-string is composed of letters ('A'-'Z','a'-'z') and dashes ('-'). The length of a letter-string is the number of characters in it not including dashes (in other words, the number of letters in the string). Given a list of letter-strings you will return the sum of their lengths.

Create a class LetterStrings that contains the method sum, which takes a String[], s, and returns an int representing the sum of the lengths of the given letter-strings.

## Definition
Class:	LetterStrings
Method:	sum
Parameters:	String[]
Returns:	int
Method signature:	int sum(String[] s)
(be sure your method is public)

## Limits
Time limit (s): 840.000
Memory limit (MB): 64

## Constraints
-	s will contain between 1 and 50 elements, inclusive.
-	Each element of s will have length between 1 and 50, inclusive.
-	Each element of s will contain only letters ('A'-'Z','a'-'z') and dashes ('-').

## Examples

 	
{"-"}
Returns: 0
    	
{"A"}
Returns: 1
    	
{"-----Abc"}
Returns: 3
    	
{"-A-B-C-D", "--------EFGHI", "JKLMNOPQR", "---STU-VW-XYZ"}
Returns: 26

**This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2010, TopCoder, Inc. All rights reserved.**

*/

//Solution
public class LetterStrings {

    public int sum(String[] s) {
        int sum = 0;
        for (String letter : s) {
            for (int j = 0; j < letter.length(); j++) {
                if (letter.charAt(j) != '-') {
                    sum++;
                }

            }
        }
        return sum;
    }
}
// Points Received : 248.6
