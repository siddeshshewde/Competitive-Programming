# Problem      : CheckFunction
# Used In      : SRM 271
# Date         : 11.08.2005
# Category     : Brute Force
# Division     : 2
# Level        : 1
# Round        : 1  
# Points       : 250
# Difficulty   : Easy
# Problem Type : Single
# Description  : https://community.topcoder.com/stat?c=problem_statement&pm=1708

# Class Name   : CheckFunction
# Method Name  : newFunction
# Return Type  : Integer
# Arg Type     : String

"""
## Problem Statement
You are given a code containing a message composed entirely of decimal digits ('0'-'9'). Each digit consists of some number of dashes (see diagram below). A "check function" of a message is defined as the total number of dashes in the message. Return the value of the check function for the message represented in code.

## Definition
Class: CheckFunction
Method: newFunction
Parameters: string
Returns: integer
Method signature: def newFunction(self, code)

## Limits
Time limit (s): 840.000
Memory limit (MB): 64

## Notes
- 0 consists of 6 dashes, 1 consists of 2 dashes, 2 consists of 5 dashes, 3 consists of 5 dashes, 4 consists of 4 dashes, 5 consists of 5 dashes, 6 consists of 6 dashes, 7 consists of 3 dashes, 8 consists of 7 dashes, 9 consists of 6 dashes.

## Constraints
- code will contain between 1 and 50 characters, inclusive.
- Each character in code will be a digit ('0'-'9').

## Examples

"13579"
Returns: 21
1 consists of 2 dashes;
3 consists of 5 dashes;
5 consists of 5 dashes;
7 consists of 3 dashes;
9 consists of 6 dashes;
2 + 5 + 5 + 3 + 6 = 21.

"02468"
Returns: 28

"73254370932875002027963295052175"
Returns: 157

**This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.**

"""

#Solution
class CheckFunction:
    def newFunction(self, Number):
        Dashes = {0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}
        
        sum = 0
        for i in Number:
            sum += Dashes[int(i)]
        
        return sum

# Points Received : 249.95

"""
Dictionary In Python : Dictionary in Python is an unordered collection of data values, used to store data values like a map, which unlike other Data Types that hold only single value as an element, Dictionary holds key:value pair. Key value is provided in the dictionary to make it more optimized. Each key-value pair in a Dictionary is separated by a colon :, whereas each key is separated by a ‘comma’.

Example of Nested Dict : Dict = {1: 'Geeks', 2: 'For', 3:{'A' : 'Welcome', 'B' : 'To', 'C' : 'Geeks'}} 
"""