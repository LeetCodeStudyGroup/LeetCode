class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.size() == 0 || matrix[0].size() == 0)
            return false;
            
        for (int i=0; i<matrix.size(); i++) {
            if (target >= matrix[i][0] && target <= matrix[i][matrix[0].size()-1]) {
                int from = 0;
                int end = matrix[0].size()-1;
                while (from <= end) {
                    int index = (from + end) / 2;
                    if (target == matrix[i][index])
                        return true;
                    if (target < matrix[i][index])
                        end = index - 1;
                    else
                        from = index + 1;
                }
            }
        }
        
        return false;
    }
};
