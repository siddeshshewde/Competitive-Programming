# Problem: Time
# Used In: SRM 144
# Division: 2
# Level: 1
# Points: 200
# Difficulty : Easy
# Problem Type : Single
# Description: https://community.topcoder.com/stat?c=problem_statement&pm=1708
 
class Time:
    def whatTime(seconds):
        hours = int(seconds / (60 * 60))
        minutes = int(seconds / 60 % 60)
        seconds = int(seconds % 60)
        
        return (str(hours) + ":" + str(minutes) + ":" + str(seconds))


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