# Problem: BiggestRectangleEasy
# Used In: SRM 318
# Division: 2
# Level: 1
# Points: 250
# Difficulty : Easy
# Problem Type : Single
# Description: https://community.topcoder.com/stat?c=problem_statement&pm=6677
 
class BiggestRectangleEasy:
		def findArea(perimeter):
			width = perimeter/4
			length = (perimeter - 2 * width) / 2
			return length * width