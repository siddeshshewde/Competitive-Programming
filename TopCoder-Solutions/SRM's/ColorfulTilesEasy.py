# Problem      : ColorfulTilesEasy
# Used In      : SRM 472
# Date         : 06.05.2010
# Category     : Greedy
# Division     : 2
# Level        : 1
# Round        : 1  
# Points       : 250
# Difficulty   : Easy
# Problem Type : Single
# Description  : https://community.topcoder.com/stat?c=problem_statement&pm=10940

# Class Name   : ColorfulTilesEasy
# Method Name  : theMin
# Return Type  : integer  
# Arg Types    : String

"""
## Problem Statement
Taro likes colorful things, especially colorful tiles.

Taro's room is divided into L square tiles arranged in a row. Each tile is one of the following four colors: red, green, blue or yellow. You are given a String room. If the i-th character of room is 'R', 'G', 'B' or 'Y', the color of the i-th tile is red, green, blue or yellow, respectively.

He decided to change the color of some tiles so that no two adjacent tiles have the same color. Return the minimal number of tiles he must change.

## Definition
Class:  ColorfulTilesEasy
Method: theMin
Parameters: String
Returns:    int
Method signature:   int theMin(String room)
(be sure your method is public)

## Limits
Time limit (s): 840.000
Memory limit (MB): 64

## Constraints
-   room will contain between 1 and 10 characters, inclusive.
-   Each character in room will be 'R', 'G', 'B' or 'Y'.

## Examples
    
"RRRRRR"
Returns: 3
For example, he can change three tiles in the following way: "RRRRRR" -> "RGRGRG".
        
"GGGGGGG"
Returns: 3
For example, "GGGGGGG" -> "GRGRGRG".
        
"BBBYYYYYY"
Returns: 4
For example, "BBBYYYYYY" -> "BRBYRYRYR".
        
"BRYGYBGRYR"
Returns: 0
The condition is already satisfied, so he doesn't need to change any tiles.
        
"RGGBBBRYYB"
Returns: 3

**This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information 
without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.**

"""

#Solution
class ColorfulTilesEasy:
    def theMin(self, room):
        count = i = 0
        while i < len(room)-1:
            try:
                if room[i] == room[i+1]:
                    count += 1
                    i += 1
                i += 1
            except:
                i += 1
        return count

# Points Received - 249.61

"""
Another Solution:

public class ColorfulTilesEasy {
    public int theMin(String room) {
        int changeNum = 0;
        int sameLength = 1;
        for (int i = 1; i <= room.length(); i++) {
            if (i < room.length() && room.charAt(i) == room.charAt(i - 1)) {
                sameLength++;
            } else {
                changeNum += sameLength / 2;
                sameLength = 1;
            }
        }
        return changeNum;
    }
}
"""