# Problem      : CheatingAfterTests
# Used In      : SRM 776
# Date         : 01.25.2020  
# Category     : Greedy, Simple Math, Simple Search, Iteration
# Division     : 2
# Level        : 1
# Round        : 1  
# Points       : 250
# Difficulty   : Easy
# Problem Type : Single
# Description  : https://community.topcoder.com/stat?c=problem_statement&pm=15901

# Class Name   : CheatingAfterTests  
# Method Name  : cheat   
# Return Type  : Int  
# Arg Types    : (tuple (integer))  

"""
## Problem Statement
In school you took some tests. Your score on each test was an integer between 0 (worst) and 99 (best), inclusive. After all the tests were done, you were given the report where all your scores are written. You are supposed to bring the report home and show it to your parents.

You aren't too happy with your scores, so you decided to improve the report: you may change any one digit to any other digit.

Do the change that will improve your report as much as possible. Compute and return the largest possible sum of all scores on your report card after you change up to one digit in one of the numbers.

## Definition
Class:	CheatingAfterTests
Method:	cheat
Parameters:	int[]
Returns:	int
Method signature:	int cheat(int[] report)
(be sure your method is public)

## Limits
Time limit (s): 840.000  
Memory limit (MB): 64

## Notes

- You can only edit digits, not add new ones. In particular, if a number on the report only has one digit, it must remain a one-digit number.


## Constraints
-	report will have between 1 and 50 elements, inclusive.
-	Each element of report will be between 0 and 99, inclusive.

## Examples

{51, 47, 93}
Returns: 241
The best improvement you can make here is to change the 47 into a 97. The sum of the scores on the fixed report card will be 51 + 97 + 93.
    	
{99, 99}
Returns: 198
This report cannot be improved, the best sum of scores you can get is 99 + 99. Therefore, the optimal solution is to do nothing.
    	
{4, 5, 7, 2}
Returns: 25
Here you should improve the 2 into a 9. Note that you cannot add new digits, you can only change the existing ones. (For example, you are not allowed to change the 4 into a 94.)
    	
{93, 97, 92, 99, 92, 93}
Returns: 573
Here the optimal solution is to improve one of the 92s into a 99.
    	
{94, 6, 1, 4}
Returns: 113
Improving 1 to 9 is better than improving 94 to 99 or either of the two remaining options.

**This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information 
without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2010, TopCoder, Inc. All rights reserved.**
"""

#Solution

class CheatingAfterTests:
    def cheat(self, marks):
        sum = 0
        min = marks[0]
        finalSum = 0
        
        for i in marks:
            sum = sum + i
            if min > i:
                min = i
        
        if min < 10:
            finalSum = sum + 9 - min

        elif min > 89:
            finalSum = sum + 99 - min
            
        else:
            finalSum = sum + 90 + (min%10) - min
        
        return finalSum
		
# Points Received - 196.57
