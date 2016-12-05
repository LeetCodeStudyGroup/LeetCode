class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4: return []
        nums.sort()
        cache = {}
        for i in range(len(nums)):
            if nums[i] in cache:
                cache[nums[i]].append((i,))
            else:
                cache[nums[i]] = [(i,)]
        cache = self.create_cache(nums, cache, nums[0] * 2, nums[-1] * 2, target)
        cache = self.create_cache(nums, cache, nums[0], nums[-1], target)
        rst = []
        for i in range(len(nums)):
            if (target - nums[i]) in cache:
                for item in cache[target - nums[i]]:
                    if item[-1] < i:
                        new_item = item + (i,)
                        if not self.contain(nums, rst, new_item):
                            rst.append(new_item)
        return map(lambda item: map(lambda i: nums[i], item), rst)

    def create_cache(self, nums, cache, min, max, target):
        new_cache = {}
        for key in cache.keys():
            for item in cache[key]:
                for i in range(item[-1] + 1, len(nums)):
                    new_sum, new_item = key + nums[i], item + (i,)
                    if (nums[i] >= 0 and new_sum > target) or (nums[i] < 0 and new_sum + min > target) or \
                        (target > 0 and nums[i] > 0 and new_sum + max * 2 < target):
                        break
                    if new_sum in new_cache:
                        if not self.equals(nums, new_cache[new_sum][-1], new_item):
                            new_cache[new_sum].append(new_item)
                    else:
                        new_cache[new_sum] = [(new_item)]
        return new_cache

    def contain(self, nums, ary, val):
        for items in ary:
            if self.equals(nums, items, val):
                return True
        return False

    def equals(self, nums, items, val):
        for i in range(len(items)):
            if nums[items[i]] != nums[val[i]]:
                return False
        return True
