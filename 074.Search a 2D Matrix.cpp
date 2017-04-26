class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.size() == 0 || matrix[0].size() == 0)
            return false;
            
        int rowSize = matrix[0].size();
            
        for (int i=0; i<matrix.size(); i++) {
            if (matrix[i][0] <= target && matrix[i][rowSize-1] >= target) {
                for (int j=0; j<rowSize; j++) {
                    if (matrix[i][j] == target)
                        return true;
                }
            }
            
        }
        
        return false;
    }
};
