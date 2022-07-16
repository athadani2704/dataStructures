import java.util.Arrays;
import java.util.HashSet;

class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<Integer>();
        for(int cur:nums)
            set.add(cur);
        int[] arr = new int[set.size()];
        int i = 0;
        for(int cur:set)
            arr[i++] = cur;
        // int i = 0;
        // for(int cur:set)
        //     nums[i++] = cur;
        // for(int j=i+1; j<nums.length; j++)
        //     nums[j] = Integer.MAX_VALUE;
        Arrays.sort(arr);
        i = 0;
        int j = 1, maxlen = 0;
        if(arr.length<=1)
            return arr.length;
        while(j<arr.length){
            if(arr[j-1]==arr[j]-1)
                j++;
            else{
                maxlen = Math.max(maxlen, j-i);
                i = j;
                j = i+1;
            }
        }
        if(j==arr.length)
            maxlen = Math.max(maxlen, j-i);
        return maxlen;
    }
}
// [1,2,3,4,100,200,201,202,203,204,205]
//  i        j

// - sort given array
// - initialize i = 0 and j = 1 and maxlen = 0
// - check if len of array is 0 or 1
//     - if yes then return len of array
// - loop thru array(while loop)
//     - check if value at j-1 == (value at j)-1
//         - increment j by 1
//     - if not then do these steps
//         - compare current j-i with maxlen and update maxlen if j-i>maxlen
//         - update i to current j value
//         - update j to i+1
    