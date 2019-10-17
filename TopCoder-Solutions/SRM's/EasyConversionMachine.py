# Problem      : EasyConversionMachine
# Used In      : SRM 550
# Date         : 07.21.2012
# Category     : Simple Math
# Division     : 2
# Level        : 1
# Round        : 1  
# Points       : 250
# Difficulty   : Easy
# Problem Type : Single
# Description  : https://community.topcoder.com/stat?c=problem_statement&pm=12125

# Class Name   : EasyConversionMachine
# Method Name  : isItPossible
# Return Type  : String  

"""

## Problem Statement
We have a String originalWord. Each character of originalWord is either 'a' or 'b'. Timmy claims that he can convert it to finalWord using exactly k moves. In each move, he can either change a single 'a' to a 'b', or change a single 'b' to an 'a'.

You are given the Strings originalWord and finalWord, and the int k. Determine whether Timmy may be telling the truth. If there is a possible sequence of exactly k moves that will turn originalWord into finalWord, return "POSSIBLE" (quotes for clarity). Otherwise, return "IMPOSSIBLE".

## Definition
Class:	EasyConversionMachine
Method:	isItPossible
Parameters:	String, String, int
Returns:	String
Method signature:	String isItPossible(String originalWord, String finalWord, int k)
(be sure your method is public)

## Limits
Time limit (s): 840.000
Memory limit (MB): 64

## Notes
- Timmy may change the same letter multiple times. Each time counts as a different move.

## Constraints
- originalWord will contain between 1 and 50 characters, inclusive.
- finalWord and originalWord will contain the same number of characters.
- Each character in originalWord and finalWord will be 'a' or 'b'.
- k will be between 1 and 100, inclusive.

## Examples

"aababba"
"bbbbbbb"
2
Returns: "IMPOSSIBLE"
It is not possible to reach finalWord in fewer than 4 moves.
    	
"aabb"
"aabb"
1
Returns: "IMPOSSIBLE"
The number of moves must be exactly k=1.
    	
"aaaaabaa"
"bbbbbabb"
8
Returns: "POSSIBLE"
Use each move to change each of the letters once.
    	
"aaa"
"bab"
4
Returns: "POSSIBLE"
The following sequence of 4 moves does the job:
aaa -> baa -> bab -> aab -> bab
    	
"aababbabaa"
"abbbbaabab"
9
Returns: "IMPOSSIBLE"
"""

#Solution
class EasyConversionMachine:
    def isItPossible(self, originalWord, finalWord, maxMoves):
        moves = 0
        for i in range(0, len(originalWord)):
            if originalWord[i] != finalWord[i]: moves += 1
        
        try:
            return "POSSIBLE" if moves == maxMoves or (maxMoves > moves and maxMoves % moves == 0) else "IMPOSSIBLE"
        except: 
            return "IMPOSSIBLE"    

# Points Received - 248.31

"""
Have used modulus as it is possible to covert into the final word in more than the max moves.

Example: 

Original Word : "aaa"
Final Word    : "bab"
Max Moves     : 4

Returns: "POSSIBLE"

The following sequence of 4 moves does the job:
aaa -> baa -> bab -> aab -> bab

"""