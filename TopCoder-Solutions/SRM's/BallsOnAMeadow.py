# Correct the description Link and Category



# Problem      : BallsOnAMeadow
# Used In      : SRM 769
# Date         : 10.19.2019
# Category     : Simple Math, String Manipulation
# Division     : 2
# Level        : 1
# Round        : 1  
# Points       : 250
# Difficulty   : Easy
# Problem Type : Single
# Description  : https://community.topcoder.com/stat?c=problem_statement&pm=1708

# Class Name   : BallsOnAMeadow
# Method Name  : count
# Return Type  : Integer
# Arg Type     : String
"""
## Problem Statement
There once was a meadow:

................
Then, somebody dropped some balls onto the meadow:

.()...()().().()
Finally, some grass grew on the meadow, obscuring some of the balls:

.(|||.()(||||||)
You are given the meadow with the final state of the meadow. Return the smallest possible number of balls that were on the meadow.

Empty ground is the character '.', each ball is the string "()", and each blade of grass is the character '|'. It is guaranteed that 
the balls did not overlap. For example, the input meadow = "(()" is invalid. Formally, meadow was produced by taking a string of periods, 
changing some ".." into "()" and then changing some characters to '|'.

## Definition
Class: BallsOnAMeadow
Method: count
Parameters: string
Returns: int
Method signature: int count(string meadow)
(be sure your method is public)

## Limits
Time limit (s):  2.000
Memory limit (MB): 256

## Constraints
- meadow will contain between 1 and 50 characters, inclusive.
- meadow will have the form described in the problem statement.

## Examples

".(|||.()(||||||)"
Returns: 4
The example from the problem statement. Even though in the problem statement there were five balls, the situation seen in this meadow can also be produced using only four balls.

"()"
Returns: 1

"||"
Returns: 0

"(|(|(||)|)|)"
Returns: 6

".....|||||....."
Returns: 0

**This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.**

"""

#Solution
class BallsOnAMeadow:
    def count(meadow):
        
        countBalls = 0
        
        for i in range(0,len(meadow)):
            if meadow[i-1] == '(' or meadow[i] == ')': countBalls += 1
            
        return countBalls    

# Points Received : 175.62

"""
First Attempt:

class BallsOnAMeadow:
    def count(self, siddesh):
        
        final = 0
        countOpen = 0
        countClose = 0
        
        for i in range(0,len(siddesh)):
            if siddesh[i] == '(':
                countOpen += 1
            if siddesh[i] == ')':
                countClose += 1
                if siddesh[i-1] == '(': 
                    final += 1
                    countClose -= 1
                    countOpen -= 1
        
        return final+countOpen+countClose
"""