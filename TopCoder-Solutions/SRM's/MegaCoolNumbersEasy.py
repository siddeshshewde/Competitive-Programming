# Problem      : MegaCoolNumbersEasy
# Used In      : SRM 431
# Date         : 12.23.2008
# Category     : Simple Search, Iteration
# Division     : 2
# Level        : 1
# Round        : 1  
# Points       : 250
# Difficulty   : Easy
# Problem Type : Single
# Description  : https://community.topcoder.com/stat?c=problem_statement&pm=10281

# Class Name   : MegaCoolNumbersEasy
# Method Name  : count
# Return Type  : String  

"""


## Problem Statement
A positive integer is called a mega cool number if its digits form an arithmetic progression. An arithmetic progression is a sequence of numbers in which the difference between any two consecutive numbers is the same. Return the number of mega cool numbers between 1 and N, inclusive.

## Definition
Class: MegaCoolNumbersEasy
Method: count
Parameters: integer
Returns: integer
Method signature: def count(self, N):

## Limits
Time limit (s): 840.000
Memory limit (MB): 64

## Constraints
- N will be between 1 and 1,000, inclusive.

## Examples

1
Returns: 1
The only mega cool number not greater than 1 is 1.

110
Returns: 99
All numbers between 1 and 99 are mega cool.

500
Returns: 119

**This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.**

"""

#Solution
class MegaCoolNumbersEasy:
    
    def megaCool(n):
        count = 99
        
        while n > 100:
            a = n
            a1 = a % 10
            a2 = int(a / 10 % 10)
            a = int(a /100)
            if a - a2 == a2 - a1:
                count += 1
            n -= 1
        return count
    
    def count(n):
        return n if n < 100 else MegaCoolNumbersEasy.megaCool(n)

# Points Received - 248.69

"""
Another Solution using charAt:

public class MegaCoolNumbersEasy {
    public int count(int N) {
        int megaCool = 0;
        for (int i = 1; i <= N; i++) {
            if (isMegaCool(i)) {
                megaCool++;
            }
        }
        return megaCool;
    }

    boolean isMegaCool(int number) {
        String str = number + "";
        for (int i = 2; i < str.length(); i++) {
            if (str.charAt(i) - str.charAt(i - 1) != str.charAt(i - 1)
                    - str.charAt(i - 2)) {
                return false;
            }
        }
        return true;
    }
}

"""