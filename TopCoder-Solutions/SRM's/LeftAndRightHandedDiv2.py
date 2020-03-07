# Problem      : LeftAndRightHandedDiv2
# Used In      : SRM 612
# Date         : 03.11.2014  
# Category     : Greedy, Simple Search, Iteration
# Division     : 2
# Level        : 1
# Round        : 1  
# Points       : 250
# Difficulty   : Easy
# Problem Type : Single
# Description  : https://community.topcoder.com/stat?c=problem_statement&pm=13043

# Class Name   : LeftAndRightHandedDiv2  
# Method Name  : count
# Return Type  : Int  
# Arg Types    : String  

"""
## Problem Statement
Some students are seated in a row next to each other. Each of them is either left-handed or right-handed. You are given a String S that describes the row of students. Each character of S is either 'L' or 'R', representing a left-handed or a right-handed person, respectively. The characters describe the row from the left to the right: for all i, the person described by character i+1 sits to the right of the person described by character i.

The students are trying to write down lecture notes. Whenever a left-handed person sits immediately to the right of a right-handed person, their elbows collide when they both try to write at the same time. Compute and return the number of elbow collisions, assuming that all students in the row attempt to write at the same time.
 
## Definition
Class:	LeftAndRightHandedDiv2
Method:	count
Parameters:	String
Returns:	int
Method signature:	int count(String S)
(be sure your method is public)

## Limits
Time limit (s): 840.000  
Memory limit (MB): 64

## Constraints
-	S will contain between 1 and 50 characters, inclusive.
-	Each character of S will be either 'L' or 'R'.

## Examples

"L"
Returns: 0
There's only one person in the row so there are no collisions.
    	
"RRR"
Returns: 0
Everybody is right-handed so there are no collisions.
    	
"LRLRLR"
Returns: 2
There will be two collisions: one of them between the second and the third person from the left (described by S[1] and S[2]) and the other between the fourth and the fifth person.
    	
"LLLRRR"
Returns: 0
    	
"RLRLRL"
Returns: 3

**This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information 
without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.**
"""

#Solution
class LeftAndRightHandedDiv2:
    def count(self, s):
        
        n = 0
        
        for i in range (1, len(s)):
            if s[i-1] == 'R' and s[i] == 'L': 
                n = n+1
        
        return n        

# Points Received - 249.93
