class Solution(object):class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return None
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        i = 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k and j < len(nums) and k > 0:
                val = nums[i] + nums[j] + nums[k]
                diff = target - val
                if abs(diff) < abs(target - closest):
                    closest = val
                if diff == 0:
                    return target
                elif diff > 0:
                    j += 1
                    while j < len(nums) and nums[j] == nums[j - 1]:
                        j += 1
                else:
                    k -= 1
                    while k > 0 and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
        return closest

    def threeSumClosest2(self, nums, target):
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return nums[0] + nums[1]

        maps = {nums[0] + nums[1]: True}
        inx = 2
        closest = None
        while inx < len(nums):
            cur_closest = self.get_closest_num(sorted(maps.keys()), target - nums[inx]) + nums[inx]
            if closest == None or abs(cur_closest - target) < abs(closest - target):
                closest = cur_closest
            self.add_subset(nums, maps, inx)
            inx += 1
        return closest

    def add_subset(self, nums, maps, inx):
        i = 0
        while i < inx:
            maps[nums[i] + nums[inx]] = True
            i += 1

    def get_closest_num(self, sort_list, target):
        if len(sort_list) == 0:
            return None
        inx = 1
        while inx < len(sort_list):
            if sort_list[inx] > target:
                if abs(sort_list[inx] - target) > abs(sort_list[inx - 1] - target):
                    return sort_list[inx - 1]
                else:
                    return sort_list[inx]
            inx += 1
        return sort_list[len(sort_list) - 1]
