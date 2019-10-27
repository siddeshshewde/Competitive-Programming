# Problem      : FoxAndGame
# Used In      : SRM 571
# Date         : 02.19.2013
# Category     : Brute Force
# Division     : 2
# Level        : 1
# Round        : 1  
# Points       : 250
# Difficulty   : Easy
# Problem Type : Single
# Description  : https://community.topcoder.com/stat?c=problem_statement&pm=12438

# Class Name   : FoxAndGame
# Method Name  : countStars
# Return Type  : Integer
# Arg Type     : String

"""
## Problem Statement
Fox Ciel is playing the popular game 'Cut the Rope' on her smartphone. The game has multiple stages, and for each stage the player can gain between 0 and 3 stars, inclusive. You are given a String[] result containing Fox Ciel's current results: For each stage, result contains an element that specifies Ciel's result in that stage. More precisely, result[i] will be "---" if she got 0 stars in stage i, "o--" if she got 1 star, "oo-" if she got 2 stars and "ooo" if she managed to get all 3 stars. Return the total number of stars Ciel has at the moment.

## Definition
Class:	FoxAndGame
Method:	countStars
Parameters:	String[]
Returns:	int
Method signature:	int countStars(String[] result)
(be sure your method is public)

## Limits
Time limit (s): 840.000
Memory limit (MB): 64

## Constraints
- result will contain between 1 and 50 elements, inclusive.
- Each element in result will be one of "---", "o--", "oo-", "ooo".
 
## Examples

{"ooo",
 "oo-",
 "o--"}
Returns: 6
This time the answer is 3 + 2 + 1 = 6.
    	
{"ooo",
 "---",
 "oo-",
 "---",
 "o--"}
Returns: 6
    	
{"o--",
 "o--",
 "o--",
 "ooo",
 "---"}
Returns: 6
    	
{"---",
 "o--",
 "oo-",
 "ooo",
 "ooo",
 "oo-",
 "o--",
 "---"}
Returns: 12
    	
{"---",
 "---",
 "---",
 "---",
 "---",
 "---"}
Returns: 0
    	
{"oo-"}
Returns: 2

**This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.**

"""

#Solution
class FoxAndGame:
    def countStars(stars):
        noOfStars = 0
        for i in stars:
            noOfStars += i.count('o')
        return noOfStars

# Points Received : 248.38
