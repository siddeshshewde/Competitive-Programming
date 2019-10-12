# Problem: AccountBalance
# Used In: SRM 288
# Division: 2
# Level: 1
# Points: 250
# Difficulty : Easy
# Problem Type : Single
# Description: https://community.topcoder.com/stat?c=problem_statement&pm=6036

class AccountBalance:
	def processTransactions(balance, transactions):
		for i in transactions:
			k = i.split()
			if k[0] == 'C': balance += k[1]
			else: balance -= k[1]
		return balance	


# Points Received - 75.57

"""
Split Function:
	split() function returns a list of strings after breaking the given string by the specified separator.
	By default - space is considered

	Syntax: str.split(separator, maxsplit)
"""