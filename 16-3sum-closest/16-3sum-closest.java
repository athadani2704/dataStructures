import java.util.Arrays;

class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int closestDiff = Integer.MAX_VALUE, result = 0;
        Arrays.sort(nums);
        int k, j, reqSum, curDiff;
        for(int i=0; i<nums.length-2; i++){
            j = i+1;
            k = nums.length-1;
            reqSum = target-nums[i];
            while(j<k){
                curDiff = Math.abs(reqSum-nums[j]-nums[k]);
                result = curDiff<closestDiff?nums[i]+nums[j]+nums[k]:result;
                closestDiff = curDiff<closestDiff?curDiff:closestDiff;
                if(nums[j]+nums[k]<reqSum)
                    j++;
                else if(nums[j]+nums[k]>reqSum)
                    k--;
                else
                    return target;
            }
        }
        return result;
    }
}