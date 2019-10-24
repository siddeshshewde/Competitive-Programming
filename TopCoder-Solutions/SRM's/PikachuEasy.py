# Problem      : PikachuEasy
# Used In      : SRM 533
# Date         : 02.18.2012
# Category     : String Parsing
# Division     : 2
# Level        : 1
# Round        : 1  
# Points       : 250
# Difficulty   : Easy
# Problem Type : Single
# Description  : https://community.topcoder.com/stat?c=problem_statement&pm=11783

# Class Name   : PikachuEasy
# Method Name  : check
# Return Type  : String

"""
## Problem Statement
Pikachu is a well-known character in the Pokemon anime series. Pikachu can speak, but only 3 syllables: "pi", "ka", and "chu". 
Therefore Pikachu can only pronounce strings that can be created as a concatenation of one or more syllables he can pronounce. 
For example, he can pronounce the words "pikapi" and "pikachu".

You are given a String word. Your task is to check whether Pikachu can pronounce the string. 
If the string can be produced by concatenating copies of the strings "pi", "ka", and "chu", return "YES" 
(quotes for clarity). Otherwise, return "NO".

## Definition
Class:	PikachuEasy
Method:	check
Parameters:	String
Returns:	String
Method signature:	String check(String word)
(be sure your method is public)

## Limits
Time limit (s): 840.000
Memory limit (MB): 64

## Constraints
- word will contain between 1 and 50 characters, inclusive.
- Each character of word will be a lowercase letter ('a'-'z').

## Examples

"pikapi"
Returns: "YES"
"pikapi" = "pi" + "ka" + "pi", so Pikachu can say it.

"pipikachu"
Returns: "YES"
This time we have "pipikachu" = "pi" + "pi" + "ka" + "chu", so Pikachu can say it as well.

"pikaqiu"
Returns: "NO"
Pikachu can't say "pikaqiu" since 'q' does not appear in "pi", "ka", or "chu".

"topcoder"
Returns: "NO"

"piika"
Returns: "NO"

"chupikachupipichu"
Returns: "YES"

"pikapipachu"
Returns: "NO"

**This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2010, TopCoder, Inc. All rights reserved.**

"""

#Solution
class PikachuEasy:
    def check(word):
        word = word.replace('pi','').replace('ka','').replace('chu','')
        return "YES" if word == '' else "NO"


# Points Received : 249.96