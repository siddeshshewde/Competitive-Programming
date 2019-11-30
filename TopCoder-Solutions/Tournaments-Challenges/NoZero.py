# Problem      : NoZero
# Used In      : TCO '04 Qualification - 2
# Date         : 02.23.2004
# Category     : Advanced Math
# Division     : 1
# Level        : 2
# Round        : 1  
# Points       : 650
# Difficulty   : Easy
# Problem Type : Single
# Description  : https://community.topcoder.com/stat?c=problem_statement&pm=1708

# Class Name   : NoZero
# Method Name  : subtract
# Return Type  : Integer

"""
## Problem Statement
A no-zero number system uses only the digits 1 through 9. So counting begins with 1, the first "counting number", 
and continues:
1,2,3,4,5,6,7,8,9,11,12,...,19,21,...,98,99,111,112,...

So, in this system 9 is the ninth counting number and 11 is the tenth counting number.

As usual, addition can be defined by reference to the counting sequence. Addition of the i-th counting number and 
the j-th counting number is defined to mean the (i+j)-th counting number. Thus, in this system 5 + 8 = 14, 
since 5 is the fifth counting number, 8 is the eighth, and 14 is the thirteenth counting number. 
Subtraction is the reverse of addition. Create a class NoZero that contains the method subtract that takes 
two no-zero numbers, big and small, and returns the no-zero value that results from calculating big - small.

## Definition
Class:  NoZero
Method: subtract
Parameters: int, int
Returns:    int
Method signature:   int subtract(int big, int small)
(be sure your method is public)

## Limits
Time limit (s):  840.000
Memory limit (MB): 64

## Constraints
-   big and small do not contain the digit 0
-   big is between 1 and 999,999,999 inclusive
-   small is between 1 and 999,999,999 inclusive
-   big is greater than small

## Examples
  
111
99
Returns: 1
This big and small are adjacent in the counting sequence. So 99 + 1 = 111 and 111 - 99 = 1.
        
19
11
Returns: 8
        
191
111
Returns: 79
        
11112
9989
Returns: 12

**This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.**

"""

#Solution
class NoZero:
    def subtract(big, small):
        count = 0
        for i in range(small, big):
            if '0' in str(i): count += 1
            
        countingNumber = big - small - count        
        
        count = 0
        for i in range(1,countingNumber):
            if '0' in str(i): count += 1
        
        return countingNumber + count

# Points Received : 195.0