class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if len(nums) < 2:
            return []
        
        temp = dict()
        for idx in range(len(nums)):
            comp = target - nums[idx]
            
            if comp in temp.keys():
                return [temp[comp], idx]
            else:
                temp[nums[idx]] = idx
                
        return []
