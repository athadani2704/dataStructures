class Solution {
    public boolean canBeIncreasing(int[] nums) {
        if(nums.length==2)
            return true;
        int pivot = -1;
        for(int i=0; i<nums.length-1; i++){
            if(i==nums.length-2 && pivot==-1)
                return true;
            if(nums[i]>=nums[i+1]){
                if(pivot>-1)
                    return false;
                else
                    pivot = i;
            }
        }
        if(pivot==0)
            return true;
        if(nums[pivot-1]>=nums[pivot+1] && nums[pivot]>=nums[pivot+2])
            return false;
        return true;
    }
}