/*
# Problem      : WhiteCells
# Used In      : SRM 367
# Date         : 09.26.2007
# Category     : Simple Search, Iteration
# Division     : 2
# Level        : 1
# Round        : 1  
# Points       : 250
# Difficulty   : Easy
# Problem Type : Single
# Description  : https://community.topcoder.com/stat?c=problem_statement&pm=1708

# Class Name   : WhiteCells
# Method Name  : countOccupied
# Return Type  : Integer
# Arg Type     : String

"""
## Problem Statement
A chessboard is an 8 x 8 grid of cells. Within each column and within each row, cells alternate between black and white. The cell in 
the upper left corner (0, 0) is white. You are given a String[] board, where the j-th character of the i-th element is 'F' if the cell 
in the j-th column from the left and i-th row from the top is occupied, or '.' if it is empty. Return the number of occupied white cells on the board.

## Definition
Class:  WhiteCells
Method: countOccupied
Parameters: String[]
Returns:    int
Method signature:   int countOccupied(String[] board)
(be sure your method is public)

## Limits
Time limit (s): 840.000
Memory limit (MB): 64

## Constraints
- board will contain exactly 8 elements.
- Each element of board will contain exactly 8 characters.
- board will contain only the characters '.' and 'F'.

## Examples

{"........", "........", "........", "........", "........", "........", "........", "........"}
Returns: 0

{"FFFFFFFF", "FFFFFFFF", "FFFFFFFF", "FFFFFFFF", "FFFFFFFF", "FFFFFFFF", "FFFFFFFF", "FFFFFFFF"}
Returns: 32

{".F.F...F", "F...F.F.", "...F.F.F", "F.F...F.", ".F...F..", "F...F.F.", ".F.F.F.F", "..FF..F."}
Returns: 1

{"........", "..F.....", ".....F..", ".....F..", "........", "........", ".......F", ".F......"}
Returns: 2

**This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2010, TopCoder, Inc. All rights reserved.**

*/

#Solution
public class WhiteCells {
    public int countOccupied(String[] board) {
        int whiteOccupied = 0;
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length(); j++) {
                if (board[i].charAt(j) == 'F' && (i + j) % 2 == 0) {
                    whiteOccupied++;
                }
            }
        }
        return whiteOccupied;
    }
}

// Points Received : 249.79