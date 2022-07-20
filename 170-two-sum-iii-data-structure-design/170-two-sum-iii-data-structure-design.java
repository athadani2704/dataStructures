import java.util.List;
import java.util.ArrayList;

class TwoSum {
    List<Integer> arr;
    public TwoSum() {
        this.arr = new ArrayList<Integer>();
    }
    
    public void add(int number) {
        this.arr.add(number);
    }
    
    public boolean find(int value) {
        Collections.sort(this.arr);
        int start = 0, end = this.arr.size()-1;
        while(start<end){
            if(this.arr.get(start)+this.arr.get(end)<value)
                start++;
            else if(this.arr.get(start)+this.arr.get(end)>value)
                end--;
            else
                return true;
        }
        return false;
    }
}

/**
 * Your TwoSum object will be instantiated and called as such:
 * TwoSum obj = new TwoSum();
 * obj.add(number);
 * boolean param_2 = obj.find(value);
 */