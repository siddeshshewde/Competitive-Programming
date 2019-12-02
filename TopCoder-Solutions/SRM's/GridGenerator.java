/*
# Problem      : GridGenerator
# Used In      : SRM 256
# Date         : 08.02.2005
# Category     : Simple Math
# Division     : 2
# Level        : 1
# Round        : 1  
# Points       : 250
# Difficulty   : Easy
# Problem Type : Single
# Description  : https://community.topcoder.com/stat?c=problem_statement&pm=4688

# Class Name   : GridGenerator
# Method Name  : generate
# Return Type  : int
# Arg Type     : int[]


## Problem Statement
Consider the following grid of numbers:
 1 0  3  4   1
 4 5  8  15  20
 1 10 23 46  81
 0 11 44 113 240
 3 14 69 226 579
Aside from the top row and left column, each number is equal to the sum of the three numbers immediately left, above, and above-left of it. You will be given a int[], row, representing the first row of a similar grid, and a int[], col, representing the first column of the grid. Your task is to return the value of the lower rightmost location when the values are calculated in the same way. Hence, the above example would be represented by the input row = {1,0,3,4,1}, col = {1,4,1,0,3}.

## Definition
Class:	GridGenerator
Method:	generate
Parameters:	int[], int[]
Returns:	int
Method signature:	int generate(int[] row, int[] col)
(be sure your method is public)

## Limits
Time limit (s): 840.000
Memory limit (MB): 64

## Constraints
- row and col will contain the same number of elements.
- row and col will contain between 2 and 10 elements, inclusive.
- Each element of row and col will be between 0 and 9, inclusive.
- The first element of row will be the same as the first element of col.

## Examples

{1,0,3,4,1}
{1,4,1,0,3}
Returns: 579
The example above.

{9,9,9,9,9,9,9,9,9,9}
{9,9,9,9,9,9,9,9,9,9}
Returns: 13163067
The largest possible return.

{0,0,0,0,0,0,0,0,0}
{0,0,0,0,0,0,0,0,0}
Returns: 0

**This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.**

*/

#Solution
public class GridGenerator {

    public int generate(int[] row, int[] col) {
        int result[][] = new int[row.length][col.length];

        result[0] = row;

        for (int i = 0; i < col.length; i++) {
            result[i][0] = col[i];
        }

        for (int i = 1; i < result.length; i++) {
            for (int j = 1; j < result[i].length; j++) {
                result[i][j] = result[i - 1][j] + result[i - 1][j - 1] + result[i][j - 1];
            }
        }

        return result[row.length - 1][col.length - 1];
    }
}

// Points Received : 237.82
