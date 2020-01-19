# Problem      : TireRotation
# Used In      : SRM 158
# Date         : 08.06.2003
# Category     : Simple Search, Iteration, String Manipulation
# Division     : 2
# Level        : 1
# Round        : 1  
# Points       : 250
# Difficulty   : Easy
# Problem Type : Single
# Description  : https://community.topcoder.com/stat?c=problem_statement&pm=1791

# Class Name   : TireRotation
# Method Name  : getCycle
# Return Type  : int
# Arg Type     : String

"""
## Problem Statement
Tire rotation is a simple but effective part of vehicle preventive maintenance. Without it, the tires of a car may wear out thousands of miles early. The idea is to have each tire spend part of its life on each wheel of the car. To accomplish this, the tire on each wheel is moved to another wheel according to a pattern. First, we assume the wheel positions are numbered left to right, front to rear. Then we establish a rotation pattern:

From the diagram, we see that for each phase of the rotation cycle, a tire is moved from one wheel position to another, according to the following chart:

starting      ending
 wheel        wheel
   1 ---------> 3
   2 ---------> 4
   3 ---------> 2
   4 ---------> 1
Therefore, if our four tires are represented by A, B, C, and D, there are four valid phases of the rotation cycle:

Phase:   1        2        3        4
Tires:  A B ---> D C ---> B A ---> C D
        C D      A B      D C      B A
         ^                          |
         |__________________________|

Write a method will take a String initial and a String current, which will both represent the tires on a car. Each character will be a capital letter ('A'-'Z') and will represent a serial number that identifies a tire. initial will be the starting locations of the tires, and current will be the current locations. The position of a character represents the wheel that the tire is on. The characters represent the wheels in the order: 1, 2, 3, 4 (from the diagram above). Using the rotation pattern above, your method should return a 1, 2, 3, or 4 if the tires are in the 1st, 2nd, 3rd, or 4th phase of the rotation cycle. If the tires have been rotated improperly (that is, they are not in any phase), your method should return -1.

## Definition	
Class:	TireRotation
Method:	getCycle
Parameters:	String, String
Returns:	int
Method signature:	int getCycle(String initial, String current)
(be sure your method is public)

## Limits
Time limit (s): 840.000
Memory limit (MB): 64

## Constraints
-	initial will only contain capital letters ('A' - 'Z', inclusive), and will be exactly 4 characters long.
-	initial will not have any repeated characters.
-	current will be exactly 4 characters long, and will contain the same characters that are in initial.
-	current will not have any repeated characters.

## Examples
	
"ABCD"
"ABCD"
Returns: 1
These tires have not been rotated yet.
    	
"ABCD"
"DCAB"
Returns: 2

The initial locations of the tires are:
A B
C D

After one rotation, the locations of the tires are:
D C
A B
    	
"ABCD"
"CDBA"
Returns: 4

Continuing the rotation, we get the following for phase 3:
B A
D C

And finally, on phase 4:
C D
B A
    	
"ABCD"
"ABDC"
Returns: -1

Here, the rear two tires were moved incorrectly, and the front two were not moved at all.	    	
"ZAXN"
"XNAZ"
Returns: 4

**This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.**

"""

#Solution

class TireRotation:
    def getCycle(self, initial, current):
        a = initial[0]
        b = initial[1]
        c = initial[2]
        d = initial[3]
        
        if current == a+b+c+d:
            return 1
        elif current == d+c+a+b:
            return 2
        elif current == b+a+d+c:
            return 3
        elif current == c+d+b+a:
            return 4
        else:
            return -1

# Points Received : 249.01

"""
#Alternate Solution: Java

public class TireRotation {
	public int getCycle(String initial, String current) {
		String tires = initial;
		for (int i = 1; i <= 4; i++) {
			if (tires.equals(current)) {
				return i;
			}
			tires = "" + tires.charAt(3) + tires.charAt(2) + tires.charAt(0)
					+ tires.charAt(1);
		}
		return -1;
	}
}
"""