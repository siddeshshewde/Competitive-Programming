# Problem      : RosePetals
# Used In      : SRM 315
# Date         : 08.09.2006
# Category     : Simple Search, Iteration
# Division     : 2
# Level        : 1
# Round        : 1  
# Points       : 250
# Difficulty   : Easy
# Problem Type : Single
# Description  : https://community.topcoder.com/stat?c=problem_statement&pm=6635

# Class Name   : RosePetals
# Method Name  : getScore
# Return Type  : int
# Arg Type     : int []

"""
## Problem Statement
"Petals Around the Rose" is a pretty well known logic game. A person who knows the game rolls five dice and then says a number. The other players must guess the rule used to obtain that number. We will not ask you to play this game because it's a tricky one. We will simply tell you that the rule is to sum the number of dots that are around the center dot of each die, like the petals around a rose. If a die has no dot in the center, it has no petals. The face of the die labeled with 1 dot has 0 petals, the face with 2 dots has 0 petals, the face with 3 dots has 2 petals, the face with 4 dots has 0 petals, the face with 5 dots has 4 petals and finally the face with 6 dots has 0 petals as can be seen in the picture.

You are given a int[] dice containing the values of the five dice. Return the total number of petals in this configuration.

## Definition
Class:  RosePetals
Method: getScore
Parameters: int[]
Returns:    int
Method signature:   int getScore(int[] dice)
(be sure your method is public)

## Limits
Time limit (s): 840.000
Memory limit (MB): 64

## Constraints
- dice will contain exactly 5 elements.
- Each element of dice will be between 1 and 6, inclusive.

## Examples

{1, 2, 3, 2, 1}
Returns: 2
In this case we have 0 petals for 1 as there are no dots around the central dot, 0 petals for 2 as it has no central dot, 2 petals for 3, 0 petals for 2 and 0 petals for 1.

{4, 4, 5, 6, 5}
Returns: 8
In this case we have 0 petals + 0 petals + 4 petals + 0 petals + 4 petals = 8 petals.

{1, 2, 3, 3, 5}
Returns: 8

{3, 3, 3, 3, 3}
Returns: 10

{2, 2, 2, 2, 2}
Returns: 0
**This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.**

"""

#Solution
class RosePetals:
    def getScore(self, dice):
        sum = 0
        for i in dice:
            if i == 3:
                sum += 2
            if i == 5:
                sum += 4
        return sum

# Points Received : 249.93
