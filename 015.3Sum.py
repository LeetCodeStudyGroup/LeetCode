class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        num_map = {}
        i = 2
        while i < len(nums):
            self.add_subset(nums, num_map, i - 1)
            target = 0 - nums[i]
            if target in num_map:
                for num_set in num_map[target]:
                    item = ()
                    if nums[i] > num_set[1]:
                        item = ([num_set[0], num_set[1], nums[i]])
                    elif nums[i] < num_set[0]:
                        item = ([nums[i], num_set[0], num_set[1]])
                    else:
                        item = ([num_set[0], nums[i], num_set[1]])
                    self.add_result(result, item)
            i += 1
        return result
    
    def add_result(self, result, in_item):
        for item in result:
            if item[0] == in_item[0] and item[1] == in_item[1]:
                return
        result.append(in_item)
        
    def add_subset(self, nums, num_map, cur):
        i = 0
        while i < cur:
            t = (nums[i], nums[cur])
            if nums[i] > nums[cur]:
                t = (nums[cur], nums[i])
            sum = nums[i] + nums[cur]
            if sum not in num_map:
                num_map[sum] = [t]
            else:
                for sub in num_map[sum]:
                    if t[0] == sub[0]:
                        t = None
                        break
                if t:
                    num_map[sum].append(t)
            i += 1
        