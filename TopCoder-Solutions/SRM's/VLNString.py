# Problem      : VLNString
# Used In      : SRM 226
# Date         : 01.05.2005
# Category     : String Manipulation, String Parsing
# Division     : 2
# Level        : 1
# Round        : 1  
# Points       : 250
# Difficulty   : Easy
# Problem Type : Single
# Description  : https://community.topcoder.com/stat?c=problem_statement&pm=3489

# Class Name   : VLNString
# Method Name  : makeAcronym
# Return Type  : String
# Arg Type     : String

"""
## Problem Statement
An acronym is a sequence of characters that is used to refer to something with a very long name. An acronym is generated from a long name by capitalizing the first letter of every word in the name and concatenating them together. There are three exceptions: the common words "and", "the", and "of" are ignored when generating the acronym. In this problem, a word is defined as one or more non-space characters preceded by either a space or the beginning of the string and followed by either a space or the end of the string. Write a class VLNString with a method makeAcronym that takes a String longName and returns a String with its acronym generated as described above.

## Definition
Class:	VLNString
Method:	makeAcronym
Parameters:	String
Returns:	String
Method signature:	String makeAcronym(String longName)
(be sure your method is public)

## Limits
Time limit (s): 840.000
Memory limit (MB): 64

## Notes
- longName may contain leading and trailing spaces, and there may be more than one space between words.
- The return value may be an empty string.

## Constraints
- longName will contain between 1 and 50 characters, inclusive.
- longName will contain only lowercase English letters ('a' to 'z') and space characters.

## Examples

"dance dance revolution"
Returns: "DDR"

" return of the king "
Returns: "RK"

"the united states of america"
Returns: "USA"

" of the and "
Returns: ""

" "
Returns: ""

**This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.**

"""

#Solution
class VLNString:
    def makeAcronym(self, longName):
        acronym = ""
        longName = longName.replace("and","").replace("the","").replace("of","")
        if longName[0] != ' ' : acronym += longName[0].upper()
        for i in range(1, len(longName)):
            if longName[i-1] == ' ' and longName[i] != ' ' : acronym += longName[i].upper()
        return acronym

# Points Received : 248.98