# Problem      : ShootingGame
# Used In      : IIT BHU Mathmania - Codefest 18
# Date         : 09.01.2018
# Category     : Math
# Division     : 1
# Level        : 1
# Round        : 1  
# Points       : 50
# Difficulty   : Easy
# Problem Type : Single
# Description  : https://community.topcoder.com/stat?c=problem_statement&pm=15012

# Class Name   : ShootingGame
# Method Name  : findProbability
# Return Type  : Double

"""
## Problem Statement
    
Alice and Bob are playing a shooting game.

The players take alternating turns, Alice goes first. In each turn the active player gets to take one shot at a target. 
Whoever hits the target first, wins the game.

In any single shot Alice hits the target with probability pAlice, while Bob hits the target with probability pBob.

You are given an int p such that pAlice = p / 10^6. Compute and return the value of pBob for which both players have an 
equal chance of winning the game. If this is impossible, return -1 instead.

## Definition
Class:  ShootingGame
Method: findProbability
Parameters: int
Returns:    double
Method signature:   double findProbability(int p)
(be sure your method is public)

## Limits
Time limit (s): 840.000
Memory limit (MB): 64

## Notes
- Your answer will be accepted if the absolute error between your answer and the correct answer is less than 10-6.

## Constraints
- p will be between 1 and 10^6, inclusive.

## Examples

999997
Returns: -1.0
Alice almost certainly wins the game already with her first shot, regardless of how good Bob happens to be.
        
400000
Returns: 0.6666666666666667
Each of Alice's shots has a 40% probability to hit the target. In order to have the same chance to win as Alice, Bob must be a much better marksman than she is.

**This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2010, TopCoder, Inc. All rights reserved.**

"""

#Solution
class ShootingGame:
    def findProbability(p):
        pAlice = float(p)/10 ** 6
        pBob = pAlice / (1.0 - pAlice)
        return pBob if pBob < 1 else -1.0

# Points Received : 15