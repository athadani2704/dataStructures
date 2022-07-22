class Solution {
    public int[] countPoints(int[][] points, int[][] queries) {
        int[] result = new int[queries.length];
        int count, i = 0;
        for(int[] arr:queries){
            count = 0;
            for(int[] point:points){
                if(Math.pow(point[0]-arr[0],2)+Math.pow(point[1]-arr[1],2)-Math.pow(arr[2],2)<=0)
                    count++;
            }
            result[i++] = count;
        }
        return result;
    }
}