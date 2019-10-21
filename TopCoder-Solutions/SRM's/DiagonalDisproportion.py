# Problem      : DiagonalDisproportion
# Used In      : SRM 283
# Date         : 01.19.2006
# Category     : Simple Search, Iteration
# Division     : 2
# Level        : 1
# Round        : 1  
# Points       : 250
# Difficulty   : Easy
# Problem Type : Single
# Description  : https://community.topcoder.com/stat?c=problem_statement&pm=6003

# Class Name   : DiagonalDisproportion
# Method Name  : getDisproportion
# Return Type  : Integer
# Arg Type     : tuple(string)
"""
## Problem Statement
Note: this problem statement contains images that may not display properly if viewed outside the applet.

You are to calculate the diagonal disproportion of a square matrix. The diagonal disproportion of a square matrix is the 
sum of the elements of its main diagonal minus the sum of the elements of its collateral diagonal. The main and collateral 
diagonals of a square matrix are shown in figures 1 and 2 respectively.

 

The elements of the main diagonal are shown in green in figure 1, and the elements of the collateral diagonal are shown in cyan in figure 2.

Given a String[] matrix, return its diagonal disproportion. The j'th character of the i'th element of matrix should be treated as the 
element in the i'th row and j'th column of the matrix.

## Definition
Class:  DiagonalDisproportion
Method: getDisproportion
Parameters: String[]
Returns:    int
Method signature:   int getDisproportion(String[] matrix)
(be sure your method is public)

## Limits
Time limit (s): 840.000
Memory limit (MB): 64

## Constraints
-   matrix will contain between 1 and 50 elements, inclusive.
-   Each element of matrix will contain only digits ('0'-'9').
-   The number of characters in each element of matrix will be equal to the number of elements in matrix.

## Examples

    
{"190","828","373"}
Returns: 1
The sum of the elements of the main diagonal is 1+2+3 = 6. The sum of the elements of the collateral diagonal is 0+2+3 = 5. So, the answer is 6-5 = 1.  
        
{"9000","0120","0000","9000"}
Returns: -1  
        
{"6"}
Returns: 0
The matrix has only one element, and this element lies on both the main and collateral diagonals.
        
{"7748297018","8395414567","7006199788","5446757413","2972498628",
"0508396790","9986085827","2386063041","5687189519","7729785238"}
Returns: -24

**This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2010, TopCoder, Inc. All rights reserved.**

"""

#Solution
class DiagonalDisproportion:
    def getDisproportion(matrix):
        
        disproportion = 0
        j = 0
        
        for i in matrix:
            disproportion = disproportion + int(i[j]) - int(i[len(matrix)-j-1])
            j += 1

        return disproportion

# Points Received : 238.97

"""
Another Solution:

public class DiagonalDisproportion {
    public int getDisproportion(String[] matrix) {
        int disproportion = 0;
        for (int i = 0; i < matrix.length; i++) {
            disproportion += matrix[i].charAt(i)
                    - matrix[i].charAt(matrix.length - 1 - i);
        }
        return disproportion;
    }
}
"""