public class Solution {
    /*
    Implement pow(x, n).
    Input:
    34.00515
    -3
    Output:
    0.02941
    Expected:
    0.00003
     */
    //===

    public double myPow(double x, int n) {
        if(n == 0)
            return 1;
        if(n<0){
            n = -n;
            x = 1/x;
        }
        return (n%2 == 0) ? myPow(x*x, n/2) : x*myPow(x*x, n/2);
    }
}
