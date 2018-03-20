class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if nums is None or len(nums) < 2:
            return []
        
        temp_dict = {}
        for index in range(len(nums)):
            diff_num = target - nums[index]
            if diff_num in temp_dict:
                return [temp_dict[diff_num], index]
            else:
                temp_dict[nums[index]] = index
            
        return []
