# Problem: EasyConversionMachine
# Used In: SRM 550
# Division: 2
# Level: 1
# Points: 250
# Difficulty : Easy
# Problem Type : Single
# Description: https://community.topcoder.com/stat?c=problem_statement&pm=12125

class EasyConversionMachine:
    def isItPossible(self, originalWord, finalWord, maxMoves):
        moves = 0
        for i in range(0, len(originalWord)):
            if originalWord[i] != finalWord[i]: moves += 1
        
        try:
            return "POSSIBLE" if moves == maxMoves or (maxMoves > moves and maxMoves % moves == 0) else "IMPOSSIBLE"
        except: 
            return "IMPOSSIBLE"    

# Points Received - 248.31

"""
Have used modulus as it is possible to covert into the final word in more than the max moves.

Example: 

Original Word : "aaa"
Final Word    : "bab"
Max Moves     : 4

Returns: "POSSIBLE"

The following sequence of 4 moves does the job:
aaa -> baa -> bab -> aab -> bab

"""