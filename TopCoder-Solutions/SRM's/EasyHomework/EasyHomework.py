# Problem: EasyHomework
# Used In: SRM 572
# Division: 2
# Level: 1
# Points: 200
# Difficulty : Easy
# Problem Type : Single
# Description: https://community.topcoder.com/stat?c=problem_statement&pm=12387
 
class EasyHomework:
    def determineSign(self,numbers):
        sign = 0 
        for i in numbers:
            if i < 0:
                sign += 1
            if i == 0:
                return "ZERO"
                
        return "POSITIVE" if sign % 2 == 0 else "NEGATIVE"


"""
First Attempt:

class Time:
    def whatTime(seconds):
        hours = int(seconds / (60 * 60))
        
        if hours > 0 :
            seconds = int(seconds - (hours * 60 * 60))
            
        minutes = int(seconds / 60)
        
        if minutes > 0 :
            seconds = seconds - (minutes * 60)
            
        seconds = int(seconds)
        return (str(hours) + ":" + str(minutes) + ":" + str(seconds))
"""