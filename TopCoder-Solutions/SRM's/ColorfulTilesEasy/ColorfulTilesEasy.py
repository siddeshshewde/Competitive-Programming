# Problem: ColorfulTilesEasy
# Used In: SRM 472
# Division: 2
# Level: 1
# Points: 250
# Difficulty : Easy
# Problem Type : Single
# Description: https://community.topcoder.com/stat?c=problem_statement&pm=10940
 
class ColorfulTilesEasy:
    def theMin(self, room):
        count = i = 0
        while i < len(room)-1:
            try:
                if room[i] == room[i+1]:
                    count += 1
                    i += 1
                i += 1
            except:
                i += 1
        return count

# Points Received - 249.61

"""
Another Solution:

public class ColorfulTilesEasy {
    public int theMin(String room) {
        int changeNum = 0;
        int sameLength = 1;
        for (int i = 1; i <= room.length(); i++) {
            if (i < room.length() && room.charAt(i) == room.charAt(i - 1)) {
                sameLength++;
            } else {
                changeNum += sameLength / 2;
                sameLength = 1;
            }
        }
        return changeNum;
    }
}
"""