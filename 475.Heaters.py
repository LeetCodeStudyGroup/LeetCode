class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        min_len = i = j = 0
        while i < len(houses):
            l = abs(houses[i] - heaters[j])
            while j + 1 < len(heaters) and l >= abs(houses[i] - heaters[j + 1]):
                l, j = abs(houses[i] - heaters[j + 1]), j + 1
            min_len = max(min_len, l)
            i += 1
        return min_len

    def findRadius2(self, houses, heaters):
        houses.sort()
        heaters.sort()
        min_len = i = j = 0
        for i in range(len(houses)):
            j = self.search(heaters, j, len(heaters) - 1, houses[i])
            min_len = max(min_len, abs(houses[i] - heaters[j]))
        return min_len

    def search(self, nums, start, end, target):
        if start >= end:
            return end
        mid = (start + end) / 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target and nums[mid + 1] > target:
            if abs(target - nums[mid]) < abs(target - nums[mid + 1]):
                return mid
            else:
                return mid + 1
        elif nums[mid] <= target:
            return self.search(nums, mid + 1, end, target)
        else:
            return self.search(nums, start, mid, target)
