# Problem      : WritingWords
# Used In      : SRM 618
# Date         : 04.24.2014
# Category     : Brute Force, Simulation
# Division     : 2
# Level        : 1
# Round        : 1  
# Points       : 250
# Difficulty   : Easy
# Problem Type : Single
# Description  : https://community.topcoder.com/stat?c=problem_statement&pm=13072

# Class Name   : WritingWords
# Method Name  : write
# Return Type  : Integer
# Arg Type     : String

"""
## Problem Statement
Fox Ciel wants to type a word on her old cell phone. The cell phone has only one button. The letter A is typed by tapping the button once, 
B by tapping it twice in a row, and so on, in alphabetical order. Thus, the last letter Z is typed by tapping the button 26 times without a pause.

You are given a String word. Compute and return the answer to the following question: How many times will Ciel tap the button while typing this word?

## Definition
Class:  WritingWords
Method: write
Parameters: String
Returns:    int
Method signature:   int write(String word)
(be sure your method is public)

## Limits
Time limit (s): 2.000
Memory limit (MB): 256

## Notes
-   While typing a word, Ciel has to make a short pause after typing each letter, so that the phone can tell when one letter ends and another letter begins. These pauses do not matter in this problem.

## Constraints
-   word will contain between 1 and 50 characters, inclusive.
-   Each character in word will be an uppercase English letter ('A'-'Z').

## Examples

"ABC"
Returns: 6
To type ABC, Ciel will do the following:
Tap the button once to type A.
Tap the button twice to type B.
Tap the button three times to type C.
The total number of taps is 1+2+3 = 6. 
        
"VAMOSGIMNASIA"
Returns: 143  
        
"TOPCODER"
Returns: 96 
        
"SINGLEROUNDMATCH"
Returns: 183
        
"ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"
Returns: 1300
**This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2010, TopCoder, Inc. All rights reserved.**

"""

#Solution
class WritingWords:
    def calc(self, word):
        countButtons = 0
        for i in word:
            countButtons += ord(i)-64 
        return countButtons

# Points Received : 249.60