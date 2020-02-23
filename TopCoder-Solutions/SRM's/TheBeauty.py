# Problem      : TheBeauty
# Used In      : SRM 437
# Date         : 03.24.2009  
# Category     : Simulation
# Division     : 2
# Level        : 1
# Round        : 1  
# Points       : 250
# Difficulty   : Easy
# Problem Type : Single
# Description  : https://community.topcoder.com/stat?c=problem_statement&pm=10233

# Class Name   : TheBeauty  
# Method Name  : find   
# Return Type  : Int  
# Arg Types    : (tuple (integer))  

"""
## Problem Statement
There is nothing more beautiful than just an integer number.

The beauty of an integer is the number of distinct digits it contains in decimal notation.

You are given an integer number n. Return the beauty of this number.

## Definition
Class:  TheBeauty
Method: find
Parameters: int
Returns:    int
Method signature:   int find(int n)
(be sure your method is public)

## Limits
Time limit (s): 840.000  
Memory limit (MB): 64

## Notes

- You can only edit digits, not add new ones. In particular, if a number on the report only has one digit, it must remain a one-digit number.


## Constraints
-   n will be between 1 and 1,000,000,000, inclusive.

## Examples

    
7
Returns: 1
Just one digit.
        
100
Returns: 2
Two distinct digits - 0 and 1.
        
123456789
Returns: 9
All the digits are different.
        
1000000000
Returns: 2
        
932400154
Returns: 7

**This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information 
without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2010, TopCoder, Inc. All rights reserved.**
"""

#Solution

class TheBeauty:

    def find(self, number):

        snumber = set(str(number))
        return len(snumber)
        
# Points Received - 196.57
