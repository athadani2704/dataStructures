import java.util.HashMap;
import java.util.Map;

class SparseVector {
    HashMap<Integer, Integer> hash = new HashMap<>();
    int numKeys = 0;
    SparseVector(int[] nums) {
        for(int i=0; i<nums.length; i++){
            if(nums[i]>0){
                hash.put(i, nums[i]);
                this.numKeys++;
            }
        }
    }
    
	// Return the dotProduct of two sparse vectors
    public int dotProduct(SparseVector vec) {
        int result = 0;
        SparseVector parseThis, otherOne;
        if(vec.numKeys<=this.numKeys){
            parseThis = vec;
            otherOne = this;
        }
        else{
            parseThis = this;
            otherOne = vec;
        }
        for(Map.Entry<Integer, Integer> entry:parseThis.hash.entrySet()){
            int key = entry.getKey(), value = entry.getValue();
            if(otherOne.hash.containsKey(key))
                result += otherOne.hash.get(key)*value;
        }
        return result;
    }
}

// Your SparseVector object will be instantiated and called as such:
// SparseVector v1 = new SparseVector(nums1);
// SparseVector v2 = new SparseVector(nums2);
// int ans = v1.dotProduct(v2);