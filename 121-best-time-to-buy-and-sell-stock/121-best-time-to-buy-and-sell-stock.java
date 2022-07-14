class Solution {
    public int maxProfit(int[] prices) {
        int minSoFar = prices[0];
        if(prices.length==1)
            return 0;
        int result = 0;
        for(int i=1; i<prices.length; i++){
            result = Math.max(result, prices[i]-minSoFar);
            minSoFar = Math.min(minSoFar, prices[i]);
        }
        return result;
    }
}