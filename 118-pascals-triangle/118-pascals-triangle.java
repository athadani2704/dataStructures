import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> arr = new ArrayList<List<Integer>>();
        ArrayList<Integer> temp;
        temp = new ArrayList<Integer>();
        temp.add(1);
        arr.add(temp);
        if(numRows==1)
            return arr;
        else{
            temp = new ArrayList<Integer>();
            temp.add(1); temp.add(1);
            arr.add(temp);
        }
        for(int i=3; i<=numRows; i++){
            temp = new ArrayList<Integer>();
            temp.add(1);
            arr.add(temp);
            for(int j=1; j<arr.get(arr.size()-2).size(); j++){
                arr.get(arr.size()-1).add(arr.get(arr.size()-2).get(j)+arr.get(arr.size()-2).get(j-1));
            }
            arr.get(arr.size()-1).add(1);
        }
        return arr;
    }
}