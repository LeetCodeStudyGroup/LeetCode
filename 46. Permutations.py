import copy

class Solution:
    
    def dfs(self, nums, temp_pernutation, results):
        if len(temp_pernutation) == len(nums):
            deep_copy = copy.deepcopy(temp_pernutation)
            results.append(deep_copy)
            return
        
        for num in nums:
            if num in temp_pernutation:
                continue
                
            temp_pernutation.append(num)
            self.dfs(nums, temp_pernutation, results)
            temp_pernutation.pop()

    
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if nums is None or len(nums) == 0:
            return [[]]
        
        results = []
        temp_pernutation = []
        self.dfs(nums, temp_pernutation, results)
        
        return results
