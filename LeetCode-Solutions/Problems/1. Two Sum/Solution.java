public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int i=0,j=0;
        for (i = 0 ; i < nums.length ; i++)
        {
            for(j = 0 ; j < nums.length ; j++)
            {
                if (i != j && nums[i] + nums[j] == target)
                {
                     return new int[]{i,j};
                }
            }
        }
        return new int[]{i,j};
    }
}