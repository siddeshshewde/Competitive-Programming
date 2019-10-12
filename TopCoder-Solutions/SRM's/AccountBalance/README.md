
Problem      : AccountBalance  
Used In      : SRM 288  
Date         : 02.08.2006  
Category     : Simple Math, String Parsing  
Division     : 2  
Level        : 1  
Round        : 1  
Points       : 250  
Difficulty   : Easy  
Problem Type : Single  
Description  : https://community.topcoder.com/stat?c=problem_statement&pm=6036  
 
Class Name   : AccountBalance  
Method Name  : processTransactions   
Return Type  : Int  
Arg Types    : (tuple (integer))  

## Problem Statement
You are working for the financial institution TopBank, and you have been tasked with writing a module that will take an initial account balance, along with a list of that day's transactions, and return the ending balance for the day.

Each transaction will be either a credit, which adds funds to the account, or a debit, which removes funds from the account. If a debit exceeds the available funds at the time, then the account balance will go negative. You will be given an int startingBalance, the initial account balance. You will also be given a String[] transactions, the list of transactions for the day. Each element of transactions will be in the form "type amount" (quotes added for clarity). Each type will be 'C' or 'D', for credit or debit, respectively. Each amount will be an integer between 1 and 1000000, inclusive, with no leading zeros. You are to return an int representing the ending balance after processing all of the transactions.

## Definition
Class:	AccountBalance  
Method:	processTransactions  
Parameters: int, String[]  
Returns: int  
Method signature: int processTransactions(int startingBalance, String[] transactions)  
(be sure your method is public)

## Limits
Time limit (s): 840.000  
Memory limit (MB): 64


## Constraints
-	startingBalance will be between 0 and 1000000, inclusive.
-	transactions will have between 0 and 50 elements, inclusive.
-	Each element of transactions will be formatted as "type amount" (quotes added for clarity).
-	Each type will be 'C' or 'D'.
-	Each amount will represent an integer between 1 and 1000000, inclusive, with no leading zeros.

## Examples

100  
{"C 1000", "D 500", "D 350"}  
Returns: 250  
This person had 100 dollars, got their paycheck, then went shopping at two different stores. 100 + 1000 - 500 - 350 = 250.  
    	
100  
{}  
Returns: 100  
With no transactions, the balance doesn't change by the end of the day.  
    	
100  
{"D 50", "D 20", "D 40"}  
Returns: -10  
Uh oh! This person's account is overdrawn.   
    	
53874  
{"D 1234", "C 987", "D 2345", "C 654", "D 6789", "D 34567"}  
Returns: 10580  
Several transactions of both types.  

**This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.**
