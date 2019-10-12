# Problem: MegaCoolNumbersEasy
# Used In: SRM 431
# Division: 2
# Level: 1
# Points: 250
# Difficulty : Easy
# Problem Type : Single
# Description: https://community.topcoder.com/stat?c=problem_statement&pm=10281
 
class MegaCoolNumbersEasy:
    
    def megaCool(n):
        count = 99
        
        while n > 100:
            a = n
            a1 = a % 10
            a2 = int(a / 10 % 10)
            a = int(a /100)
            if a - a2 == a2 - a1:
                count += 1
            n -= 1
        return count
    
    def count(n):
        return n if n < 100 else MegaCoolNumbersEasy.megaCool(n)

# Points Received - 248.69

"""
Another Solution using charAt:

public class MegaCoolNumbersEasy {
    public int count(int N) {
        int megaCool = 0;
        for (int i = 1; i <= N; i++) {
            if (isMegaCool(i)) {
                megaCool++;
            }
        }
        return megaCool;
    }

    boolean isMegaCool(int number) {
        String str = number + "";
        for (int i = 2; i < str.length(); i++) {
            if (str.charAt(i) - str.charAt(i - 1) != str.charAt(i - 1)
                    - str.charAt(i - 2)) {
                return false;
            }
        }
        return true;
    }
}

"""