
Problem      : EasyHomework
Used In      : SRM 572
Date         : 03.06.2013
Category     : Simple Math
Division     : 2
Level        : 1
Round        : 1
Points       : 250
Difficulty   : Easy
Problem Type : Single
Description  : https://community.topcoder.com/stat?c=problem_statement&pm=12387
 
Class Name   : EasyHomework 
Method Name  : determineSign 
Return Type  : String
Arg Types    : (tuple (integer))

## Problem Statement
You are taking a course in analysis of algorithms and now you are learning about efficient multiplication of large integers. This week, your professor wanted to give you a homework: given a list of integers, determine the product of all elements in the list.

However, later your professor decided that the homework is too difficult and gave you an easier version instead. In this version, you are only required to determine the sign of the product. The professor also gave you some hints:

- Any integer multiplied by zero is always zero.
- The product of two positive integers is always a positive integer.
- The product of a positive integer and a negative integer is always a negative integer.
- The product of two negative integers is always a positive integer.

More formally, you are given a numbers. Let P be the product of all elements of numbers. If P is positive, return "POSITIVE"; if P is negative, return "NEGATIVE"; else return "ZERO".

## Definition
Class: EasyHomework
Method: determineSign
Parameters: tuple (integer)
Returns: string
Method signature: def determineSign(self, A):

## Limits
Time limit (s): 840.000
Memory limit (MB): 64

## Notes
- It is possible that the product of all elements of numbers is not representable in 32-bit or 64-bit signed integer data type.

## Constraints
- Numbers will contain between 1 and 50 elements, inclusive.
- Each element of numbers will be between -1,000,000,000 and 1,000,000,000, inclusive.

## Examples

{5, 7, 2}
Returns: "POSITIVE"
The product is 70, which is a positive integer.

{-5, 7, 2}
Returns: "NEGATIVE"
This time the product is -70, which is a negative integer.

{5, 7, 2, 0}
Returns: "ZERO"
The product is 0.

{3, -14, 159, -26}
Returns: "POSITIVE"

{-1000000000}
Returns: "NEGATIVE"

{123, -456, 789, -101112, 131415, 161718, 192021, 222324, 252627, 282930, 313233, 343536, 373839, 404142, 434445, 464748, 495051, 525354, 555657}
Returns: "POSITIVE"
The product is 137646845657507645199797549975668224555202443025319758098026743549006534800854109919487361024000, which is a positive integer. Note that this number does not fit even into a 64-bit signed integer data type!

This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.