# Problem      : GreaterGameDiv2
# Used In      : SRM 637
# Date         : 10.23.2014
# Category     : Simple Search, Iteration
# Division     : 2
# Level        : 1
# Round        : 1
# Points       : 250
# Difficulty   : Easy
# Problem Type : Single
# Description  : https://community.topcoder.com/stat?c=problem_statement&pm=13505

# Class Name   : GreaterGameDiv2
# Method Name  : calc
# Return Type  : Integer

"""
## Problem Statement
    
Cat Snuke and wolf Sothe are playing the Greater Game. The game is played with cards. Each card has a number written on it. 
There are 2N cards. The numbers on the cards are the integers between 1 and 2N, inclusive.

At the beginning of the game, each player gets N of the cards and chooses the order in which he wants to play them. 
The game then consists of N turns. In each turn, both players play one of their cards simultaneously. The player who 
revealed the card with the larger number gets a point.

You are given two int[]s: snuke and sothe. The elements of snuke are the numbers on the cards Snuke is going to play, in order. 
Similarly, the elements of sothe are the numbers on the cards Sothe is going to play, in order. Compute and return the number 
of points Snuke will have at the end of the game.

## Definition
Class:  GreaterGameDiv2
Method: calc
Parameters: int[], int[]
Returns:    int
Method signature:   int calc(int[] snuke, int[] sothe)
(be sure your method is public)

## Limits
Time limit (s): 2.000
Memory limit (MB): 256

## Constraints
- N will be between 1 and 50, inclusive.
- snuke and sothe will contain exactly N elements each.
- Each integer in snuke and sothe will be between 1 and 2N, inclusive.
- The integers in snuke and sothe will be distinct.

## Examples

{1,3}
{4,2}
Returns: 1
Snuke loses the first round because 1 is less than 4. Snuke then wins the second round because 3 is greater than 2.

{1,3,5,7,9}
{2,4,6,8,10}
Returns: 0

{2}
{1}
Returns: 1

{3,5,9,16,14,20,15,17,13,2}
{6,18,1,8,7,10,11,19,12,4}
Returns: 6

**This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2010, TopCoder, Inc. All rights reserved.**

"""

#Solution
class GreaterGameDiv2:
    def calc(self, snuke, sothe):

        snukePoints = 0
        length = len(snuke)
        
        for i in range(0, length):
            if snuke[i] > sothe[i]:
                snukePoints += 1
        
        return snukePoints
        
# Points Received : 242.71