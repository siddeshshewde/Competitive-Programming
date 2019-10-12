
Problem      : BiggestRectangleEasy
Used In      : SRM 318
Date         : 08.29.2006
Category     : Geometry
Division     : 2
Level        : 1
Round        : 1
Points       : 250
Difficulty   : Easy
Problem Type : Single
Description  : https://community.topcoder.com/stat?c=problem_statement&pm=6677
 
Class Name   : BiggestRectangleEasy 
Method Name  : findArea 
Return Type  : integer
Arg Types    : (integer)

## Problem Statement
Little Josh has found several sticks that are each 1 inch long. He wants to form a rectangle with the biggest possible area, using these sticks as the perimeter. He is allowed to glue sticks together, but he is not allowed to break a single stick into multiple shorter sticks.

For example, if Josh has 11 sticks, he can create a 2 x 3 rectangle using 10 sticks. This rectangle has an area of 6 square inches, which is the biggest area that can be achieved in this case.

You will be given an N, and you must return the maximal area (in square inches) of a rectangle that can be created using N or less sticks.

## Definition
Class: BiggestRectangleEasy
Method: findArea
Parameters: integer
Returns: integer
Method signature: def findArea(self, N):

## Limits
Time limit (s): 840.000
Memory limit (MB): 64

## Constraints
- N will be between 4 and 10000, inclusive.

## Examples
0)
11
Returns: 6
The example from the problem statement.

1)
5
Returns: 1
The only rectangle that can be created is a square with 1 inch side.

2)
64
Returns: 256
Josh can create a square with the 16 inches side.

3)
753
Returns: 35344

4)
7254
Returns: 3288782

This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.
