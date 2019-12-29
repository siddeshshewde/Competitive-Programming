/*
# Problem      : ArrayHash
# Used In      : SRM 238
# Date         : 04.14.2005
# Category     : Brute Force, Simple Search, Iteration
# Division     : 2
# Level        : 1
# Round        : 1  
# Points       : 250
# Difficulty   : Easy
# Problem Type : Single
# Description  : https://community.topcoder.com/stat?c=problem_statement&pm=4503

# Class Name   : ArrayHash
# Method Name  : getHash
# Return Type  : int

## Problem Statement
You will be given a String[] input. The value of each character in input is computed as follows:
   Value = (Alphabet Position) + (Element of input) + (Position in Element) 

All positions are 0-based. 'A' has alphabet position 0, 'B' has alphabet position 1, ... The returned hash is the sum of all character values in input. For example, if
input = {"CBA",
         "DDD"}

then each character value would be computed as follows:
2 =   2 + 0 + 0   :  'C' in element 0 position 0
2 =   1 + 0 + 1   :  'B' in element 0 position 1
2 =   0 + 0 + 2   :  'A' in element 0 position 2
4  =  3 + 1 + 0   :  'D' in element 1 position 0
5  =  3 + 1 + 1   :  'D' in element 1 position 1
6  =  3 + 1 + 2   :  'D' in element 1 position 2
The final hash would be 2+2+2+4+5+6 = 21.

## Definition
Class:  ArrayHash
Method: getHash
Parameters: String[]
Returns:    int
Method signature:   int getHash(String[] input)
(be sure your method is public)

## Limits
Time limit (s): 840.000
Memory limit (MB): 64

## Constraints
-   input will contain between 1 and 50 elements inclusive.
-   Each character in each element of input will be a capital letter ('A'-'Z').
-   Each element of input will contain between 1 and 50 characters inclusive.
-   Each element of input will contain the same number of characters.

## Examples

{"CBA",
 "DDD"}
Returns: 21
From the problem statement.
        
{"Z"}
Returns: 25
A very small example.
        
{"A",
 "B",
 "C",
 "D",
 "E",
 "F"}
Returns: 30
Tall and narrow.
        
{"ABCDEFGHIJKLMNOPQRSTUVWXYZ",
 "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
 "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
 "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
 "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
 "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
Returns: 4290
        
{"ZZZZZZZZZZ"}
Returns: 295


**This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2010, TopCoder, Inc. All rights reserved.**

*/

//Solution
public class ArrayHash
{
    public static int getHash(String [] input)
    {
        int sum = 0;
        for (int i = 0 ; i < input.length ; i++)
        {
            for (int j = 0 ; j < input[i].length() ; j++)
            {
                sum += input[i].charAt(j) - 'A' + i + j;
            }
        }
        return sum;
    }
}

// Points Received: 249.92