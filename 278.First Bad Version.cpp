// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int min_version = 1;
        int max_version = n;
        
        if (isBadVersion(1)) {
            return 1;
        }

        while (min_version+1 != max_version) {
            int bound = (max_version - min_version) /2 + min_version;
            if(!isBadVersion(bound))
                min_version = bound;
            else
                max_version = bound;
        }
        
        return max_version;
    }
};
