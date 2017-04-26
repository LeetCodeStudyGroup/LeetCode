public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        if (n <= 0) {
            return -1;
        }
        
        int left = 1;
        int right = n;
        
        if (n == 1) {
            return 1;
        }
        
        while(left < right) {
            int mid = left + (right - left) / 2;
            
            if (isBadVersion(mid)) {
                if (!isBadVersion(mid-1)) {
                    return mid;
                }
                right = mid;
                
            } else {
                left = mid + 1;
            }
        }
        
        return left;
    }
}
