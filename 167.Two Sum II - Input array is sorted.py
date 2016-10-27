class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(numbers) - 1
        while start < end:
            end = self.search(numbers, target - numbers[start], start + 1, end)
            if numbers[start] + numbers[end] == target:
                return start + 1, end + 1
            index = self.search(numbers, target - numbers[end], start + 1, end)
            if index > start:
                start = index
                if numbers[start] + numbers[end] == target:
                    return start + 1, end + 1
            else:
                start += 1
                
    def search(self, numbers, target, start, end):
        if start == end:
            return start
        mid = (start + end) / 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target and numbers[mid + 1] > target:
            return mid
        elif numbers[mid] > target:
            return self.search(numbers, target, start, mid - 1)
        else:
            return self.search(numbers, target, mid + 1, end)
