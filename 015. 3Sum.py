class Solution:
    
    def twoSum(self, nums, target):
        result = []
        wantedNum = {}
        for num in nums:
            if num not in wantedNum:
                wantedNum[-target-num] = num
            else:
                result.append((-target-num, num, target))

        return result

    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) < 3:
            return []
        
        results = []
        sortedNums = sorted(nums)
        for idx in range(len(sortedNums)):
            if idx+1 > len(sortedNums):
                break
            
            searchNums = sortedNums[idx+1:]
            result = self.twoSum(searchNums, sortedNums[idx])

            if len(result) == 0:
                continue
                
            results += result
        
        s = set(results)
        results = [list(t) for t in s]
 
        return results
