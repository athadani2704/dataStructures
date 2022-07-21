import java.util.Arrays;

class Solution {
    public boolean isBoomerang(int[][] points) {
        // System.out.println(points[0]+","+ points[1]+","+ points[2]);
        if(Arrays.equals(points[0],points[1]) || Arrays.equals(points[1],points[2]) || Arrays.equals(points[2],points[0]))
            return false;
        double a = points[1][0]!=points[0][0]?Math.abs((points[1][1]-points[0][1])*1.0/(points[1][0]-points[0][0])):Double.POSITIVE_INFINITY;
        double b = points[1][0]!=points[2][0]?Math.abs((points[1][1]-points[2][1])*1.0/(points[1][0]-points[2][0])):Double.POSITIVE_INFINITY;
        double c = points[0][0]!=points[2][0]?Math.abs((points[0][1]-points[2][1])*1.0/(points[0][0]-points[2][0])):Double.POSITIVE_INFINITY;
        return a!=b || b!=c || c!=a;
    }
}