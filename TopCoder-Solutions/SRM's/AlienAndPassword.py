# Problem      : AlienAndPassword
# Used In      : SRM 605
# Date         : 01.21.2014  
# Category     : Brute Force, String Manipulation
# Division     : 2
# Level        : 1
# Round        : 1  
# Points       : 250
# Difficulty   : Easy
# Problem Type : Single
# Description  : https://community.topcoder.com/stat?c=problem_statement&pm=12950

# Class Name   : AlienAndPassword  
# Method Name  : getNumber   
# Return Type  : Int  
# Arg Types    : String  

"""
## Problem Statement
Alien Fred wants to destroy the Earth, but he forgot the password that activates the planet destroyer.

You are given a String S. Fred remembers that the correct password can be obtained from S by erasing exactly one character.

Return the number of different passwords Fred needs to try.

## Definition
Class:	AlienAndPassword
Method:	getNumber
Parameters:	String
Returns:	int
Method signature:	int getNumber(String S)
(be sure your method is public)

## Limits
Time limit (s): 840.000  
Memory limit (MB): 64

## Constraints
-	S will contain between 1 and 50 characters, inclusive.
-	Each character in S will be an uppercase English letter ('A'-'Z').

## Examples

"A"
Returns: 1
In this case, the only password Fred needs to try is an empty string.
	
    	
"ABA"
Returns: 3
The following three passwords are possible in this case: "BA", "AA", "AB".
	
    	
"AABACCCCABAA"
Returns: 7
	
    	
"AGAAGAHHHHFTQLLAPUURQQRRRUFJJSBSZVJZZZ"
Returns: 26
    	
"ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"
Returns: 1
Regardless of which character we erase, we will always obtain the same string. Thus there is only one possible password: the string that consists of 49 'Z's.

**This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information 
without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.**
"""

#Solution
class AlienAndPassword:
    def getNumber(self, s):
        
        n = 1
        
        for i in range (1, len(s)):
            if s[i] != s[i-1]: 
                n = n+1
        
        return n        

# Points Received - 249.89